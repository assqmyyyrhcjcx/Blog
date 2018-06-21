from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index_redirect(request):
    return HttpResponseRedirect(
        reverse('nav')
    )

def index(request):
    return render(request, 'nav.html')
