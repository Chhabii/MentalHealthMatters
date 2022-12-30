from django import forms
from django.core import validators
from .models import BlogPost
from django.utils import timezone
from ckeditor.fields import RichTextField

class AddNewPost(forms.ModelForm):
    published_date = forms.DateTimeField(disabled=True,initial=timezone.now)
    # post = RichTextField(attrs={'placeholder':'  title','class':'inoutfield'})

    class Meta:
        model = BlogPost
        fields = ['title','abstract','post','published_date']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'  title','class':'inoutfield'}),
            'abstract':forms.TextInput(attrs={'placeholder':'  title','class':'inoutfield'}),

        }