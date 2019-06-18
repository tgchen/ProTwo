from django.db import models

# Create your models here.
class User(models.Model):
    lastName = models.CharField(max_length=128)
    firstName = models.CharField(max_length=128)
    email = models.EmailField(max_length=245, unique=True)
    
