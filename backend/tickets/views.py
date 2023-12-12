"""
Class-based views allow the response to different HTTP request methods
with different class instance methods, instead of conditionally branching code 
inside a single view function.
"""
from rest_framework import generics

from .models import Ticket
from .serializers import TicketSerializer


class TicketListCreateAPIView(generics.ListCreateAPIView):
    """
    View for listing a queryset or creating a model instance.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        author = serializer.validated_data.get('author')
        pub_date = serializer.validated_data.get('pub_date')
        content = serializer.validated_data.get('content')

        serializer.save(author=author, pub_date=pub_date, content=content)

ticket_list_create_view = TicketListCreateAPIView.as_view()

class TicketDetailAPIView(generics.RetrieveAPIView):
    """
    View for retrieving a model instance.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

ticket_detail_as_view = TicketDetailAPIView.as_view()
