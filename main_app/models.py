from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=50)
  img = models.CharField(max_length=250)
  current_city=models.CharField(max_length=100)
  date_joined=models.DateField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  