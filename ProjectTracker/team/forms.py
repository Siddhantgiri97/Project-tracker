from django import forms
from .models import Team


class TeamRegistration(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        labels = {
            'team_name': 'Team Name',
            'member1': 'Member 1',
            'member2': 'Member 2',
            'member3': 'Member 3',
            'member4': 'Member 4',
            'team_leader': 'Team Leader',

        }
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'member1': forms.Select(attrs={'class': 'form-control'}),
            'member2': forms.Select(attrs={'class': 'form-control'}),
            'member3': forms.Select(attrs={'class': 'form-control'}),
            'member4': forms.Select(attrs={'class': 'form-control'}),
            'team_leader': forms.Select(attrs={'class': 'form-control'}),
        }
