from django.urls import path

from app.api.group import group_list, group_detail

urlpatterns = [
    path('', group_list),
    path('<int:pk>', group_detail),
]