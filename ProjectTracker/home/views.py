from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "home/home.html")


def support(request):
    context = {}
    return render(request, "home/support.html")
