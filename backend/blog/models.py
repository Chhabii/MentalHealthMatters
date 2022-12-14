from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # post = models.TextField()
    abstract = models.TextField(default='Write the abstract for your blog')
    post = RichTextField()

    published_date=models.DateTimeField(default=timezone.now)