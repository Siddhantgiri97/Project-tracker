from django.urls import path
from .import views

app_name = "guide"

urlpatterns = [
    path('', views.guide_list, name="guide_list"),
    path('add_guide/', views.add_guide, name="add_guide"),
    path('update_guide/<int:pk>/', views.update_guide, name="update_guide"),
    path('delete_guide/<int:pk>/', views.delete_guide, name="delete_guide"),

]
