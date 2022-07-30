import requests
from bs4 import BeautifulSoup
import json

url = 'https://pt.stackoverflow.com/questions/tagged/python'
resposta = requests.get(url)
html = BeautifulSoup(resposta.text, 'html.parser')
lista_info = []

with open('scrap.json', 'w', encoding='utf8') as json_scrap:
    for pergunta in html.select('.s-post-summary'):
        titulo = pergunta.select_one('.s-link')
        data = pergunta.select_one('.s-user-card--time')
        numero_de_votos = pergunta.select_one('.s-post-summary--stats-item-number')
        votos = pergunta.select_one('.s-post-summary--stats-item-unit')
        info = f'{numero_de_votos.text}  {votos.text}  {data.text}  {titulo.text}'
        lista_info.append(info)
    for item in lista_info:
        json.dump(item, json_scrap, indent=4, ensure_ascii=False)
        json_scrap.write('\n')
