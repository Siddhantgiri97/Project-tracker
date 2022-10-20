from django.urls import path
from .import views

app_name = "team"

urlpatterns = [
    path('', views.team_list, name="team_list"),
    path('add_team/', views.add_team, name="add_team"),
    
]
