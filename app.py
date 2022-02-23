from flask import Flask, render_template
import json
from data_structures import websites

# Configure application
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Load URLs
with open("url.json", "r") as urls:
    URLS = json.load(urls)

    urls_dict = dict()
    urls_dict.update(URLS)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", brands=urls_dict.keys(), data=urls_dict.values())

#
# ANALYTICS APP
#

@app.route("/analytics/brand/<brand>", methods=['GET', 'POST'])
def brand_view(brand):

    print(brand)

    selected_brand = websites[brand]
    cats=selected_brand['categories'].keys()
    tags=selected_brand['tags'].keys()

    print(cats)
    print(tags)

    return render_template(
        "brand.html",
        brand=brand, 
        cats=cats,
        tags=tags
        )


@app.route("/analytics/category/<category>/<brand>", methods=['GET', 'POST'])
def category(category, brand):

    print(brand)
    print(category)

    category_id = websites[brand]['categories'][category]['id']
    
    print(category_id)

    posts = []

    with open(f"posts/{brand}.json", "r") as posts_src:
        post_data = json.load(posts_src)

    for item in post_data:
        if category_id in item['categories']:
            posts.append(item)

    return render_template(
        "taxonomy.html",
        title=category,
        posts=posts
    )


@app.route("/analytics/tag/<tag>/<brand>", methods=['GET', 'POST'])
def tag(tag, brand):

    print(brand)
    print(tag)

    tag_id = websites[brand]['tags'][tag]['id']
    
    print(tag_id)

    posts = []

    with open(f"posts/{brand}.json", "r") as posts_src:
        post_data = json.load(posts_src)

    for item in post_data:
        if tag_id in item['tags']:
            posts.append(item)

    return render_template(
        "taxonomy.html",
        title=tag,
        posts=posts
    )