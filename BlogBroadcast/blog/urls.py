from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    #Path to Home page of Blog app
    path('', views.blogHomeView, name='blogHome'),
    #API to post a comment
    path('postComment', views.postComment, name='postComment'),
    #Path to All of User's Blogs
    path('yourBlogs', views.yourBlogs, name='yourBlogs'),
    #Path to All of User's Comments
    path('yourComments', views.yourComments, name='yourComments'),
    
    #Path to a certain Blog. Make sure to keep this in the last
    path('<str:slug>', views.blogView, name='blog'),

]