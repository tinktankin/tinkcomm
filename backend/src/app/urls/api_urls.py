"""
All Api URL Configuration
"""
from django.urls import path,include
from app.urls import company_urls
from app.urls import auth_urls
from app.urls import account_urls
from app.urls import subscriber_urls
from app.urls import group_urls
from app.urls import email_urls

urlpatterns = [
    path('companies/', include(company_urls)),
    path('auth/', include(auth_urls)),
    path('accounts/', include(account_urls)),
    path('subscribers/', include(subscriber_urls)),
    path('groups/', include(group_urls)),
    path('email/', include(email_urls)),
]
