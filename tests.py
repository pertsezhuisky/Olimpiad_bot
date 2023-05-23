from datetime import datetime
import locale

# Установка русской локали
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

date_string = "31 марта 2023"

# Замена названий месяцев на числовые значения
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

for russian_month, numeric_month in month_mapping.items():
    date_string = date_string.replace(russian_month, numeric_month)

# Разбор даты
date = datetime.strptime(date_string, "%d %m %Y")

# Форматирование даты
formatted_date = date.strftime("%d-%m-%Y")

print(formatted_date)
