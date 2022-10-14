from django.shortcuts import render
from .models import Guide
# Create your views here.


def guide_list(request):
    guides = Guide.objects.all()
    context = {'guides': guides}
    return render(request, "guide/guide.html", context)
