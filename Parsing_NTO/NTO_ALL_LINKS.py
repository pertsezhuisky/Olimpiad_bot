"Определяем все ссылки на олимпиады"

import requests
from bs4 import BeautifulSoup

URL_eight_eleven = "https://ntcontest.ru/tracks/nto-school/" 

links_to_nto_eight_eleven = []

request = requests.get(URL_eight_eleven)
bs = BeautifulSoup(request.text, "html.parser")
for elem in bs.find_all("a", class_="item-link"):
    links_to_nto_eight_eleven.append("https://ntcontest.ru" + elem["href"])