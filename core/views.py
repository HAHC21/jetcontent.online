from django.shortcuts import render
from django.shortcuts import redirect
from core.models import Site, Article

import requests
from requests.exceptions import HTTPError

def index(request):
    data = {
        'sites': Site.objects.all()
    }
    return render(request, 'index.html', data)


def show(request, id):
    site = Site.objects.filter(id=id).first()
    data = {
        'articles': Article.objects.filter(site_id=site.id).all(),
        'site': site
    }

    return render(request, 'show.html', data)


def article(request, id):
    return render(request, 'article.html')


def import_posts(request, id):

    try:
        response = requests.post(
            "http://192.168.1.10:3000/import-posts",
            data={'id': id},
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as err:
        print(f'Other error occurred: {err}')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


