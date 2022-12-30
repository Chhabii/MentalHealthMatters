from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Chat, Group

# Create your views here.

@login_required(login_url='/account/login/')
def chat_groups(request):
    group = Group.objects.all()
    return render(request,'chat/chat_groups.html',{'group':group})

@login_required(login_url='/account/login/')
def chat(request,group_name):
    group = Group.objects.filter(name=group_name).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group(name=group_name)
        group.save()
    return render(request,'chat/chat.html',{'group_name':group_name,'chats':chats})