from django.urls import path
from .import views

app_name = "team"

urlpatterns = [
    path('', views.team_list, name="team_list"),
    path('add_team/', views.add_team, name="add_team"),
    path('update_team/<int:pk>/', views.update_team, name="update_team"),
    path('delete_team/<int:pk>/', views.delete_team, name="delete_team"),

]
