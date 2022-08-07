from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''
        Consumer that handles the chat function in between two people
    '''
    pass


class GroupChatConsumer(AsyncJsonWebsocketConsumer):
    '''
        Consumer that handles the chat function in between group of people
    '''
    pass