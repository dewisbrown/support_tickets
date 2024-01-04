"""
Class-based views allow the response to different HTTP request methods
with different class instance methods, instead of conditionally branching code 
inside a single view function.
"""
from .models import Ticket
from .serializers import TicketSerializer, UserSerializer
from .mixins import StaffEditorPermissionMixin
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, status
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
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    """
    API View for creating Ticket or listing all Ticket objects. 
    Staff, Admin, and Ticket owners have access. Anonymous Users 
    cannot view data.
    """
    serializer_class = TicketSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Overriden perform_create to create ticket with an owner.
        """
        serializer.save(owner=self.request.user)


    def get_queryset(self, *args, **kwargs):
        """
        Overriden to allow filtering by user if user is not staff.
        """
        owner_field = 'owner'
        user = self.request.user

        # anonymous user sees empty list
        if not user.is_authenticated:
            return Ticket.objects.none()

        # staff can view all tickets
        if self.request.user.is_staff:
            return Ticket.objects.all()

        # filter by user if user is not staff
        lookup_data = {}
        lookup_data[owner_field] = self.request.user
        return Ticket.objects.filter(**lookup_data)


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
