from django.urls import path
from . import views

app_name = 'blog'

#added second urls so that the app can handle url requests without calling to the main project urls.
urlpatterns = [
    path('', views.home, name='home'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),
    path('about/', views.about, name='about'),
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]