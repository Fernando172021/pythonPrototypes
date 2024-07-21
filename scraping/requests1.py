#requests é um framework que possibilita a conecção com paginas web

import requests

res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

txt = res.text
status = res.status_code

print(txt, status)
