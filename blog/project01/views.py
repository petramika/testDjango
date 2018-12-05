from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
