from django.shortcuts import render
from .models import Coin, CryptoNews
from django.core.cache import cache


def home(request):
    return render(request, 'crypto_info/home.html', {})


def coin(request):
    coin = Coin.objects.all().order_by('id')

    #store the symbol+price in cache for calculating ratio
    for c in coin:
        cache.set(c.symbol, c.price)

    return render(request, 'crypto_info/coin.html', {'coin': coin})


def news(request):
    news = CryptoNews.objects.all()
    return render(request, 'crypto_info/news.html', {'news': news})
