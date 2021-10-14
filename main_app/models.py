from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    city = models.CharField(max_length=100)
    img = models.CharField(max_length=250, default=None)
    description = models.TextField(max_length=1000)
    
  
 