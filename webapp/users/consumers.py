import asyncio
import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer


class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'random_numbers',
            self.channel_name
        )
        await self.accept()

        while True:
            await asyncio.sleep(2)
            random_number = random.randint(1, 100)
            await self.channel_layer.group_send(
                'random_numbers',
                {
                    'type': 'send_random_number',
                    'random_number': random_number,
                }
            )

    async def send_random_number(self, event):
        await self.send(text_data=json.dumps({
            'random_number': event['random_number']
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'random_numbers',
            self.channel_name
        )