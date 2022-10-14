from django.shortcuts import render
from .models import Team
# Create your views here.
def team_list(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request,'team/team.html',context)