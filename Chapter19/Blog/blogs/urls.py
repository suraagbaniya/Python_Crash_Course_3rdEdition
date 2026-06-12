"""Defines  URL patterns for Blogs App """

from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path(route='', view=views.index, name= 'index'),
]