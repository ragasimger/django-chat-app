from django.urls import path

from apps.chat.consumers import ChatConsumer, GroupChatConsumer

websocket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
    path('ws/group-chat/', GroupChatConsumer.as_asgi()),
]