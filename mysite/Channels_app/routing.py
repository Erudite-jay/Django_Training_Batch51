from django.urls import path
from .consumers import MySyncConsumer

ws_urlpatterns=[

path('ws/sc/',MySyncConsumer.as_asgi()),

]