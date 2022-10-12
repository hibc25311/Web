from django.db import models


# Create your models here.
class CryptoNews(models.Model):

    news_url = models.URLField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    img_url = models.URLField(max_length=200)
    media_info = models.CharField(max_length=80)
    post_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    site = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Coin(models.Model):

    symbol = models.CharField(max_length=20)
    price = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.symbol
