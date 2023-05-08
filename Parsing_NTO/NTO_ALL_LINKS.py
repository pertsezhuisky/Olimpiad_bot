"Определяем все ссылки на олимпиады"

import requests
from bs4 import BeautifulSoup

URL_LIST = ["https://ntcontest.ru/tracks/nto-school/" , "https://ntcontest.ru/tracks/nto-student/"]

links_to_nto = []

for url in URL_LIST: 
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    for elem in bs.find_all("a", class_="item-link"):
        links_to_nto.append("https://ntcontest.ru" + elem["href"])