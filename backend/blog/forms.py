from django import forms
from django.core import validators
from .models import BlogPost
from django.utils import timezone

class AddNewPost(forms.ModelForm):
    published_date = forms.DateTimeField(disabled=True,initial=timezone.now)
    class Meta:
        model = BlogPost
        fields = ['title','abstract','post','published_date']
        