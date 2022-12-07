from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'authentication/signup.html',{'form':fm})