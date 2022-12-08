from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'pw2'}))

    class Meta:
        model  = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'username'}),
            
        }