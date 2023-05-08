"Определяем все ссылки на олимпиады"

import requests
from bs4 import BeautifulSoup


URL_LIST = [
    "https://olimpiada.ru/activity/22", "https://olimpiada.ru/activity/125", "https://olimpiada.ru/activity/123", "https://olimpiada.ru/activity/240"
    "https://olimpiada.ru/activity/181", "https://olimpiada.ru/activity/146", "https://olimpiada.ru/activity/233", "https://olimpiada.ru/activity/22",
           ]

URL_LIST_ALL_LINKS = ['https://olimpiada.ru//activity/5668', 'https://olimpiada.ru//activity/5668', 'https://olimpiada.ru//activity/157', 'https://olimpiada.ru//activity/157', 'https://olimpiada.ru//activity/5319', 'https://olimpiada.ru//activity/5319', 'https://olimpiada.ru//activity/5715', 'https://olimpiada.ru//activity/5715', 'https://olimpiada.ru//activity/158', 'https://olimpiada.ru//activity/158', 'https://olimpiada.ru//activity/159', 'https://olimpiada.ru//activity/159', 'https://olimpiada.ru//activity/227', 'https://olimpiada.ru//activity/227', 'https://olimpiada.ru//activity/5208', 'https://olimpiada.ru//activity/5208', 'https://olimpiada.ru//activity/153', 'https://olimpiada.ru//activity/153', 'https://olimpiada.ru//activity/147', 'https://olimpiada.ru//activity/147', 'https://olimpiada.ru//activity/228', 'https://olimpiada.ru//activity/228', 'https://olimpiada.ru//activity/5669', 'https://olimpiada.ru//activity/5669', 'https://olimpiada.ru//activity/149', 'https://olimpiada.ru//activity/149', 'https://olimpiada.ru//activity/5819', 'https://olimpiada.ru//activity/5819', 'https://olimpiada.ru//activity/150', 'https://olimpiada.ru//activity/150', 'https://olimpiada.ru//activity/5574', 'https://olimpiada.ru//activity/5574', 'https://olimpiada.ru//activity/5447', 'https://olimpiada.ru//activity/5447', 'https://olimpiada.ru//activity/151', 'https://olimpiada.ru//activity/151', 'https://olimpiada.ru//activity/5058', 'https://olimpiada.ru//activity/5058', 'https://olimpiada.ru//activity/160', 'https://olimpiada.ru//activity/160', 'https://olimpiada.ru//activity/5448']


"""for url in URL_LIST: 
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    for elem in bs.find_all("a", class_="none_a black"):
        URL_LIST_ALL_LINKS.append("https://olimpiada.ru/"+ elem["href"])
print(URL_LIST_ALL_LINKS)"""