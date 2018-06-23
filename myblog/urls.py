from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.myblog_redirect),
    path('myblog', views.myblog, name='myblog'),
    path('writeblog', views.writeblog, name='writeblog'),
    path('write', views.write, name='write'),
]