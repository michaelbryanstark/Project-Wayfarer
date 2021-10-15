from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.Model):
#     city = models.CharField(max_length=100)
#     img = models.CharField(max_length=250, default=None)
#     description = models.TextField(max_length=1000)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    past_cities = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pic = models.ImageField(upload_to="main_app/static/images", null=True)

    def __str__(self):
        return self.name
  
 