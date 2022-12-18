from django.db import models
# from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField
# from backend.authentication.models import CustomUser
# User = get_user_model()
# Create your models here.
class BlogPost(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # post = models.TextField()
    abstract = models.TextField()
    post = RichTextField()

    published_date=models.DateTimeField(default=timezone.now)