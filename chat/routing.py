from django.urls import path

from . import consumers

websocket_urlpatterns = [
    # kwargs fetched by async
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]