from time import sleep
import requests, json

with open("url.json", "r") as urls:
    URLS = json.load(urls)

def load_posts_old(container):

    for key in container:

        print(f"Loading {key}...")

        print("     Loading posts")
        data = requests.get(f'{container[key]}/wp-json/wp/v2/posts?per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')
        data2 = requests.get(f'{container[key]}/wp-json/wp/v2/posts?offset=100&per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')
        data3 = requests.get(f'{container[key]}/wp-json/wp/v2/posts?offset=200&per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')

        print("     Cleaning JSON data 1 and saving file...")
        cdata1 = clean_data(data.content)


        cdata2 = clean_data(data2.content)
        if cdata2:
            print("     Cleaning JSON data 2 and saving file...")
            save_file(cdata2, f"{key}-2")

        cdata3 = clean_data(data3.content)
        if cdata3:
            print("     Cleaning JSON data 3 and saving file...")
            save_file(cdata3, f"{key}-3")



            

load_posts_2(URLS)