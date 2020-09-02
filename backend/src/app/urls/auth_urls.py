from django.urls import path

from app.api.signup import (
    signup,
)
from app.api.login import (
    login,
    logout,
)

urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('signup', signup),
]
