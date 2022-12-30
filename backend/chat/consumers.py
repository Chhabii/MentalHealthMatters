from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync
from .models import Group, Chat
from channels.db import database_sync_to_async

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print("Websocket Connected....")
        # print("Channel Layer...",self.channel_layer)
        # print("Channel name...",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        # print("Group Name...",self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        
    
    async def receive(self,text_data=None,bytes_data=None):
        # print("Message Received from Client...",text_data)
        data = json.loads(text_data)
        message = data['msg']
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        if self.scope['user'].is_authenticated:
            chat = Chat(
                user = str(self.scope['user']),
                content = data['msg'],
                group = group
            )
            await database_sync_to_async(chat.save)()

            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'chat.message',
                    'message': message,
                    'user':str(self.scope['user'])

                }
            )
        else:
            await self.send(text_data=json.dumps({
                'msg':"Login Required"
            }))
    async def chat_message(self,event):
        # print("Event.......",event)
        
        await self.send(text_data=json.dumps({
            'msg':event['message'],
            'user':event['user']

        }))

    async def disconnect(self,close_code):
        # print("Websocket Disconnected....",close_code)
        await self.channel_layer.group_discard(
                    self.group_name,
                    self.channel_name
                )