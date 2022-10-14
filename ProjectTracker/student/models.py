from unicodedata import name
from django.db import models

# Create your models here.

DIV = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)

DEPARTMENT = (
    ("CS", "CS"),
    ("IT", "IT"),
    ("ENTC", "ENTC"),
    ("MECH", "MECH"),
)


class Student(models.Model):
    gr_no = models.CharField(max_length=20)
    student_name = models.CharField(max_length=200)
    student_div = models.CharField(max_length=10, choices=DIV)
    student_branch = models.CharField(max_length=200, choices=DEPARTMENT)
    student_roll = models.CharField(max_length=10)
    student_email = models.EmailField()
    student_mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
