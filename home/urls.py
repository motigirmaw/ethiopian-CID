from django.conf.urls import url
from django.contrib import admin
from . import views

app_name ='home'
urlpatterns = [
    url(r'^$', views.home, name= "home"),
    url(r'^home/identfay/$', views.identfay),
    url(r'^home/medical/$', views.medical, name= "medical"),
    url(r'^age_cal/$', views.age_cal, name= "age_cal"),
    url(r'^home/register/$', views.register),
    url(r'^homeaddFace/$', views.addFace),
    url(r'^home/welcome/(?P<face_id>\d+)/$', views.welcome)
]
