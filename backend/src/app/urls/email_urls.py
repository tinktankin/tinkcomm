from django.urls import path

from app.api.email import send_email, config_email

urlpatterns = [
    path('', send_email),
    path('config', config_email),
]
