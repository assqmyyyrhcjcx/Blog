from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index_redirect(request):
    return HttpResponseRedirect(
        reverse('index')
    )

def index(request):
    return render(request, 'content.html')
