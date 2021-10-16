from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')    
class ProfileView(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["profile"] = Profile.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["profile"] = Profile.objects.filter(user=self.request.user) 
            context["header"] = "Profile"
        return context
    
   
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
          
class ProfileForm(forms.ModelForm):
    model = Profile
    fields = [
        'name',
        'current_city',
        'past_cities'
    ]


# def profile(request):
#     # posts = Posts.objects.filter(author=request.user.id)
#     # profile = Profile.objects.get(user=request.user)
#     # comments = Comment.objects.filter(author=request.user.id)

#     context = {
#         'profile': profile,
#         # 'posts': posts,
#         # 'comments': comments,
#         # 'num_comments': len(comments),
#         # 'num_posts': len(posts)
#     }
#     return render(request, 'profiles/index.html', context)       

# def add_profile(request):
#     error_message = ''
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST)
#         if profile_form.is_valid():
#             new_profile = profile_form.save(commit=False)
#             new_profile.user_id = request.user.id
#             new_profile.save()
#             return redirect('profile')
#         else:
#             error_message = 'Something went wrong - try again'
#     else:
#         profile_form = ProfileForm()
#         context = {
#             'profile_form': profile_form, 
#             'error_message': error_message
#         }
#         return render(request, 'profiles/add.html', context)
    
# def update_profile(request):
#     error_message = ''
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if profile_form.is_valid():
#             updated_profile = profile_form.save()
#             return redirect('profile')
#         else:
#             error_message = 'Something went wrong - try again'
#     else:
#         profile_form = ProfileForm(instance=request.user.profile)
#         context = {
#             'profile_form': profile_form, 
#             'error_message': error_message
#         }
#         return render(request, 'profiles/edit.html', context)