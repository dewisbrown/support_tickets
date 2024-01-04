"""
Defining urls for the entire project. API and tickets urls 
are further defined in their respective urls.py files.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),
    path('api/auth/', obtain_auth_token),
]
