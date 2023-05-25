import requests
import datetime
import json
from bs4 import BeautifulSoup
from Olimpiad_ALL_LINKS import URL_LIST_ALL_LINKS
from String_to_Date import check_date

cnt_passed = 0
cnt_errors = 0

def get_standart_pages(url):
    #If mesuaraments are not found on website then default will be used
    level = 0
    date_begin = "01-01-1970"
    date_end = "01-01-1990"
    prizes = "Nothing found"
    format = "Nothing found"

    request = requests.get(url)
    bs = BeautifulSoup(request.text, 'html.parser')

    name = bs.find("h1")
    dates = bs.find("table", class_="events_for_activity")

    try:

        if dates != None:
            dates_numbers = dates.find_all("td", colspan=1)
            dates_labels = dates.find_all("td", colspan=2)  
            date_converter = check_date(dates_labels, dates_numbers)
            # If you need to collect info in datetime.date you should remove str, split and join functions
            date_begin = str(date_converter[0]).split("-")[::-1]
            date_begin = "-".join(date_begin)
            date_end = str(date_converter[1]).split("-")[::-1]
            date_end = "-".join(date_end)

    except:
        pass
    
    description = bs.find("div", class_="info block_with_margin_bottom")
    if description != None:
        description = description.text.replace("\n","").replace("\t","").replace("Еще", "").replace("Свернуть описание", "").replace("\xa0", "").replace("... ", ".").replace("...", ".")

    else:
        description = ""

    level_1 = bs.find_all("div", class_="f_blocks")
    
    subj = bs.find("div", class_="subject_tags_full")
    grade_str = bs.find("span", class_="classes_types_a").text

    if grade_str != None:
        grade_str = grade_str.replace(" ", "–").split("–")
        grade = []
        for gr in range(int(grade_str[0]), int(grade_str[1])+1):
            grade.append(gr)
    else:
        grade = []
  
    type_olimpiad = bs.find("h1").text.lower()
    if type_olimpiad.find("олимпиад") != -1:
        tp_olimp = "олимпиада"

    if type_olimpiad.find("конкурс") != -1:
        tp_olimp  = "конкурс"

    if "tp_olimp" not in vars():
        tp_olimp = "неизвестно"

    for perch in level_1:
        if perch.text[3:10] == "Перечне":
            if perch.text[54].isdigit():
                level = int(perch.text[54].replace("Перечень 2022/23 →", ""))
            else:
                cnt = 54
                while cnt < len(perch.text):
                    if perch.text[cnt].isdigit():
                        level = int(perch.text[cnt].replace("Перечень 2022/23 →", ""))
                        break
                    else:
                        cnt = cnt + 1

        if perch.text[1:6] == "Призы":
            prizes = perch.text[6:]

        if perch.text[1:7] == "Льготы":
            prizes = perch.text[23:].replace("Подробнее о льготах →", "")

        if perch.text[1:5] == "Очно" or perch.text[1:5] == "Заоч" or perch.text.find("Очная") != -1:
            format = perch.text.replace("я", "я. ", 1).replace("\n", "")

    try:

        dct = {
            "name":name.text,
            "description": description,
            "begin_date": date_begin,
            "end_date": date_end,
            "event_type": tp_olimp,
            "level": level,
            "format" : format,
            "grade":grade,
            "subjects": subj.text.replace("\n", "").replace("\xa0", " ").replace(" язык", "").split(),
            "prizes": prizes,
            "URL" : url,
            } 
        return dct
    
    except:
        pass

olimpiad = []
for web in URL_LIST_ALL_LINKS:
    olimpiad.append(get_standart_pages(web))

# Конвертируем данные в формат JSON с отступами
json_data = json.dumps(olimpiad, ensure_ascii=False, indent=4)

# Сохраняем JSON в файл
with open("olimpiad_data_diff.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)