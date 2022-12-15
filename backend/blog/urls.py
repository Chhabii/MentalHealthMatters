from django.urls import path 
from . import views
urlpatterns = [
    path('',views.blog,name='blog'),
    path('addnewpost/',views.addnewpost,name='addnewpost'),
    path('readmore/<int:object_id>',views.readmore,name='readmore'),
    path('delete/<int:object_id>',views.delete_post,name='delete'),
    path('update/<int:object_id>/',views.update_post,name='update'),
]