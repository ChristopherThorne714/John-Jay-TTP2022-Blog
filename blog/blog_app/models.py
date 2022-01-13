from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog_app/images/')
    
    def __str__(self):
        return self.title