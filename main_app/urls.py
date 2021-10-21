from django.urls import path
from .views import ProfileView, ProfileUpdate, Profile, EditProfileView
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('accounts/editprofile/', views.ProfileUpdate.as_view(), name="profile_update"),
 path('<int:pk>/profile', views.ProfileView.as_view(), name="profile_view"),
 path('cities/', views.CityList.as_view(), name="city_list"),
 path('cities/posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
 path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
 path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
 path('posts/new/', views.PostCreate.as_view(), name="post_create"),
 path('cities/new/', views.CityCreate.as_view(), name="city_create"),
 path('<int:pk>/editprofile', views.EditProfileView.as_view(), name="edit_profile_view"),
]