# read readme file
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
import os
import json

BLOG = 'https://leeleelee3264.github.io/archives/'
README = 'README.md'
LIMIT = 5
ANCHOR = 'Post'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def write_new_readme() -> None:
    posts = get_recent_post()

    for post in posts:
        print(post)
    write_to_readme(posts)


def get_recent_post() -> List:

    posts = []
    raw_posts = _get_recent_post_from_website()

    for raw_post in raw_posts:
        post = _format_recent_post(raw_post)
        posts.append(post)

    return posts[:LIMIT]


def write_to_readme(posts: List) -> None:
    template = _get_readme_template()
    new_readme = template + posts

    with open(os.path.join(BASE_DIR, README), 'w+', encoding='utf-8') as file:
        file.write("\n".join(new_readme))


def _get_recent_post_from_website() -> List:

    req = requests.get(BLOG)
    req.encoding = 'utf-8'

    html = req.content
    parser = BeautifulSoup(html, 'html.parser')

    posts = parser.select('body > main > div.container-lg.clearfix > div > div.post > h3')
    return posts


def _format_recent_post(element) -> str:
    raw_title = element.text.strip()
    raw_link = element.contents[1].attrs['href']

    post = f'- [{raw_title}]({raw_link})'
    return post


def _get_readme_template() -> List:

    template = []
    raw_lines = _read_from_readme()

    for raw_line in raw_lines:
        line = raw_line.strip('\n')
        template.append(line)

        if ANCHOR in line:
            break

    return template


def _read_from_readme() -> List:
    with open(README, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        return lines


if __name__ == "__main__":
    write_new_readme()
