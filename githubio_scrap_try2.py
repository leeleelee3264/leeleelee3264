# file for scrapping github.io try 2

import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("start scrapping....")
static_url = 'https://leeleelee3264.github.io'

req = requests.get(static_url)
req.encoding=None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select('.post-link')

data = {}

for title in datas:
    link = static_url + title.attrs['href']
    text = title.text
    data[link] = text

print(data)

with open(os.path.join(BASE_DIR, 'post.json'), 'w+', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent='\t')