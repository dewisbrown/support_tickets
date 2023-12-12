"""
Defining urls for tickets endpoints:
    - 'api/tickets/': retrieves list of all tickets
    - 'api/tickets/<int:pk>/': retrieves single ticket given the primary key
"""
from django.urls import path

from . import views

# api/tickets/
urlpatterns = [
    path('', views.ticket_list_create_view),
    path('<int:pk>/', views.ticket_detail_as_view),
]
