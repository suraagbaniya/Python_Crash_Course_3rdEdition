"""Defines URLpattern for all pizzas app urls"""

from django.urls import path, include

from . import views

urlpatterns = [
    #Home page
    path('',view= views.index, name= 'index')
]