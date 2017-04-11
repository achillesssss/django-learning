from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)   
    snder = models.ForeignKey(User, related_name='sender')


    def __str__(self):
        return self.content