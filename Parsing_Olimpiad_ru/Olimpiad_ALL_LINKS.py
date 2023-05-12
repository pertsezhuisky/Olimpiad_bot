"Определяем все ссылки на олимпиады"

import requests
from bs4 import BeautifulSoup


"""
НТО, Высшая проба, всесиб, физтех, Олимпиада школьников «Ломоносов», Санкт-Петербургского государственного университета, Всероссийская олимпиада школьников «Высшая проба», 
Многопредметная олимпиада «Юные таланты», Отраслевая олимпиада школьников «Газпром», Кутафинская олимпиада школьников по праву.

"""  

URL_LIST = [
    "https://olimpiada.ru/activity/22", "https://olimpiada.ru/activity/125", "https://olimpiada.ru/activity/123", "https://olimpiada.ru/activity/240"
    "https://olimpiada.ru/activity/181", "https://olimpiada.ru/activity/146", "https://olimpiada.ru/activity/233", "https://olimpiada.ru/activity/22", 
           ]

URL_LIST_ALL_LINKS = []


for url in URL_LIST: 
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    for elem in bs.find_all("a", class_="none_a black"):
        link = "https://olimpiada.ru/" + elem["href"]
        if link not in URL_LIST_ALL_LINKS:
            URL_LIST_ALL_LINKS.append(link)

