"""
Class-based views allow the response to different HTTP request methods
with different class instance methods, instead of conditionally branching code 
inside a single view function.
"""
from tickets.models import Ticket
from tickets.serializers import TicketSerializer, UserSerializer
from tickets.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tickets': reverse('ticket-list', request=request, format=format)
    })


class TicketListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]


# class TicketsByUserView(generics.ListAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [
#         permissions.IsAdminUser,
#         IsOwnerOrReadOnly
#     ]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]
