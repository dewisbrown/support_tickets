"""
Database model for a Ticket object.
Attributes:
    - author: user that submitted ticket
    - pub_date: date ticket was created
    - content: info about ticket
    - resolved: boolean that staff can set when ticket is resolved
"""
from django.db import models


class Ticket(models.Model):
    """
    Ticket object represents a customer support ticket.
    """
    author = models.CharField(max_length=20)
    pub_date = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    resolved = models.BooleanField(default=False)
