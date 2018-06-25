from datetime import datetime
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from SSO.models import User
from myblog.models import Article

# Create your views here.
from django.urls import reverse

# 获取作者基本信息
def getUserInfo(username):
    user = User.objects.get(username=username)
    blogs = Article.objects.filter(author=username)
    result = {}
    result['user'] = user
    result['blogs'] = blogs
    result['articleNum'] = len(blogs)
    result['words'] = sum(map(int, [i.wordcount for i in blogs]))
    return result

# 重定向到我的blog
def myblog_redirect(request):
    return HttpResponseRedirect(
        reverse('myblog')
    )

# 进入到我的blog页面
def myblog(request):
    username = request.session.get('username', None)
    result = getUserInfo(username)
    return render(request, 'myblog/myblog.html', result)

# 进入他人blog
def otherblog(request, username):
    result = getUserInfo(username)
    return render(request, 'myblog/myblog.html', result)

# 跳转到写blog页面
def writeblog(request):
    username = request.session.get('username', None)
    if username:
        return render(request, 'myblog/writeblog.html')
    else:
        return HttpResponseRedirect('/sso/login')

# 提交blog
def write(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    author = request.session.get('username', None)
    content = request.POST.get('content')
    wordcount = request.POST.get('words')
    updatetime = datetime.now()

    username = request.session.get('username', None)
    user = User.objects.get(username=username)
    if id:
        article = Article.objects.get(id=id)
    else:
        article = Article()
        article.createtime = datetime.now()
        article.user = user

    article.title = title
    article.desc = desc
    article.author = author
    article.content = content
    article.wordcount = wordcount
    article.updatetime = updatetime

    result = {}
    try:
        article.save()
        result['status'] = 200
    except Exception:
        result['status'] = 500

    return HttpResponse(json.dumps(result), content_type="application/json")

# blog详情页
def blogdetail(request, id):
    blog = Article.objects.get(id=id)
    result = getUserInfo(blog.author)
    result['blog'] = blog
    return render(request, 'myblog/blogdetail.html', result)