from django.shortcuts import render

from .models import Project

def index(request):
    return render(request, 'index.html')

from django.views import generic

class ProjectsListView(generic.ListView):
    model = Project
    paginate_by = 10

class ProjectDetailView(generic.DetailView):
    model = Project

def connect(request):
    return render(request, 'connect.html')