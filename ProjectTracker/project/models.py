from django.db import models
from guide.models import Guide
from team.models import Team

# Create your models here.


class Project(models.Model):
    project_title = models.CharField(max_length=300)
    project_desc = models.TextField(max_length=1000)
    project_guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team_name}--{self.project_title}'
