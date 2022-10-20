from django.urls import path
from .import views

app_name = "project"

urlpatterns = [
    path('', views.project_list, name="project_list"),
    path('add_project/', views.add_project, name="add_project"),
    path('update_project/<int:pk>/', views.update_project, name="update_project"),
    
]