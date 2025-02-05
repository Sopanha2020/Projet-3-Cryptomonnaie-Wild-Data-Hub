from django.shortcuts import render
from django.conf import settings

from crypto.models import Crypto
from crypto.selectors import crypto_invest, crypto_ohlc


def landing(request):
    crypto_queryset = Crypto.objects\
        .order_by('order', 'symbol')\
        .prefetch_related('data', 'purchases')\
        .filter(enabled=True)
    cryptos = crypto_invest(
        crypto_queryset=crypto_queryset
    )


    context = {
        'cryptos': cryptos,
    }
    return render(request, 'crypto/dashboard.html', context)
