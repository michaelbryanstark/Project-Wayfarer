from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
  name = forms.CharField(max_length=100)
  current_city = forms.CharField(max_length=100)
  
  class Meta:
    model = Profile
    fields = ["name", "current_city"]

class PostForm(forms.ModelForm):
  title = forms.CharField(max_length=200, required=True)
  text = forms.CharField(required=True, label="Text", widget=forms.Textarea())
  
  class Meta:
    model = Post
    fields = ["title", "text"]