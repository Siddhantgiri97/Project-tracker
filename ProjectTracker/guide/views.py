from django.shortcuts import render
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
        return redirect('guide:guide')
    else:
        form = GuideRegistration()
    context = {'form': form}
    return render(request, "guide/add_guide.html", context)
