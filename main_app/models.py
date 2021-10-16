from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=50)
  img = models.CharField(max_length=500)
  current_city=models.CharField(max_length=100)
  date_joined=models.DateField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  
class City(models.Model):
  name = models.CharField(max_length=75)
  image = models.CharField(max_length=500)
  
  def __str__(self):
    return self.name
  
  
class Post(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=500)
  text = models.TextField(max_length=500)
  date_created = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(Profile, on_delete=models.CASCADE)
  city = models.ForeignKey(City, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
  
  class Meta: 
    ordering = ['-date_created']
