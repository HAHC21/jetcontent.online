from django.shortcuts import render

from core.models import Site


def index(request):
    data = {
        'sites': Site.objects.all()
    }
    return render(request, 'index.html', data)


def show(request, id):
    data = {
        'site': Site.objects.filter(id=id).first()
    }
    return render(request, 'show.html', data)
