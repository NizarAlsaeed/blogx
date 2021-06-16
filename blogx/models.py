from django.db import models
from django.contrib.auth import  get_user_model
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
