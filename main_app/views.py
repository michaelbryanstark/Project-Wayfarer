from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, City, Profile
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = "profile.html"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, 'registration/signup.html', context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/profile/')
        else:
            context = {'form': form}
            return render(request, 'registration/signup.html', context)

        
class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        context["posts"] = Post.objects.all()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
    
class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"


class PostEdit(UpdateView):
    model = Post 
    fields = ['title', 'image','text', 'city']
    template_name = "post_edit.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
class ProfileEdit(UpdateView):
    model = Profile
    fields = ['image', 'current_city']
    template_name ='profile_edit.html'
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})