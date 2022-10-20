from django import forms
from .models import Student


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'gr_no': 'Registration No',
            'student_name': 'Name',
            'student_div': 'Division',
            'student_branch': 'Branch',
            'student_roll': 'Roll No',
            'student_email': 'Email',
            'student_mobile': 'Contact',

        }
        widgets = {
            'gr_no': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_div': forms.Select(attrs={'class': 'form-control'}),
            'student_branch': forms.Select(attrs={'class': 'form-control'}),
            'student_roll': forms.TextInput(attrs={'class': 'form-control'}),
            'student_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'student_mobile': forms.TextInput(attrs={'class': 'form-control'}),
        }
