from django.urls import path

from app.api.account import (
    get_account,
    get_all_account,
    signup_account,
    update_account,
    delete_account
)

urlpatterns = [
    path('', get_all_account),
    path('<int:pk>', get_account),
    path('signup', signup_account),
    path('update', update_account),
    path('delete', delete_account)
]

