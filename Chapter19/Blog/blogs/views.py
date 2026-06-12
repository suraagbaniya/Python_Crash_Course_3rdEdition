from django.shortcuts import render

# Create your views here.

def index(request):
    """ The home page for Blogs """
    return render(request=request, template_name='blogs/index.html')