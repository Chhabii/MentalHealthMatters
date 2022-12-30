from django.urls import path 
from . import views
urlpatterns = [
    path('',views.chat_groups,name='chatgroups'),
    path("<str:group_name>/",views.chat,name='chat'),
]