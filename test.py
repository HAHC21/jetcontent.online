import pandas
import json

with open("taxonomies.json", "r") as src:
    taxonomies = json.load(src)
    site = taxonomies['happyhomeinsider.com']
    categories = site['categories']
    tags = site['tags']

with open("posts/happyhomeinsider.com.json", "r") as src:
    datasrc = json.load(src)

    #for item in datasrc: