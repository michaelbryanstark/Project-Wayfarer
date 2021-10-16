from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [

 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('profile/', views.ProfileView.as_view(), name="profile"),



]