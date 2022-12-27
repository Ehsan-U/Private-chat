from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "Dream_chat"
        # assign a channel to group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        # discard a group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    # send message to all group-members
    async def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']
        username = text_data['username']
        await self.channel_layer.group_send(self.group_name, {"type":"chat_msg", "message":message, "username":username})

    # send back message to websocket connection (client that initiate websocket connection)
    async def chat_msg(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({"message":message, "username":username}))







