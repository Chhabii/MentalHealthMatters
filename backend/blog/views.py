from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import AddNewPost
from  django.shortcuts import redirect

# Create your views here.

@login_required(login_url='/account/login/')
def blog(request):
    post = BlogPost.objects.all()
    return render(request,'blog/blog.html',{'post':post})


@login_required(login_url='/account/login/')
def addnewpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = AddNewPost(request.POST)
            if fm.is_valid():
                bp = BlogPost()
                bp.author = request.user
                bp.title = fm.cleaned_data['title']
                bp.post = fm.cleaned_data['post']
                bp.published_date = fm.cleaned_data['published_date']
                bp.save()
                return redirect('/blog/')
        else:
            fm = AddNewPost()
        return render(request,'blog/addnewpost.html',{'form':fm})


@login_required(login_url='/account/login/')
def readmore(request,object_id):
    p = BlogPost.objects.get(id=object_id)
    return render(request,'blog/readmore.html',{'p':p})