"""
Urls for api/ are defined here.
"""
from django.urls import path

from . import views


urlpatterns = [
    path('', views.api_home),
]
