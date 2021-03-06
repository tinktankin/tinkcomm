from django.urls import path

from app.api.subscriber import (
    subscriber_list,
    subscriber_detail,
    subscriber_upload,
    subscriber_bulk_delete
)

urlpatterns = [
    path('', subscriber_list),
    path('<int:pk>', subscriber_detail),
    path('upload', subscriber_upload),
    path('bulk_delete', subscriber_bulk_delete),
]
