import logging
from django.conf import settings
import requests
import redis
import json
from datetime import datetime, timedelta
from django.utils import timezone
from crypto.constants import ENDPOINT, HEADERS
from crypto.models import Crypto, CryptoData, Alert

logger = logging.getLogger(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def crypto_update():
    """ Updates all enabled Cryptos' price information """
    cryptos = Crypto.objects.filter(enabled=True).values_list('symbol', flat=True)
    if not cryptos:
        logger.info('No cryptos available for updating; skipping...')
        return
        
    crypto_quotes = crypto_get(crypto_symbols=cryptos)
    
    for symbol, quote in crypto_quotes.items():
        try:
            crypto = Crypto.objects.get(symbol=symbol)
            price_data = CryptoData.objects.create(
                crypto=crypto,
                source_price=quote.get('price'),
                source_currency=settings.COINMARKET_CURRENCY,
                target_price=quote.get('price'),
                target_currency=settings.COINMARKET_CURRENCY,
                percent_day=quote.get('percent_day'),
                rank=quote.get('rank')
            )
            
            # Store in Redis with timestamp
            cache_key = f"crypto_price:{symbol}"
            cached_data = redis_client.get(cache_key)
            if cached_data:
                historical_data = json.loads(cached_data)
            else:
                historical_data = []
                
            historical_data.append({
                'timestamp': datetime.now().timestamp(),
                'open': float(price_data.target_price),
                'high': float(price_data.target_price),
                'low': float(price_data.target_price),
                'close': float(price_data.target_price),
                'volume': 0  # You might want to store actual volume if available
            })
            
            # Keep only last 24 hours of data
            cutoff_time = (datetime.now() - timedelta(days=1)).timestamp()
            historical_data = [d for d in historical_data if d['timestamp'] > cutoff_time]
            
            # Store updated data back in Redis
            redis_client.set(cache_key, json.dumps(historical_data))
            
        except Exception as e:
            logger.error(f'Error creating price data for {symbol}: {str(e)}')
            continue

def check_price_alerts(crypto_data):
    """Check if any price alerts should be triggered"""
    alerts = Alert.objects.filter(
        crypto=crypto_data.crypto,
        active=True
    )
    
    current_price = crypto_data.target_price
    
    for alert in alerts:
        should_trigger = (
            (alert.is_above and current_price > alert.price) or
            (not alert.is_above and current_price < alert.price)
        )
        
        if should_trigger:
            if alert.send_discord:
                direction = 'above' if alert.is_above else 'below'
                message = (
                    f"{alert.crypto.symbol} price is {direction} {alert.price}\n"
                    f"Current price: {current_price}"
                )
                send_discord_alert(
                    crypto_symbol=alert.crypto.symbol,
                    signal_type='alert',
                    price=current_price,
                    description=message
                )
            
            # Update last triggered time
            alert.last_triggered = timezone.now()
            alert.save()

def crypto_get(*, crypto_symbols: list) -> dict:
    """ Queries the latest cryptos price information from CoinMarket """
    HEADERS.setdefault('X-CMC_PRO_API_KEY', settings.COINMARKET_KEY)
    params = {
        'symbol': ','.join(crypto_symbols),
        'convert': settings.TARGET_CURRENCY or settings.COINMARKET_CURRENCY
    }
    
    response = requests.get(
        f'{ENDPOINT}/v1/cryptocurrency/quotes/latest',
        headers=HEADERS,
        params=params
    )
    
    data = response.json()
    if data.get('status', {}).get('error_code'):
        logger.warning(f'CoinMarket returned an error! Response: {data}')
        return {}
        
    logger.info(f'Consumed {data.get("status", {}).get("credit_count")} CoinMarket Credit for request')

    result = {}
    for symbol in crypto_symbols:
        try:
            coin_data = data.get('data', {}).get(symbol, {})
            convert_currency = settings.TARGET_CURRENCY or settings.COINMARKET_CURRENCY
            coin_quote = coin_data.get('quote', {}).get(convert_currency, {})
            
            result[symbol] = {
                'rank': coin_data.get('cmc_rank'),
                'price': coin_quote.get('price'),
                'percent_day': coin_quote.get('percent_change_24h'),
                'currency': convert_currency
            }
            
            logger.debug(
                f'[{symbol}] {coin_quote.get("price")} {convert_currency} '
                f'({coin_quote.get("percent_change_24h"):+.2f} %) -- '
                f'Rank: {coin_data.get("cmc_rank")}'
            )
        except Exception as e:
            logger.error(f'Error processing {symbol}: {e}')
            continue

    return result

def send_discord_alert(crypto_symbol, signal_type, price, description):
    """Send alert to Discord channel"""
    webhook_url = settings.DISCORD_WEBHOOK_URL
    
    # Set color based on signal type
    colors = {
        'buy': 0x00ff00,  # Green
        'sell': 0xff0000,  # Red
        'hold': 0xffff00,  # Yellow
    }
    
    embed = {
        "title": f"🚨 {crypto_symbol} Signal Alert",
        "description": description,
        "color": colors.get(signal_type, 0x808080),
        "fields": [
            {
                "name": "Signal",
                "value": signal_type.upper(),
                "inline": True
            },
            {
                "name": "Price",
                "value": f"€{price:,.2f}",
                "inline": True
            }
        ],
        "timestamp": datetime.now().isoformat()
    }
    
    payload = {
        "content": f"New {signal_type.upper()} signal for {crypto_symbol}!",
        "embeds": [embed]
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            logger.info(f"Discord alert sent successfully for {crypto_symbol}")
        else:
            logger.error(f"Failed to send Discord alert: {response.status_code}")
    except Exception as e:
        logger.error(f"Error sending Discord alert: {str(e)}")