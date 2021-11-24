from django.shortcuts import render

from core.models import Site
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
        'site': Site.objects.filter(id=id).first()
    }

    category_global = {}
    tag_global = {}

    try:
        response = requests.get(
            site.url + "/wp-json/wp/v2/posts", params={
                'per_page': 100
            },
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        info = []
        for item in response.json():
            post_id = item['id']
            title = item['title']['rendered']

            categories = []
            for category in item['categories']:
                if category_global.get(category):
                    categories.append(category_global.get(category))
                else:
                    category_result = requests.get(
                        site.url + "/wp-json/wp/v2/categories/" + str(category),
                        headers={'Content-Type': 'application/json'}
                    )
                    categories.append(category_result.json()["name"])
                    category_global[category] = category_result.json()["name"]

            tags = []
            for tag in item['tags']:
                if tag_global.get(tag):
                    tags.append(tag_global.get(tag))
                else:
                    tag_result = requests.get(
                        site.url + "/wp-json/wp/v2/tags/" + str(tag),
                        headers={'Content-Type': 'application/json'}
                    )
                    tags.append(tag_result.json()["name"])
                    tag_global[tag] = tag_result.json()["name"]

            media = media_result = requests.get(
                item['_links']['wp:featuredmedia'][0]['href'],
                headers={'Content-Type': 'application/json'}
            )

            media = media.json()['guid']['rendered']
            date = item['date']
            author = ''

            print(item)

    return render(request, 'show.html', data)
