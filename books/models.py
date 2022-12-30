from django.db import models
from django.contrib.auth import get_user_model



class Book(models.Model):
    
    name = models.CharField(max_length=200)
    page = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default='The Description Here...')
   

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

    def __str__(self) -> str:
        return self.title

    



