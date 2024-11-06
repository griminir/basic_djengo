from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Are like controllers in MVC


def index(request):
    return HttpResponse('Hello, World!')
