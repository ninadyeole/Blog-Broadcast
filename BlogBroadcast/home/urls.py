from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView, name='Home'),
    path('contact', views.ContactView, name='Contact'),
    path('profile', views.profileView, name='profile'),
    path('editProfile', views.editProfileView, name='editProfile'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('search', views.search, name='search'),
    path('blogTutorial', views.blogTutorial, name='blogTutorial'),
    path('addBlog', views.addBlog, name='addBlog'),
    path('saveBlog', views.saveBlog, name='saveBlog'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handlelogin'),
    path('logout', views.handleLogout, name='handlelogout'),
]