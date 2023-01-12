
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("pages.urls")),
    path("account/",include("authentication.urls")),
    path('blog/',include("blog.urls")),

    
]
# Serving the media files in development mode. Change debug=false during production.
#This is to show profile picture in the media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
