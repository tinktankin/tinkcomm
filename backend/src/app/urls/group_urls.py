from django.urls import path

from app.api.group import create_group

urlpatterns = [
    path('', create_group),
]