import requests
import json 
import urllib2
import glob

def get_page(page):
    payload = {'f[topic_facet][]': 'Architecture', 'page': page}

    response = requests.get('https://d.lib.ncsu.edu/collections/catalog/manifest/page', params=payload)
    return response.json()

def collect_urls(page):
    ## Store each manifest URL from that page
    ids = []
    for member in page['members']:
        ids.append(member['@id'])
        # print ids

    ## Read the json files and collect Schema.json URLs
    collect_item =[]
    for i in ids:
        item = requests.get(i).json()
     
        for a in item['seeAlso']:
            if a.get('profile') == "https://schema.org":
                collect_item.append((a.get('@id')))
    return collect_item
    # print collect_item

def save_files(urls):
    ## for each url in collect_item get that url and create a new file 
    data_dir = "/Users/njkhan/Projects/web_scraping/test_data"

    for jsonfile in urls:
        filepath = data_dir + "/" + jsonfile.split('/')[-2] + '.json'
        # print filepath

        f = open(filepath, "w")
        data = urllib2.urlopen(jsonfile)
        for line in data:
            f.write(line)
            f.close()
                    

def all_pages():
    next_page = parsed_response['next']
    go_to_next_page = requests.get(next_page).json()
    
current_page = 1
while True:
    parsed_response = get_page(current_page)
    if not parsed_response['members']:
        break
    
    all_urls = collect_urls(parsed_response)
    save_files(all_urls)
    
    current_page = current_page + 1    
    
print("Done!")
    