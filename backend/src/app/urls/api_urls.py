"""
All Api URL Configuration
"""
from django.urls import path,include
from app.urls import company_urls
from app.urls import auth_urls
from app.urls import account_urls

urlpatterns = [
    path('companies/', include(company_urls)),
    path('auth/', include(auth_urls)),
    path('accounts/', include(account_urls)),
]
