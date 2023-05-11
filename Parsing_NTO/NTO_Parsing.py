"""
Файл, где будем вытаскивать инфу с сайта НТО с помошью ссылок из файла
NTO_ALL_LINKS
"""
import requests
from NTO_ALL_LINKS import links_to_nto
from bs4 import BeautifulSoup

flag = 0

for url in links_to_nto:
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    name = bs.find("h1").text.replace("  ", "").replace("\n", "")
    level_sps = bs.find_all("li", class_="profile-level")
    for prize in level_sps:
        prize = prize.text.replace("  ", "").replace("\n", "")
        if "уровень РСОШ" in prize:
            level = prize
        if "100" in prize:
            prizes = prize

    try:
        if level == [] or level == "":
            level = "No Info"
        if prizes == [] or prizes == "":
            prizes = "No Info"
    except:
        pass

    list_subjects = []
    subjects = bs.find_all("span", class_="input-title")
    for sub in subjects:
        sub = sub.text.replace("\n", "").replace(" ", "")
        list_subjects.append(sub)

    date = bs.find("ul", class_="information-stages-list")
    date = date.find_all("div", class_="list-item-data")

    for date_id in date:
        if date.index(date_id) == 0:
            date_begin = date_id.text.replace("\n", "").replace(" ", "")
            dash_replacement = date_begin.find("—")
            date_begin = date_begin[0:dash_replacement]
        if date.index(date_id) == len(date) - 1:
            date_end = date_id.text.replace("\n", "").replace(" ", "")
            dash_replacement = date_end.find("—")
            date_end = date_end[dash_replacement+1:]

    if "(Студенческий трек)" not in name:
        grade = "8-11 класс"
    else:
        grade = "Студенческий трек"
    type_olimpiad = "олимпиада"
    format = "очно-заочная"
    print(name, date_begin, date_end, type_olimpiad, format, list_subjects,
          level, prizes, grade)
