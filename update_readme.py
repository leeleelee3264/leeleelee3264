# read readme file
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

with open(os.path.join(BASE_DIR, 'post.json'), 'r+', encoding='utf-8') as post:
# json file 이라서 data 로 열러준다
    datas = json.load(post)

for key in datas.keys():
    new_post = """- [{0}]({1})""".format(datas[key], key)
    new_readme.append(new_post)


print(new_readme)

with open(os.path.join(BASE_DIR, 'README.md'), 'w+', encoding='utf-8') as w_readme:
        w_readme.write("\n".join(new_readme))
