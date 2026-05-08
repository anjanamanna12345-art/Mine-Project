import urllib.request
import json

def get_wiki_image(title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=800"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id in pages:
            if 'thumbnail' in pages[page_id]:
                return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(e)
    return None

print("Pakhala:", get_wiki_image("Pakhala"))
print("Chhena Poda:", get_wiki_image("Chhena_poda"))
print("Dalma:", get_wiki_image("Dalma_(dish)"))
