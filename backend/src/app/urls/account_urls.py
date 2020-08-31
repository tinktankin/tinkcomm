from django.urls import path

from app.api import account

urlpatterns = [
    path('', account.account_list),
    path('<int:pk>', account.get_account),
]

