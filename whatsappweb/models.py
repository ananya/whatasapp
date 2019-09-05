from django.db import models
from django.conf import settings
from django.utils import timezone


class Message(models.Model):
    text = models.TextField()
    recepient_no = models.TextField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def publish_msg(self):   
        self.save()

    def __str__(self):
        return self.text

class Employe(models.Model):
    name = models.TextField()
    designation = models.TextField()
    phone_no = models.TextField()
    # to be changed
    # image = models.TextField() 

    def employe_add_to_db(self):   
        self.save()

    def __str__(self):
        return self.name

class Company(models.Model):
    all_employes = models.ForeignKey(Employe, related_name = 'employes', on_delete = models.CASCADE)