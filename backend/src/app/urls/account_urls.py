from django.urls import path,include

from app.api.account import account_list, account_detail

urlpatterns = [
   path('', account_list),
    path('<int:pk>', account_detail),
]