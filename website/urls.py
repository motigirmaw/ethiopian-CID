from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings, urls
from . import views, settings  
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('home.urls')),
   # url(r'^media/(?p<path>.*)$',serve{'document_root' : settings.MEDIA_ROOT}),
    #url(r'^static/(?p<path>.*)$',serve{'document_root' : settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
