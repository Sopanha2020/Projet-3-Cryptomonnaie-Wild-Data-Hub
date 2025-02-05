import json
import redis
import pandas as pd
import numpy as np
import ta
import warnings
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVR
from django.db.models.signals import pre_save
from django.dispatch import receiver
from crypto.models import CryptoData  
from crypto.services import logger, send_discord_alert, check_price_alerts
# Suppress warnings
warnings.filterwarnings("ignore")

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

### 🔹 Function: Store and Retrieve Data from Redis

def store_historical_data(symbol: str, data: list) -> None:
    """Store historical cryptocurrency data in Redis cache."""
    cache_key = f"crypto_price:{symbol}"
    redis_client.set(cache_key, json.dumps(data))

def get_historical_data(symbol: str) -> pd.DataFrame:
    """Retrieve historical cryptocurrency data from Redis cache."""
    cache_key = f"crypto_price:{symbol}"
    cached_data = redis_client.get(cache_key)
    
    if not cached_data:
        return pd.DataFrame()  # Return empty DataFrame if no data is found
    
    data = json.loads(cached_data)
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    return df.sort_values('timestamp')

### 🔹 Function: Feature Engineering

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Generate technical indicators for the dataset."""
    if df.empty:
        return df
    
    df = df.dropna().copy()
    df["returns"] = df["close"].pct_change(1)  # Calculate daily returns
    
    # Add all technical indicators
    df_ta = ta.add_all_ta_features(
        df, open="open", high="high", low="low", close="close", volume="volume", fillna=True
    )
    
    df_final = pd.concat([df_ta, df], axis=1).dropna()
    return df_final

### 🔹 Function: SVM Regression Trading Model

def svm_reg_trading(df: pd.DataFrame) -> tuple:
    """Train an SVM model to predict trading signals."""
    df = feature_engineering(df)
    if df.empty:
        return False, False
    
    split_idx = int(0.90 * len(df))  # Use 90% of the data for training
    
    # Prepare training and test datasets
    X = df.select_dtypes(include=[np.number]).drop(columns=["returns"], errors='ignore')
    y = df.get("returns", pd.Series(dtype='float64'))
    
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train = y.iloc[:split_idx]
    
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Dimensionality reduction using PCA
    pca = PCA(n_components=min(6, X_train.shape[1]))  # Ensure PCA components don't exceed feature count
    X_train_pca = pca.fit_transform(X_train_scaled)
    X_test_pca = pca.transform(X_test_scaled)
    
    # Train the SVM model
    model = SVR()
    model.fit(X_train_pca, y_train)
    
    # Predict trading signals
    df["prediction"] = model.predict(np.vstack((X_train_pca, X_test_pca)))
    
    # Determine buy/sell signals
    latest_prediction = df["prediction"].iloc[-1]
    return latest_prediction > 0, latest_prediction <= 0

### 🔹 Function: Get Trading Signal

def get_trading_signal(symbol: str) -> tuple:
    """Compute trading signal using historical data."""
    df = get_historical_data(symbol)
    if df.empty:
        return 'none', 'No data available'
    
    try:
        buy_signal, sell_signal = svm_reg_trading(df)
        if buy_signal:
            return 'buy', f'Buy signal detected for {symbol}'
        elif sell_signal:
            return 'sell', f'Sell signal detected for {symbol}'
        return 'hold', f'Hold position for {symbol}'
    except Exception as e:
        return 'none', f'Error calculating signal: {str(e)}'

### 🔹 Django Signal: Update Crypto Signal on Save

@receiver(pre_save, sender=CryptoData)
def update_crypto_signal(sender, instance, **kwargs):
    """Update crypto signal when new price data is saved"""
    try:
        signal, description = get_trading_signal(instance.crypto.symbol)
        
        # Check if signal has changed
        if signal != instance.crypto.signal:
            # Send Discord alert
            send_discord_alert(
                crypto_symbol=instance.crypto.symbol,
                signal_type=signal,
                price=instance.target_price,
                description=description
            )
        
        # Update crypto signal
        instance.crypto.signal = signal
        instance.crypto.signal_description = description
        instance.crypto.save()
    except Exception as e:
        logger.error(f"Error updating signal: {str(e)}")

def check_alerts(sender, instance, created, **kwargs):
    if created:
        check_price_alerts(instance)