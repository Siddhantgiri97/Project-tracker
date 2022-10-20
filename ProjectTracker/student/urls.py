from django.urls import path
from .import views

app_name = "student"

urlpatterns = [
    path('', views.student_list, name="student_list"),
    path('add_student/', views.add_student, name="add_student"),
    path('update_student/<int:pk>/', views.update_student, name="update_student"),

]
