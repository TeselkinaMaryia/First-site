from django.shortcuts import render
from .models import Project


def main(request):
    return render(request, 'portfolio/main.html')


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)
