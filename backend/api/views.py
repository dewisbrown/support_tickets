from rest_framework.decorators import api_view
from rest_framework.response import Response

from tickets.models import Ticket
from tickets.serializers import TicketSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    '''
    CSTS API View
    '''
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)
