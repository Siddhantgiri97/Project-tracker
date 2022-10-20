from django.shortcuts import render
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
        return redirect('team:team')
    else:
        form = TeamRegistration()
    context = {'form': form}
    return render(request, "team/add_team.html", context)
