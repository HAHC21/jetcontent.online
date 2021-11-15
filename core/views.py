from django.shortcuts import render


def index(request):
    data = {
        'name': 'JetContent'
    }
    return render(request, 'index.html', data)
