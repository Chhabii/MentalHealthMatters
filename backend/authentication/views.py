from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm,LoginForm,ChangePassForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,logout,update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from blog.models import BlogPost

from .models import CustomUser, Student, Admin, Teacher


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
                    user_type = user.user_type
                    if user_type == '1':
                        messages.success(request,'Logged in as admin!!')
                    elif user_type == '2':
                        messages.success(request,'Logged in as Teacher!!')
                    elif user_type == '3':
                        messages.success(request,'Logged in as Student!!')
                    else:
                        messages.success(request,'logged in but no user_type')
                    

                    # messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/account/dashboard/')

                
        else: 
            fm = LoginForm()
        return render(request,'authentication/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/account/dashboard/')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        favorite_posts = BlogPost.objects.filter(user_favorite=user)
        return render(request,'authentication/dashboard.html',{'name':request.user,'post':favorite_posts})
    else:
        return HttpResponseRedirect('/account/login/')

def log_out(request):
    logout(request)
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

def profile(request):
    # if request.user.user_type == '1':
    #     user = Admin.object.get(id = request.user.id)
    # elif request.user.user_type == '2':
    #     user = Teacher.object.get(id = request.user.id)

    # elif request.user.user_type == '3':
    #     user = Student.object.get(id = request.user.id)

    # else:
    user = CustomUser.objects.get(id = request.user.id)

    context = {
        "user":user,
    }
    return render(request,'authentication/profile.html',context)

@csrf_exempt
def profileupdate(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    address = request.POST.get('address')
    # print(first_name,last_name,username)
    try:
        customuser = CustomUser.objects.get(id = request.user.id)
        # userr = customuser(
        #     first_name = first_name,
        #     last_name = last_name,
        #     username = username,
        #     email = email


        # )
        # userr.save()
 
        customuser.first_name = first_name
        customuser.last_name = last_name
        customuser.username = username
        customuser.email = email
        customuser.save()
        # print(request.user.user_type)
        if customuser.user_type == '1':
            print('hello')
            adminUser = Admin.object.get(id = request.user.id)

            adminUser.address = address

            adminUser.save()


        messages.success(request,'Profile Updated!!')
        # return HttpResponseRedirect('authentication/profile.html')
        return redirect('profile')
    except:
        messages.error(request,'Something went wrong. Try again!!')
        
    return render(request,'authentication/profile.html')
    