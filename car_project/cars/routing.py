from django.conf.urls import url

from cars.consumers import CarDataConsumer

websocket_urlpatterns = [
    url(r'^ws/connect/$', CarDataConsumer.as_asgi()),
]