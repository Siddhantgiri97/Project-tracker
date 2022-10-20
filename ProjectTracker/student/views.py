from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentRegistration
# Create your views here.


def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, "student/student.html", context)


def add_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student:student')
    else:
        form = StudentRegistration()
    context = {'form': form}
    return render(request, "student/add_student.html", context)



def update_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentRegistration(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('student:student_list')
    else:
        form = StudentRegistration(instance=student)
    context = {'form': form}
    return render(request, "student/update_student.html", context)
