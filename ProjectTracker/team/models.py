from django.db import models
from student.models import Student

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    member1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="member1")
    member2 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="member2", blank=True, null=True)
    member3 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="member3", blank=True, null=True)
    member4 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="member4", blank=True, null=True)
    team_leader = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="leader")

    def __str__(self):
        return self.team_name
