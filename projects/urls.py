from django.urls import path

from . import views

from django.conf.urls import include

urlpatterns = [
     path('', views.index, name='index'),
     path('projects/', views.ProjectsListView.as_view(), name='projects'),
     path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
     path('connect/', views.connect, name='connect'),
]
