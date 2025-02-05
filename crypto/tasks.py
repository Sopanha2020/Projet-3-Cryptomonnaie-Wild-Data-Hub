from celery import shared_task
from crypto.services import crypto_update

@shared_task
def crypto_update_task():
    """Task to update crypto prices from CoinMarketCap API"""
    crypto_update()