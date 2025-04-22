from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default='Unknown')
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)