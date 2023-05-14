import datetime

rus_to_eng_mn = {
                "янв" :	1,
                "фев" :	2,
                "мар" :	3,
                "апр" :	4,
                "май" : 5,
                "июн" : 6,
                "июл" : 7,
                "авг" : 8,
                "сен" : 9,
                "окт" : 10,
                "ноя" : 11,
                "дек" : 12,
                }


def check_date(dates_labels, dates_numbers):
    date_labels_slice = dates_labels[0].text.replace("Прошедшие события", "").replace("..."," ").split()
    date_numbers_slice = dates_numbers[0].text.replace("Прошедшие события", "").replace("..."," ").split()
    for i in rus_to_eng_mn:
        if i in date_labels_slice:
            date_begin = str_to_dt_b(date_labels_slice)
            date_end = str_to_dt_e(dates_numbers[-1].text.replace("Прошедшие события", ""))
            break
    if "date_begin" not in vars() or "date_end" not in vars():
        date_begin = str_to_dt_b(date_numbers_slice)
        date_end = str_to_dt_e(dates_numbers[-1].text.replace("Прошедшие события", ""))
    if "date_begin" not in vars() or "date_end" not in vars():
        return
    if str(date_end - date_begin)[0] == "-":
        date_end = year_changing(date_end, str(date_end)[3]) 
    return date_begin, date_end


def str_to_dt_b(dt_b):
    year = int(str(datetime.datetime.now())[0:4])
    dtt = dt_b[0]
    if dt_b[1].isdigit() == True:
        dt_b_mn = rus_to_eng_mn[dt_b[2]]
    else:
        dt_b_mn = rus_to_eng_mn[dt_b[1]]
    
    if dt_b[0].isdigit() == False:
        dtt = dt_b[1]
    return datetime.date(year, dt_b_mn, int(dtt))
    
def str_to_dt_e(dt_e):
    year = int(str(datetime.datetime.now())[0:4])
    dt_e = dt_e.replace("..."," ").split()[::-1]
    dt_e_mn = rus_to_eng_mn[dt_e[0]]
    return datetime.date(year, dt_e_mn, int(dt_e[1]))

def year_changing(date_end, year_ch):
    date_end = str(date_end)
    date_end = date_end.replace(f"{year_ch}", str(int(year_ch) + 1), 1)
    date_end = datetime.date(int(date_end[0:4]), int(date_end[5:7].replace("0", "")), int(date_end[8:].replace("0", "")))
    return date_end




