from django.shortcuts import render

from .models import Project

def index(request):
    try:
        context = {"projects": Project.objects.all()}
        return render(request, 'mywebsite_app/index.html', context)
    except:
        return render(request, 'mywebsite_app/index.html')
