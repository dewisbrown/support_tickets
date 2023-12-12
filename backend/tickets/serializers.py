"""
Allows complex data to be converted to Python datatypes,
which can then be rendered into JSON, XML, etc.
"""
from rest_framework import serializers

from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'author',
            'pub_date',
            'content',
            'resolved',
        ]
