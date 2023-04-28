URL = "https://olimpiada.ru/activity/"

lst = []

for i in range(1, 20):
    url = URL + str(i)
    try:
        lst.append(url)
    except:
        pass
