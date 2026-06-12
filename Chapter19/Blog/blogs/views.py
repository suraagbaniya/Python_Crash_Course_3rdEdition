from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import PostForm

# Create your views here.

def index(request):
    """ The home page for Blogs """
    return render(request=request, template_name='blogs/index.html')

def posts(request):
    """ The posts page for Blogs """
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request=request, template_name='blogs/posts.html', context= context)

def new_post(request):
    """Add a new post"""
    if request.method != 'POST':
        # No data submitted; create a blank post.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    
    context = {'form': form}
    return render(request= request,template_name = 'blogs/new_post.html', context= context,)

            