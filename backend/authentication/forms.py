from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'  Password','class':'inoutfield'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'  Confirm Password','class':'inoutfield'}))

    class Meta:
        model  = CustomUser
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'  Username','class':'inoutfield'}),
            'first_name' : forms.TextInput(attrs={'placeholder':'  Firstname','class':'inoutfield'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'  Lastname','class':'inoutfield'}),
            'email' : forms.TextInput(attrs={'placeholder':'  Email','class':'inoutfield'}),
            # 'user_type' : forms.MultipleChoiceField(widget=forms.RadioSelect,choices= CustomUser.user_type)
            # 'password' : forms.TextInput(attrs={'placeholder':'Password','class':'inoutfield'}),

            
            
        }
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder':'  Username','autofocus':True,'class':'inoutfield'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder':'  Password',"autofocus": True,'class':'inoutfield'})
    )

class ChangePassForm(PasswordChangeForm):
        old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder':'  Old Password',"autocomplete": "current-password", "autofocus": True,'class':'inoutfield'}
        ),
        )
        new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder':'  New Password',"autocomplete": "new-password", "autofocus": True,'class':'inoutfield'}
        ),
        )
        new_password2 = forms.CharField(
        label=_("Confirm password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder':'  Confirm Password',"autocomplete": "new-password", "autofocus": True,'class':'inoutfield'}
        ),
        )

