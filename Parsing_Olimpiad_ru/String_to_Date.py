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

class DatesConverter:
    def __init__(self, date_numbers, date_labels):
        self.date_numbers = date_numbers # 1
        self.date_labels = date_labels   # 2
        self.year = int(str(datetime.datetime.now())[0:4])
        self.check_date()

    def check_date(self):
        self.date_labels_slice = self.dates_labels.text.replace("Прошедшие события", "").replace("..."," ").split()
        for i in rus_to_eng_mn:
            if i in self.date_labels_slice:
                print(i)

    def str_to_dt_b():
        dt_b = dt_b.replace("..."," ").split()
        dtt = dt_b[0]
        if dt_b[1].isdigit() == True:
            dt_b_mn = rus_to_eng_mn[dt_b[2]]
        else:
            dt_b_mn = rus_to_eng_mn[dt_b[1]]
        if dt_b[0].isdigit() == False:
            dtt = dt_b[1]
        mnt = dt_b_mn
        return datetime.date(year, dt_b_mn, int(dtt))
        
    def str_to_dt_e(dt_e):
        year = int(str(datetime.datetime.now())[0:4])
        dt_e = dt_e.replace("..."," ").split()[::-1]
        dt_e_mn = rus_to_eng_mn[dt_e[0]]
        if dt_e_mn < mnt:
            year = year + 1
        return datetime.date(year, dt_e_mn, int(dt_e[1]))








