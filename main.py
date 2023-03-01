from bs4 import BeautifulSoup
import requests


URL = "https://olimpiada.ru/activity/"
for event_code in range(1, 10):
    url = URL + str(event_code)
    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')
    name = bs.find("h1")
    grade = bs.find("span", class_="classes_types_a")
    description = bs.find("div", class_="info block_with_margin_bottom")
    subj = bs.find("div", class_="subject_tags_full")
    date = bs.find("table", class_="events_for_activity")
    try:
        date_name = date.find("tbody").find_all("div",class_="event_name")
        date_time = date.find("tbody").find_all("a")
        specif_label = bs.find('div', id="features").find_all("span")
        specif = bs.find('div', id="features")
        dct = {"name":name.text,
               "date_name":date_name,
               "date_time":date_time,
               "grade":grade.text,
               "description":description.text.replace("\n","").replace("\t","").replace("Еще", "").replace("Свернуть описание", ""),
               "specifications":specif.text.replace("\n", "").replace("strelka2 Еще факты", "").replace("→", ""),
               'subjects': subj.text.replace("\n", "").replace("\xa0", " ")
               }
        print(dct)

    except:
        pass
