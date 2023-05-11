import requests
import re
import datetime

from bs4 import BeautifulSoup
from Olimpiad_ALL_LINKS import URL_LIST_ALL_LINKS
from String_to_Date import str_to_dt_b, str_to_dt_e


def get_standart_pages(url):
    #If mesuaraments are not found on website then default will be used
    level = 0
    date_begin = datetime.date(1970,1,1)
    date_end = datetime.date(1990,1,1)

    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')

    name = bs.find("h1")

    dates = bs.find("table", class_="events_for_activity")
    if dates != None:
        dates_numbers = dates.find_all("td", colspan=1)
        dates_labels = dates.find_all("td", colspan=2)
        date_begin = str_to_dt_b(dates_labels[0].text.replace("Прошедшие события", "")) 
        date_end = str_to_dt_e(dates_numbers[len(dates_numbers)-1].text.replace("Прошедшие события", "")) 
        
        
    type_olimpiad = "олимпиада"
    
   
    level_1 = bs.find_all("div", class_="f_blocks")
    
    subj = bs.find("div", class_="subject_tags_full")
    grade = bs.find("span", class_="classes_types_a")
  
    for perch in level_1:
        if perch.text[3:10] == "Перечне":
            level = int(perch.text[54:].replace("Перечень 2022/23 →", ""))
    try:
        dct = {
            "name":name.text,
            "begin-date": date_begin,
            "end-date": date_end,
            "type": type_olimpiad,
            "level": level,
            "grade":grade.text,
            "subjects": subj.text.replace("\n", "").replace("\xa0", " ").replace(" язык", "").split(),
            
            } 
        return dct
    except:
        pass


for web in URL_LIST_ALL_LINKS:
    print(get_standart_pages(web))
