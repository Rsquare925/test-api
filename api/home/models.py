from django.db import models

# Create your models here.



class User1(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=90)
