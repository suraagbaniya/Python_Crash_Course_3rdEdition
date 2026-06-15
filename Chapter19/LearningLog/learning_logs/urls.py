""" Defines URL patterns for learning_logs. """

#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #Home page
    # path(route = "", view = views.index, name = "index"),
    # path(route = "topics/", view = views.topics, name= 'topics'),
    # path(route= "topics/(?P<topic_id>\d+)/", view= views.topic, name= 'topic'),
   
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    
    
    #page for adding a new topic
    #path(route='new_topic/', view= views.new_topic, name= 'new_topic'),
    
    path("new_topic/", views.new_topic, name="new_topic"),
    
    
    #page for adding a new entry
    #path(route = 'new_entry/(?P<topic_id>\d+)/', view = views.new_entry, name = 'new_entry'),
    
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    
    #Page for editing an entry
    # path(route = 'edit_entry/(?P<entry_id>\d+)/', view = views.edit_entry, name = 'edit_entry'),
    
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    
]