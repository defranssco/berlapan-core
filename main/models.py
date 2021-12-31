#models.py
from django.db import models
 
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True)
    nik = models.IntegerField(blank=True)
    
    def __str__(self):  # biar jadi profile: atha
        return self.user.username
   