# myapp/models.py
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
