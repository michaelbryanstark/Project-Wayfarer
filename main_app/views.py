from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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

class City:
    def __init__(self, image, name):
        self.image = image
        self.name = name
        
class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = cities
        context["posts"] = posts
        return context
    
cities = [
    City("https://cdn.shopify.com/s/files/1/2012/8501/products/80775098-b507-481e-bada-412f5600ae06_61e2bacb-72c2-451d-91ae-3d4783de5b81_256x256.jpg?v=1628179761","New York"),
    City("https://cdn.shopify.com/s/files/1/2012/8501/products/80775098-b507-481e-bada-412f5600ae06_61e2bacb-72c2-451d-91ae-3d4783de5b81_256x256.jpg?v=1628179761","Atlanta"),
]
       
class Post:
    def __init__(self, title, image, text, date_created, author, city):
        self.title = title
        self.image = image
        self.text = text
        self.date_created = date_created
        self.author = author #FK 
        self.city = city #FK

# class PostList(TemplateView):
#     template_name = "city_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["posts"] = posts
#         return context
    
posts = [
    Post("Welcome to New York","https://cdn.shopify.com/s/files/1/2012/8501/products/80775098-b507-481e-bada-412f5600ae06_61e2bacb-72c2-451d-91ae-3d4783de5b81_256x256.jpg?v=1628179761","This is a test post","1/1/2021","John Smith","New York"),
     Post("Welcome to New York","https://cdn.shopify.com/s/files/1/2012/8501/products/80775098-b507-481e-bada-412f5600ae06_61e2bacb-72c2-451d-91ae-3d4783de5b81_256x256.jpg?v=1628179761","This is a test post","1/1/2021","John Smith","New York"),
]