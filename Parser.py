import requests
import bs4
url = 'https://tproger.ru/page/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

search = ['С++', 'Python', 'JavaScript', 'IT-команды']

page = 1
print("1) Использовать базовые слова для поиска('С++', 'Python', 'JavaScript', 'IT-команды' \n2) Ввести новые слова")
com = int(input("Введите команду(номер): "))

if com == 1:
    print("Используются базовые слова")
elif com == 2:
    print('Введите 5 поисковых слов через Enter')
    for i in range(5):
        slov = input('Введите поисковое слово: ')
    search.append(slov.strip(' '))
else:
    print("Комадна не найдена")
ran = int(input("Введите число страниц для парсинга(не более 10): "))

while True:
    if ran > 10:
        ran = int(input("Введено число больше 10, повторите ввод: "))
    else:
        break
ran += 1
for page in range(1, ran):
    resp = requests.get(url + str(page)).text
    soup = bs4.BeautifulSoup(resp, features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        link = article.find(class_="article__link").attrs['href']
        temp_art = bs4.BeautifulSoup(requests.get(link).text, features='html.parser')
        #date = temp_art.find(class_='localtime meta__date').text.strip()
        heading = article.find(class_="article__link").text.strip('\n')
        words = heading.split(' ')
        for word in words:
            if word in search:
                print(f'Заголовок: {heading} \nСсылка: {link}')
    print("Перешел к следующей странице")
    page += 1