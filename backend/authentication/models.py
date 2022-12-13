from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField()
    published_date=models.DateTimeField(default=timezone.now)