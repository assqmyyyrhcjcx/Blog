from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from SSO.models import User


def index_redirect(request):
    return HttpResponseRedirect(
        reverse('index')
    )

def index(request):
    authors = {}
    authors['users'] = recommendAuthor(request)
    return render(request, 'content.html', authors)

# 查找除了自己以外的其他用户
def recommendAuthor(request):
    username = request.session.get('username', None)
    if username:
        users = User.objects.exclude(username__contains=username)
    else:
        users = User.objects.all()
    return users