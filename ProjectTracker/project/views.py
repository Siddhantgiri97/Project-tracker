from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectRegistration

# Create your views here.


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project/project.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('project:project_list')
    else:
        form = ProjectRegistration()
    context = {'form': form}
    return render(request, "project/add_project.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = ProjectRegistration(request.POST, instance=project)
        if form.is_valid():
            form.save()
        return redirect('project:project_list')
    else:
        form = ProjectRegistration(instance=project)
    context = {'form': form}
    return render(request, "project/update_project.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('project:project_list')
