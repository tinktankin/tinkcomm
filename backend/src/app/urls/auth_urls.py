from django.urls import path

from app.api.signup import (
    signup,
)
from app.api.login import (
    login,
)

urlpatterns = [
    path('login', login),
    path('signup', signup),
]
