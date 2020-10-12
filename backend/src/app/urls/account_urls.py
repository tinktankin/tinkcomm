from django.urls import path,include

from app.api.account import (
    account_list,
    account_detail,
    account_bulk_delete,
)

urlpatterns = [
   path('', account_list),
    path('<int:pk>', account_detail),
    path('bulk_delete', account_bulk_delete),
]