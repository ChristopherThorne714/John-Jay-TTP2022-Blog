from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')
def contact(request):
    return render(request, 'blog_app/contact.html')
def about(request):
    return render(request, 'blog_app/about.html')