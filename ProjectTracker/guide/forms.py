from django import forms
from .models import Guide


class GuideRegistration(forms.ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'
        labels = {
            'guide_name': 'Guide Name',
            'guide_department': 'Department',
            'guide_email': 'Email',
            'guide_mobile': 'Contact',
            'guide_specilization': 'Specilization',

        }
        widgets = {
            'guide_name': forms.TextInput(attrs={'class': 'form-control'}),
            'guide_department': forms.Select(attrs={'class': 'form-control'}),
            'guide_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'guide_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'guide_specilization': forms.Select(attrs={'class': 'form-control'}),
        }
