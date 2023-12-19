"""
Database model for a Ticket object.
Attributes:
    - owner: user that submitted ticket
    - pub_date: date ticket was created
    - content: info about ticket
    - resolved: boolean that staff can set when ticket is resolved
"""
from django.db import models


class Ticket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
