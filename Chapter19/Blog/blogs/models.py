from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """ This is a BlogPost model """
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
