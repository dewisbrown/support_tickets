"""
Defining urls for tickets endpoints:
    - 'api/tickets/': retrieves list of all tickets
    - 'api/tickets/<int:pk>/': retrieves single ticket given the primary key
"""
from django.urls import path

from tickets import views


urlpatterns = [
    path('', views.api_root),
    path('tickets/', views.TicketListView.as_view(),
         name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(),
         name='ticket-detail'),
    path('users/', views.UserListView.as_view(),
         name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(),
         name='user-detail'),
    # path('tickets-by-user/<int:pk>/', views.TicketsByUserView.as_view(),
    #    name='tickets-by-user'),
]
