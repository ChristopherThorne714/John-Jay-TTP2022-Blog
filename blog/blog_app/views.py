from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
#defining what's being rendered based on requests by the browser
def home(request):
    return render(request, 'blog_app/home.html')
def about(request):
    return render(request, 'blog_app/about.html')

#Setting up the all_blogs page to automatically get and sort the blogs on one page from a database
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_app/all_blogs.html', {'blogs': blogs})

#setting up the page for each blog post to display when a blog_id is requested
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_app/detail.html', {'blog': blog})