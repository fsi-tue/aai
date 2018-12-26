from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request):
    return HttpResponse("Hello, world. This is the detail page.")


def allentries(request):
    return HttpResponse("Hello, world. This page will show all entries.")
