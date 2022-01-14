from django.db import models

# Create your models here.
#setting what data fields the admin page will ask for when adding a blog post
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog_app/images/')
    
    def __str__(self):
        return self.title