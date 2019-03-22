from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def connect(request):
    return render(request, 'connect.html')