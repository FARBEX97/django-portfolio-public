from django.shortcuts import render
from django.views.generic import ListView
from .models import CodeProject

class ProjectListView(ListView):
    model = CodeProject
    template_name = 'projects/html/projects.html'