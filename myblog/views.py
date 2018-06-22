from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def myblog_redirect(request):
    return HttpResponseRedirect(
        reverse('myblog')
    )

def myblog(request):
    return render(request, 'myblog/myblog.html')

def writeblog(request):
    username = request.session.get('username', None)
    if username:
        return render(request, 'myblog/writeblog.html')
    else:
        return render(request, 'SSO/login.html')