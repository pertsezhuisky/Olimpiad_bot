
from bs4 import BeautifulSoup
import requests

"""
НТО, Высшая проба, всесиб, физтех, Олимпиада школьников «Ломоносов», Санкт-Петербургского государственного университета, Всероссийская олимпиада школьников «Высшая проба», 
Многопредметная олимпиада «Юные таланты», Отраслевая олимпиада школьников «Газпром», Кутафинская олимпиада школьников по праву.

"""
lst_olimpiads_nto = [
                 "https://olimpiada.ru/activity/5369", "https://olimpiada.ru/activity/5516", "https://olimpiada.ru/activity/199"
                 ] 

lst_olimpiads_special = [
    "https://olimpiada.ru/activity/22", "https://olimpiada.ru/activity/125", "https://olimpiada.ru/activity/123", "https://olimpiada.ru/activity/240"
    "https://olimpiada.ru/activity/181", "https://olimpiada.ru/activity/146", "https://olimpiada.ru/activity/233", "https://olimpiada.ru/activity/22",
]


def get_special_pages(url):
    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')
    name = bs.find("h1")
    info = bs.find("div", class_="info")
    
    try:
        dct = {
            "name":name.text,
            "grade":grade.text,
            "description":description.text.replace("\n","").replace("\t","").replace("Еще", "").replace("Свернуть описание", "").replace("...", "."),
            "subjects": subj.text.replace("\n", "").replace("\xa0", " "),
            "level": level,
            
        }
    except:
        pass

        
        

def get_standart_pages(url):
    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')
    name = bs.find("h1")
    grade = bs.find("span", class_="classes_types_a")
    info = bs.find("div", class_="info block_with_margin_bottom")
    subj = bs.find("div", class_="subject_tags_full")
    level_1 = bs.find_all("div", class_="f_blocks")
    for perch in level_1:
        if perch.text[3:10] == "Перечне":
            perch = perch.text.replace("Перечень 2022/23 →", "")
            level = perch[22:]
            break
    try:
        dct ={
            "name":name.text,
            "grade":grade.text,
            "info":info.text.replace("\n","").replace("\t","").replace("Еще", "").replace("Свернуть описание", "").replace("...", "."),
            "subjects": subj.text.replace("\n", "").replace("\xa0", " "),
            "level": level,
            } 
        return dct
    except:
        pass


for web in lst_olimpiads_nto:
    print(get_standart_pages(web))

for webpage in lst_olimpiads_special:
    print(get_special_pages(webpage))
