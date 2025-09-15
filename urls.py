from django.urls import path
from .webhook import WebhookList, WebhookHandler

urlpatterns = [
    path('webhook/', WebhookList.as_view(), name='webhook_list'),
    path('webhook/<str:botname>/', WebhookHandler.as_view(), name='webhook_handler'),
]