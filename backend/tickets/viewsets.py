from rest_framework import viewsets, mixins

from .models import Ticket
from .serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    get -> list -> QuerySet
    get -> retrieve -> Ticket Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'pk' # default


class TicketGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    """
    get -> list -> QuerySet
    get -> retrieve -> Ticket Instance Detail View
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'pk' # default
