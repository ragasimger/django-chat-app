from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''
        Consumer that handles the chat function in between two people
    '''
    async def connect(self):
        print("WebSocket Connection Established")
        await self.accept()

    async def receive_json(self, content=None, **kwargs):
        await self.send_json(
            {
                'message' : content
            }
        )
        print("Message Sent")

    async def disconnect(self, close_code):
        print("WebSocket Disconnected", close_code)
        

class GroupChatConsumer(AsyncJsonWebsocketConsumer):
    '''
        Consumer that handles the chat function in between group of people
    '''
    pass