# BeatifulSoup é um framework utilizado para extrair dados de uma pagina web

import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
soup = BeautifulSoup(page.content, 'html.parser')

page_title = soup.title.text
page_body = soup.body
page_head = soup.hand

print(page_title, page_body, page_head)
