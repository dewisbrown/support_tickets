"""
Allows complex data to be converted to Python datatypes,
which can then be rendered into JSON, XML, etc.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ticket


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Ticket
        fields = [
            'url',
            'id',
            'owner',
            'content',
            'resolved',
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(many=True, view_name='ticket-detail', read_only=True)

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'tickets',
        ]
