from django.shortcuts import render
from .models import Student

# Create your views here.

def student_list(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,"student/student.html",context)

