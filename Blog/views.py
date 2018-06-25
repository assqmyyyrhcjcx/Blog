from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from SSO.models import User
from myblog.models import Article

# 重定向到首页
def index_redirect(request):
    return HttpResponseRedirect(
        reverse('index')
    )

# 展示首页
def index(request):
    # 获取推荐作者
    result = {}
    result['users'] = recommendAuthor(request)

    # 获取推荐文章
    username = request.session.get('username', None)
    blogs = Article.objects.exclude(author=username)
    result['blogs'] = blogs
    return render(request, 'content.html', result)

# 查找除了自己以外的其他用户
def recommendAuthor(request):
    username = request.session.get('username', None)
    if username:
        users = User.objects.exclude(username__contains=username)
    else:
        users = User.objects.all()
    return users