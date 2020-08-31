from django.urls import path

from app.api.subscriber import subscriber_list, subscriber_detail

urlpatterns = [
    path('', subscriber_list),
    path('<int:pk>', subscriber_detail),
]
