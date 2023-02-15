# import requests
# from bs4 import BeautifulSoup
# import re
# response = requests.get('https://av.by/').text
# soup = BeautifulSoup(response, 'lxml')
# items = soup.find_all('li', class_='catalog__item')
# for item in items:
#     url = item.find('a', class_='catalog__link')['href']
#     autos = BeautifulSoup(requests.get(url).text, 'lxml')
#     auto_items = soup.find_all('div', class_='listing-item listing-item--top')
#     for i in auto_items:
#         auto_name = i.find('span', class_='link-text')
#     name = item.find('span', class_='catalog__title').text
#     print(url, name)

