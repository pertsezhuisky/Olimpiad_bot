import requests
from bs4 import BeautifulSoup
from Olimpiad_ALL_LINKS import URL_LIST_ALL_LINKS


"""
НТО, Высшая проба, всесиб, физтех, Олимпиада школьников «Ломоносов», Санкт-Петербургского государственного университета, Всероссийская олимпиада школьников «Высшая проба», 
Многопредметная олимпиада «Юные таланты», Отраслевая олимпиада школьников «Газпром», Кутафинская олимпиада школьников по праву.

"""


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
