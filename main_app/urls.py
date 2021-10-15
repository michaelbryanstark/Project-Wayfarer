from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('accounts/profile', views.Profile.as_view(), name="profile"),
    path('profile/', views.profile, name='profile'),
    path('profile/add_profile/', views.add_profile, name='add_profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
]