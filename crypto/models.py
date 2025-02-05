from django.db import models
from django.conf import settings
from django.utils import timezone
from crypto.utils import crypto_image_path
from django.contrib import admin

class Crypto(models.Model):
    SIGNAL_CHOICES = [
        ('hold', 'On Hold'),
        ('none', 'No Signal')
    ]

    signal = models.CharField(
        max_length=10,
        choices=[('hold', 'On Hold'), ('none', 'No Signal')],
        default='none',
        help_text='Trading signal for this cryptocurrency'
    )

    signal_description = models.TextField(
        blank=True,
        help_text='Additional details about the trading signal'
    )

    symbol = models.CharField(
        max_length=10,
        help_text='Crypto Ticker used for querying from CoinMarketCap',
        unique=True
    )
    display_name = models.CharField(
        max_length=64,
        help_text='Used as the header when charting'
    )
    show_overall = models.BooleanField(
        default=False,
        help_text='Show overall value instead of current price'
    )
    show_chart = models.BooleanField(
        default=False,
        verbose_name='Chart crypto',
        help_text='Show 7-day chart with price trend on Dashboard'
    )
    image = models.ImageField(
        default='crypto/default.png',
        upload_to=crypto_image_path
    )
    enabled = models.BooleanField(
        default=True,
        help_text='Hides crypto from Dashboard and does not pull further information'
    )
    order = models.PositiveSmallIntegerField(default=999)
    updated = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)

    # Trading Signals
    signal = models.CharField(
        max_length=10,
        choices=SIGNAL_CHOICES,
        default='none',
        help_text='Trading signal for this cryptocurrency'
    )
    signal_description = models.TextField(
        blank=True,
        help_text='Additional details about the trading signal'
    )

    class Meta:
        ordering = ('order', 'symbol')

    def __str__(self):
        return self.symbol

class CryptoData(models.Model):
    crypto = models.ForeignKey(
        Crypto, on_delete=models.CASCADE, related_name='data'
    )
    source_price = models.FloatField()
    source_currency = models.CharField(max_length=4)
    target_price = models.FloatField()
    target_currency = models.CharField(max_length=4)
    percent_day = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='24h Percentual Change'
    )
    rank = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Price Data'
        verbose_name_plural = 'Price Data'
        get_latest_by = 'timestamp'

    def save(self, *args, **kwargs):
        if not self.target_currency:
            self.target_currency = (
                settings.TARGET_CURRENCY or settings.COINMARKET_CURRENCY
            )
        if not self.target_price:
            self.target_price = self.source_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'[{self.crypto}] {self.target_price}@{self.timestamp}'

    @property
    @admin.display(ordering='target_price', description='Price')
    def price(self) -> str:
        return f'{self.target_price:.20f} {self.target_currency}'

    @property
    @admin.display(ordering='percent_day', description='24h percentual')
    def percent(self) -> str:
        return f'{self.percent_day:+.2f} %'


class CryptoPurchases(models.Model):
    crypto = models.ForeignKey(
        Crypto, on_delete=models.CASCADE, related_name='purchases'
    )
    amount = models.FloatField()
    buy_price = models.FloatField()
    buy_currency = models.CharField(max_length=4)
    target_price = models.FloatField(null=True, blank=True)  # Allow null values
    target_currency = models.CharField(max_length=4, blank=True)
    bought_at = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def save(self, *args, **kwargs):
        if not self.buy_currency:
            self.buy_currency = settings.TARGET_CURRENCY or settings.COINMARKET_CURRENCY
        if not self.target_currency:
            self.target_currency = settings.TARGET_CURRENCY or settings.COINMARKET_CURRENCY
        if not self.target_price:
            self.target_price = self.buy_price
        super().save(*args, **kwargs)

    @property
    def total_price(self):
        return f'{(self.amount * self.target_price):.2f} {self.target_currency}'
    
class Alert(models.Model):
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    price = models.FloatField(help_text='Price of crypto in target currency to surpass')
    send_discord = models.BooleanField(default=False, help_text='Send alert to Discord when triggered')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_above = models.BooleanField(default=True, help_text='Alert when price goes above (True) or below (False) target')
    active = models.BooleanField(default=True, help_text='Alert is active')
    last_triggered = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Price Alert'

    def __str__(self):
        direction = 'above' if self.is_above else 'below'
        return f'[{self.crypto}] {direction} {self.price}'
