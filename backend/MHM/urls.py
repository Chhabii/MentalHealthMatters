
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("pages.urls")),
    path("account/",include("authentication.urls")),
    path('blog/',include("blog.urls")),
    path('community/',include("chat.urls")),


]
