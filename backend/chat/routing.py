from django.urls import path 
from . import consumers 

websocket_urlpatterns = [
    path("ws/awsc/<str:groupname>/",consumers.MyAsyncWebsocketConsumer.as_asgi()),
]