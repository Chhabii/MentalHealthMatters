from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # post = models.TextField()
    abstract = models.TextField()
    post = RichTextField()
    user_favorite = models.ManyToManyField(User,related_name='user_favorite',blank=True)
    published_date=models.DateTimeField(default=timezone.now)

    def total_favorite(self):
        return self.user_favorite.count()
