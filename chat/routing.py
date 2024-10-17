from django.urls import path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path(r'ws/socket-server/<str:room_name>/', ChatConsumer.as_asgi()),
]

