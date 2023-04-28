"Файл, где будем вытаскивать инфу с сайта НТО с помошью ссылок из файла NTO_ALL_LINKS"

import requests
from NTO_ALL_LINKS import links_to_nto_eight_eleven
from bs4 import BeautifulSoup


url = "https://ntcontest.ru/tracks/nto-school/proekt-novogo-proizvodstva/avtomatizatsiya-bisnes-protsessov/"
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")
name = bs.find("h1").text.replace("  ", "").replace("\n", "")
prizes = bs.find_all("li", class_="profile-level")
for prize in prizes:
    prize = prize.text.replace("  ", "").replace("\n", "")
    if "уровень РСОШ" in prize:
        prizes = prize
        break   
    else:
        prizes = "No Info"
try:
    if prizes == []:
        prizes = "No Info"
except:
    pass

list_subjects = []
subjects = bs.find_all("span", class_="input-title")
for sub in subjects:
    sub = sub.text.replace("\n", "").replace(" ", "")
    list_subjects.append(sub)

grade = "8-11 класс"    



print(name, prizes, url)













