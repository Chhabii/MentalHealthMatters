from django.shortcuts import render
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .forms import AddNewPost
from  django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.db.models import Q



# Create your views here.

@login_required(login_url='/account/login/')
def blog(request):
    post = BlogPost.objects.all()
    admin = True
    if request.user.is_staff:
        return render(request,'blog/blog.html',{'post':post,'admin':admin})
    else:    
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
                bp.abstract = fm.cleaned_data['abstract']
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


def search(request):
    query=None
    results=[]
    if request.method=="GET":
        query=request.GET.get('search')
        results=BlogPost.objects.filter(Q(title__icontains=query) | Q(abstract__icontains=query))
    return  render(request,'blog/search.html',{'query': query,
                                          'results': results})

@login_required(login_url='/account/login/')
def delete_post(request,object_id):
    if request.method == "POST":
        p = BlogPost.objects.get(id=object_id)
        p.delete()
        return redirect('/blog/')

        
@login_required(login_url='/account/login/')
def update_post(request,object_id):
    if request.method == "POST":
        bp = BlogPost.objects.get(id=object_id)
        fm = AddNewPost(request.POST,instance=bp)
        if fm.is_valid():
            fm.save()
            return redirect('/blog/')
    else:
        bp = BlogPost.objects.get(id=object_id)
        fm = AddNewPost(instance=bp)
    
    return render(request,'blog/updatepost.html',{'form':fm})

@login_required(login_url='/account/login/')
def add_favorite(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.user.is_authenticated:
        if request.user in post.user_favorite.all():
            post.user_favorite.remove(request.user)
        else:
            post.user_favorite.add(request.user)
    return HttpResponseRedirect(reverse('readmore',args=[str(pk)]))
    
