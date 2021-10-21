from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post, City, Profile, User
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
class EditProfileView(UpdateView):
    model = Profile
    fields = ['name', 'image', 'current_city']
    template_name = 'editprofile.html'
    success_url = '/'

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
        
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    def get(self, request):
        form = UserChangeForm()
        context = {"form": form}
        return render(request, 'registration/profile_update.html', context)
    def get_object(self):
        return self.request.user 
        
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
    
class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    success_url = '/cities/'
    
class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"
    
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'image', 'text', 'author', 'city' ]
    template_name = "post_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)
    
    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
class CityCreate(CreateView):
    model = City
    fields = ['name', 'image']
    template_name = "city_create.html"
    success_url = "/cities/"
    
    