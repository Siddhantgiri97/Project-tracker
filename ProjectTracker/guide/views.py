from django.shortcuts import render, redirect
from .models import Guide
from .forms import GuideRegistration
# Create your views here.


def guide_list(request):
    guides = Guide.objects.all()
    context = {'guides': guides}
    return render(request, "guide/guide.html", context)


def add_guide(request):
    if request.method == 'POST':
        form = GuideRegistration(request.POST)
        if form.is_valid():
            form.save()
        return redirect('guide:guide_list')
    else:
        form = GuideRegistration()
    context = {'form': form}
    return render(request, "guide/add_guide.html", context)


def update_guide(request, pk):
    guide = Guide.objects.get(id=pk)
    if request.method == 'POST':
        form = GuideRegistration(request.POST, instance=guide)
        if form.is_valid():
            form.save()
        return redirect('guide:guide_list')
    else:
        form = GuideRegistration(instance=guide)
    context = {'form': form}
    return render(request, "guide/update_guide.html", context)
