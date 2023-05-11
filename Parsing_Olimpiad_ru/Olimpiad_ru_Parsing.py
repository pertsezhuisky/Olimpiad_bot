import requests
import re

from bs4 import BeautifulSoup
from Olimpiad_ALL_LINKS import URL_LIST_ALL_LINKS


def get_standart_pages(url):
    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')
    name = bs.find("h1")
    dates = bs.find("table", class_="events_for_activity")
    try:
        dates_name = dates.find_all("div",class_="event_name")
        dates_numbers = dates.find_all("td", colspan=1)
        for date in dates_numbers:
            date_begin = date
            print(date.text.replace("Прошедшие события", ""), url)
    except:
        print("че-то не то", url)
    subj = bs.find("div", class_="subject_tags_full")
    level_1 = bs.find_all("div", class_="f_blocks")
    
    grade = bs.find("span", class_="classes_types_a")
  
    for perch in level_1:
        if perch.text[3:10] == "Перечне":
            level = int(perch.text[54:].replace("Перечень 2022/23 →", ""))
            break
    try:
        dct ={
            "name":name.text,
            "grade":grade.text,
            "subjects": subj.text.replace("\n", "").replace("\xa0", " "),
            "level": level,
            } 
        return dct
    except:
        pass


for web in URL_LIST_ALL_LINKS:
    print(get_standart_pages(web))
