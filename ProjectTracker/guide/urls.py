from django.urls import path
from .import views

app_name = "guide"

urlpatterns = [
    path('', views.guide_list, name="guide_list"),

]
