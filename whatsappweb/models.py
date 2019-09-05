from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
    text = models.TextField()
    recepient_no = models.TextField()
    resolved = models.BooleanField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text

class Company(models.Model):
    user_name = models.TextField()
    designation = models.TextField()
    phone_no = models.TextField()
    introduction = models.TextField()
    # to be changed
    image = models.TextField() 
