from django.urls import path

from app.api.account import (
    get_account,
    get_all_account,
)

urlpatterns = [
    path('', get_all_account),
    path('<int:pk>', get_account),
]
