from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def projects(request):
    return HttpResponse("Hello, world. You're at the projects index.")