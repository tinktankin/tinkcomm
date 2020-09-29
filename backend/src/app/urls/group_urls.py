from django.urls import path

from app.api.group import (
    group_list,
    group_detail,
    group_bulk_delete
)

urlpatterns = [
    path('', group_list),
    path('<int:pk>', group_detail),
    path('bulk_delete', group_bulk_delete),
]