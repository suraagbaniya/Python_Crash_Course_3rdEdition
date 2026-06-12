"""Defines  URL patterns for Blogs App """

from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path(route='', view=views.index, name= 'index'),
    path(route='posts/',view= views.posts, name='posts'),
    path(route='new_posts/',view= views.new_post, name='new_post'),
    
]