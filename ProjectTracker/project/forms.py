from django import forms
from .models import Project


class ProjectRegistration(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'project_title': 'Project Title',
            'project_desc': 'Project Description',
            'project_guide': 'Project Guide',
            'team_name': 'Team Name',

        }
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            'project_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'project_guide': forms.Select(attrs={'class': 'form-control'}),
            'team_name': forms.Select(attrs={'class': 'form-control'}),
        }
