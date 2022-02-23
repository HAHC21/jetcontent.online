from time import sleep
import requests, json

def load_posts(container):

    for key in container:

        print(f"Loading {key}...")

        print("     Loading posts")
        data = requests.get(f'{container[key]}/wp-json/wp/v2/posts?per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')
        data2 = requests.get(f'{container[key]}/wp-json/wp/v2/posts?offset=100&per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')
        data3 = requests.get(f'{container[key]}/wp-json/wp/v2/posts?offset=200&per_page=100&_fields=id,excerpt,title,link,date,slug,categories,tags')

        print("     Cleaning JSON data...")
        cdata1 = clean_data(data.content)
        cdata1 = list(cdata1)

        cdata2 = clean_data(data2.content)
        cdata3 = clean_data(data3.content)

        if cdata2:
            print("     Adding more posts to the container from secondary request...")
            for item in cdata2:
                cdata1.append(item)

        if cdata3:
            print("     Adding more posts to the container from third request...")
            for item in cdata3:
                cdata1.append(item)

        print("     Saving file...")
        save_file(cdata1, key)

def save_file(data, name):

    with open(f"posts/{name}.json", "w") as file:
        file.write(json.dumps(data))
    
    file.close()
    sleep(2)

def clean_data(data):
    
    proc = str(data)
    proc = proc.replace("b'", "")
    proc = proc.replace("'", "")
    proc = proc.replace("\n", "")
    proc = proc.replace("\\", "")
    proc = proc.replace("</p>n", "")
    proc = proc.replace("<p>", "")
    proc = proc.replace("u2019", "'")

    json_c = json.loads(proc)

    return json_c