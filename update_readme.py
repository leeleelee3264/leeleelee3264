# read readme file
import requests
from bs4 import BeautifulSoup
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open('README.md', 'r+', encoding='utf-8') as f:
    lines = f.readlines()

new_readme = []

comp = '### :bettle: Cheat Sheet for myself :bettle: '

for line in lines:
    temp_line = line.strip('\n')
    new_readme.append(temp_line)
    if temp_line == comp:
        break

# scrap
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
    new_post = """- [{0}]({1})""".format(text, link)
    new_readme.append(new_post)


print(new_readme)

with open(os.path.join(BASE_DIR, 'README.md'), 'w+', encoding='utf-8') as w_readme:
        w_readme.write("\n".join(new_readme))
