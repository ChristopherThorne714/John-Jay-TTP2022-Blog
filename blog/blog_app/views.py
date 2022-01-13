from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.

def base(request):
    return render(request, 'blog_app/base.html')
def contact(request):
    return render(request, 'blog_app/contact.html')
def about(request):
    return render(request, 'blog_app/about.html')

def all_blogs(request):
    #blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog_app/all_blogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_app/detail.html', {'blog': blog})