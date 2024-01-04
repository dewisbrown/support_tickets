"""
Class-based views allow the response to different HTTP request methods
with different class instance methods, instead of conditionally branching code 
inside a single view function.
"""
from .models import Ticket
from .serializers import TicketSerializer, UserSerializer
from .mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    """
    Function-based view for api home endpoint.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tickets': reverse('ticket-list', request=request, format=format),
    })


class TicketListView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    """
    API View for creating Ticket or listing all Ticket objects.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Overriden perform_create to create ticket with an owner.
        """
        serializer.save(owner=self.request.user)


    # def get_queryset(self, *args, **kwargs):
    #     """
    #     Allows filtering tickets, returns all tickets if no params.
    #     """
    #     # Filter by resolved attribute
    #     resolved = self.request.query_params.get('resolved', None)
    #     if resolved:
    #         qs = Ticket.objects.filter(resolved=resolved)
    #         return qs

    #     # Filter by user_id
    #     user_id = self.request.query_params.get('user_id', None)
    #     if user_id:
    #         qs = Ticket.objects.filter(owner=user_id)
    #         return qs

    #     return super().get_queryset(*args, **kwargs)


class TicketDetailView(
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView):
    """
    API View for retrieving, deleting, or updating 
    a single Ticket object.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UserListView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    """
    User view to handle 'GET' request for collection of users,
    and 'POST' requests for creating a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView):
    """
    User view to handle 'GET' requests for a single user instance,
    'PUT' requests to update User info, and
    'DELETE' requests to delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
