from .consumers import ChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r"chat/socket/", ChatConsumer.as_asgi())
]