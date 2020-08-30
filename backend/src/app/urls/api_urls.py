"""
All Api URL Configuration
"""
from django.urls import path,include
from app.urls import company_urls
from app.urls import auth_urls
from app.urls import account_urls
from app.urls import subscriber_urls
from app.urls import group_urls

urlpatterns = [
    path('company/', include(company_urls)),
    path('auth/', include(auth_urls)),
    path('account/', include(account_urls)),
    path('subscriber', include(subscriber_urls)),
    path('group', include(group_urls)),

]
