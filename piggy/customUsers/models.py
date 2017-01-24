from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    school = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10)
