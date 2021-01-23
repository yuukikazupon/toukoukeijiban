# django_channels/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import toukoukeijibanapp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            toukoukeijibanapp.routing.websocket_urlpatterns
        )
    ),
})
