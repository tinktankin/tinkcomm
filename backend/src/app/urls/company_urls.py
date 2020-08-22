from django.urls import path

from app.api.company import (
    get_company,
    get_all_company,
)

urlpatterns = [
    path('', get_all_company),
    path('<int:pk>', get_company),
]
