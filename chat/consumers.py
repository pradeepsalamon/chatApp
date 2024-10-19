import json
# from .models import Message, Room
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = {
            'type': 'send_message',
            'data' : data
        }
        # await self.create_message(data = data)
        await self.channel_layer.group_send(self.room_name, event)
        
    async def send_message(self, event):
        data = event['data']
        await self.send(text_data=json.dumps({'data':data}))
        
    # @database_sync_to_async
    # def create_message(self, data):
    #     get_room = Room.objects.get(room_name = data['roomname'])
    #     new_message = Message(room = get_room, sender = data['sender'], message = data['message'])
    #     new_message.save()