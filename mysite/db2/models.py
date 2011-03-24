from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=60)
    session = models.CharField(max_length=60)
