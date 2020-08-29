from django.urls import path

from app.api.add_subscriber import add_subscriber
from app.api.subscriber import get_all_subscriber

urlpatterns = [
    path('add', add_subscriber),
    path('', get_all_subscriber),
]
