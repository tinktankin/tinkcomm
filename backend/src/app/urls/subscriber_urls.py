from django.urls import path

from app.api.subscriber import subscriber_list

urlpatterns = [
    path('', subscriber_list),
]
