from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('loginAction', views.loginAction, name='loginAction'),
    path('registerAction', views.registerAction, name='registerAction'),
]
