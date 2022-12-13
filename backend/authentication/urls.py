from django.urls import path 
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.log_out,name='logout'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('blog/',views.blog,name='blog')
    # path('forgot-password/', auth_views.PasswordResetView.as_view(), name='forgot_password'),
]