from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm,LoginForm,ChangePassForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,logout,update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from .models import BlogPost

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request,'Account Created Successfully!!')
                fm.save()
        else:
            fm = SignUpForm()
        return render(request,'authentication/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/dashboard')

@csrf_exempt
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/account/dashboard/')

                
        else: 
            fm = LoginForm()
        return render(request,'authentication/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/dashboard/')


def dashboard(request):
    if request.user.is_authenticated:
        
        return render(request,'authentication/dashboard.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/account/login/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = ChangePassForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password Changed Successfully!!')
                return HttpResponseRedirect('/account/dashboard/')
        else:
            fm = ChangePassForm(user=request.user)
        return render(request,'authentication/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/login/')

def blog(request):
    post = BlogPost.objects.all()
    return render(request,'authentication/blog.html',{'post':post})