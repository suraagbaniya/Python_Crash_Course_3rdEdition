""" A urlpattern to manage all urls in 'meal_plans' app. """

from django.urls import path, include

from . import views

urlpatterns = [
    #Homepage
    path('', view= views.index, name= 'index'),
]