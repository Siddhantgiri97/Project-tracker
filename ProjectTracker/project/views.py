from django.shortcuts import render
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
        return redirect('project:project')
    else:
        form = ProjectRegistration()
    context = {'form': form}
    return render(request, "project/add_project.html", context)
