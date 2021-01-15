# file for scrap github.io
# it will be copied for github action


# order
# make github.io scrap code
# run the code with git action
# make git action scrap file and update profile.md

from bs4 import BeautifulSoup
from selenium import webdriver

DIR_PATH = 'C:\\Users\\absin\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe'
driver = webdriver.Chrome(DIR_PATH)
url = 'https://leeleelee3264.github.io/'

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
# body > div.page-content > div > div.wrapper > ul > li:nth-child(1) > h2 > a

titles = soup.select('.post-link')
title_arr = []

for title in titles:
    title_arr.append(title.text)

print(title_arr)