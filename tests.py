import datetime
import time
import locale

locale.setlocale(locale.LC_TIME, ('ru_RU', 'UTF-8'))


date = "июля"[:-1]
print(date)

print(time.strptime(date, "%b"))
