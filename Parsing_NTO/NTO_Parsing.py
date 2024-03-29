import requests
from NTO_ALL_LINKS import links_to_nto
from bs4 import BeautifulSoup
import json
from datetime import datetime
import locale


locale.setlocale(locale.LC_TIME, "ru_RU")

flag = 0

month_mapping = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

def date_convetation(date_string):
    for russian_month, numeric_month in month_mapping.items():
        date_string = date_string.replace(russian_month, numeric_month)
    date = datetime.strptime(date_string, "%d%m %Y")
    return date.strftime("%d-%m-%Y")

olimpiad = []

def convert_level(level):
    if "III уровень РСОШ" in level:
        return 3
    elif "II уровень РСОШ" in level:
        return 2
    elif "I уровень РСОШ" in level:
        return 1
    else:
        return 0

for url in links_to_nto:
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    name = bs.find("h1").text.replace("  ", "").replace("\n", "")
    level_sps = bs.find_all("li", class_="profile-level")
    description = bs.find("div", class_="profile-2-text").text.replace("\n", "").replace("\r", "").replace("\t", "").replace("<>","").replace("  ", "").replace("\"", "**")
    for prize in level_sps:
        prize_text = prize.text.replace("  ", "").replace("\n", "")
        if "уровень РСОШ" in prize_text:
            level_soup = prize_text
        if "100" in prize_text:
            prizes = prize_text

    list_subjects = []
    subjects = bs.find_all("span", class_="input-title")
    for sub in subjects:
        sub_text = sub.text.replace("\n", "").replace(" ", "")
        list_subjects.append(sub_text)

    date = bs.find("ul", class_="information-stages-list")
    date = date.find_all("div", class_="list-item-data")
    date_elements = bs.find("ul", class_="information-stages-list").find_all("div", class_="list-item-data")
    year_elements = bs.find("ul", class_="information-stages-list").find_all("div", class_="list-item-year")

    if date_elements and year_elements:
        year_begin = year_elements[0].text.strip()
        year_end = year_elements[-1].text.strip()



    for date_id in date:
        if date.index(date_id) == 0:
            date_begin = date_id.text.replace("\n", "").replace(" ", "")
            dash_replacement = date_begin.find("—")
            date_begin = date_begin[0:dash_replacement]
            date_begin = date_begin + ' ' + year_begin
            date_begin = date_convetation(date_begin)
        if date.index(date_id) == len(date) - 1:
            date_end = date_id.text.replace("\n", "").replace(" ", "")
            dash_replacement = date_end.find("—")
            date_end = date_end[dash_replacement+1:]
            # Добавление года окончания олимпиады в поле date_end
            date_end = date_end + ' ' + year_end
            date_end = date_convetation(date_end)

    if "(Студенческий трек)" not in name:
        grade = [8,9,10,11]
    else:
        grade = [12]
    type_olimpiad = "олимпиада"
    format = "очно-заочная"

    level = convert_level(level_soup)

    olimpiad_data = {
        "name": name,
        "description": description,
        "begin_date": date_begin,
        "end_date": date_end,
        "event_type": type_olimpiad,
        "level": level,
        "format": format,
        "grade": grade,
        "subjects": list_subjects,
        "prizes": prizes,
        "URL":url,
    }
    olimpiad.append(olimpiad_data)

# Конвертируем данные в формат JSON с отступами
json_data = json.dumps(olimpiad, ensure_ascii=False, indent=4)

# Сохраняем JSON в файл
with open("olimpiad_data_nto.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)