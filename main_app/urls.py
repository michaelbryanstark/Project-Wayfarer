from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('profile/', views.Profile.as_view(), name="profile"),
 path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name="profile_edit"),
 path('cities/', views.CityList.as_view(), name="city_list"),
 path('cities/posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
 path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
 path('post/<int:pk>/edit/', views.PostEdit.as_view(), name="post_edit"),
 
]