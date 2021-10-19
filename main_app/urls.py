from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('profile/', views.Profile1.as_view(), name="profile"),
 path('cities/', views.CityList.as_view(), name="city_list"),
 path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile_update"),
]