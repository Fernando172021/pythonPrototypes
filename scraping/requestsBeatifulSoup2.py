import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
soup = BeautifulSoup(page.content, 'html.parser')

all_h1_texts = []

#extraindo valores da tag <h1>
for element in soup.select('h1'):
    all_h1_texts.append(element.text)

#extraindo valores da tag <p>
seventh_p_text = soup.select('p')[6]

print(all_h1_texts, seventh_p_text)
