"""
Defining urls for the entire project. API and tickets urls 
are further defined in their respective urls.py files.
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/tickets/', include('tickets.urls')),
]
