from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamRegistration

# Create your views here.


def team_list(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'team/team.html', context)


def add_team(request):
    if request.method == 'POST':
        form = TeamRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('team:team_list')
    else:
        form = TeamRegistration()
    context = {'form': form}
    return render(request, "team/add_team.html", context)


def update_team(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == 'POST':
        form = TeamRegistration(request.POST, instance=team)
        if form.is_valid():
            form.save()
        return redirect('team:team_list')
    else:
        form = TeamRegistration(instance=team)
    context = {'form': form}
    return render(request, "team/update_team.html", context)
