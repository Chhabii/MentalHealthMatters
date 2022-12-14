from django.urls import path 
from . import views
urlpatterns = [
    path('',views.blog,name='blog'),
    path('addnewpost/',views.addnewpost,name='addnewpost'),
    path('readmore/<int:object_id>',views.readmore,name='readmore'),

]