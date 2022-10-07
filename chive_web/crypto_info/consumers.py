import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache


class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('coins', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('coins', self.channel_name)

    async def send_new_data(self, event):
        coin_data = event['data']
        await self.send(json.dumps(coin_data))

    async def receive(self, text_data):
        coin_symbols = json.loads(text_data)

        #get coin price by cache
        coin_1_price = cache.get(coin_symbols['message'][0])
        coin_2_price = cache.get(coin_symbols['message'][1])

        price_ratio = round((coin_1_price / coin_2_price), 3)
        #
        await self.send(
            json.dumps({
                'price_ratio': price_ratio,
                'coin_1': coin_symbols['message'][0],
                'coin_2': coin_symbols['message'][1]
            }))
