from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('Hello,I am Takahiro Fujii.This is my site!')

