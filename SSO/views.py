from django.contrib import auth
from django import forms
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import User

# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponseRedirect(
        reverse('login')
    )

def login(request):
    return render(request, 'SSO/login.html')

def register(request):
    return render(request, 'SSO/register.html')

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=11)

def loginAction(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user:
        request.session['username'] = username
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'SSO/login.html')

@csrf_exempt
def registerAction(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # 判断用户是否存在
            user = auth.authenticate(username=username,password=password)
            if user:
                context['userExit']=True
                return render(request, 'SSO/login.html', context)

            #添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password, email=email, phone=phone)
            user.save()

            #添加到session
            request.session['username'] = username
            #调用auth登录
            auth.login(request, user)
            #重定向到首页
            return redirect('/')
    else:
        context = {'isLogin':False}
    #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return render(request,'SSO/register.html',context)

def logoutAction(request):
    logout(request)
    return HttpResponseRedirect('/')