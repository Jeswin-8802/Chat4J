import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message, Forum
from accounts.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = '%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'image': await self.get_user_image(username),
            'time': await self.get_msg_time()
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        if message != '':
            m = Message.objects.create(
                user = User.objects.get(username = username),
                room = Forum.objects.get(name = room),
                content = message)
            Forum.objects.get(name = room).messages.add(m)

    @sync_to_async
    def get_user_image(self, username):
        return User.objects.get(username = username).image.url
    
    @sync_to_async
    def get_msg_time(self):
        x = Message.objects.last().timestamp.strftime("%B %d, %Y, %I:%M %p")
        return ((x[:-8] + x[-7:-2] if x[-8:-7] == '0' else x[:-2]) + x[-2:-1].lower() + '.' + 'm.')