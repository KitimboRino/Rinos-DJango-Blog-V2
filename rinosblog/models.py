from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)

    # Deletes all the admins blog posts in cace the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    # Allows us to see the title of the blog post and author on admin page
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
    