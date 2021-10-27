from django.urls import path
from .views import ProfileView, ProfileUpdate, Profile, EditProfileView, CreateProfileView, account_redirect
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name="home"),
 path('accounts/signup/', views.Signup.as_view(), name="signup"),
 path('<int:pk>/profile', views.ProfileView.as_view(), name="profile_view"),
 path('loggedin/', account_redirect, name="loggedin_view"),
 path('cities/', views.CityList.as_view(), name="city_list"),
 path('cities/posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
 path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
 path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
 path('posts/new/', views.PostCreate.as_view(), name="post_create"),
 path('cities/new/', views.CityCreate.as_view(), name="city_create"),
 path('<int:pk>/editprofile', views.EditProfileView.as_view(), name="edit_profile_view"),
 path('createprofile/', views.CreateProfileView.as_view(), name="create_profile_view"),
 path('posts/', views.posts_index, name='index'),
 path('posts/<int:review_id>/posts', views.posts_detail, name='detail'),
 path('posts/<int:pk>/edit', views.PostEdit.as_view(), name="post_edit"),
]