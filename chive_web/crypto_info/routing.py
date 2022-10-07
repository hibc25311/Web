from django.urls import re_path
from crypto_info import consumers

websocket_urlpattern = [re_path(r'ws/price', consumers.CoinConsumer.as_asgi())]
