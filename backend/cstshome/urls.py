"""
Defining urls for the entire project. API and tickets urls 
are further defined in their respective urls.py files.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tickets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
