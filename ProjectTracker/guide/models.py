from django.db import models

# Create your models here.

SPECIALIZATION = (
    ("AI/ML", "AI/ML"),
    ("Cloud", "Cloud"),
    ("Blockchain", "Blockchain"),
    ("Cyber Security", "Cyber Security"),
    ("HCI", "HCI"),
    ("Robotics", "Robotics"),
)

DEPARTMENT = (
    ("CS", "CS"),
    ("IT", "IT"),
    ("ENTC", "ENTC"),
    ("MECH", "MECH"),
)


class Guide(models.Model):
    guide_name = models.CharField(max_length=200)
    guide_department = models.CharField(
        max_length=200, choices=DEPARTMENT)
    guide_email = models.EmailField()
    guide_mobile = models.CharField(max_length=20)
    guide_specilization = models.CharField(
        max_length=50, choices=SPECIALIZATION)

    def __str__(self):
        return self.guide_name
