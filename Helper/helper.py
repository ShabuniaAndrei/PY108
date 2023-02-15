# a=5
# b=2
# print(f"1) здесь мы сложим {a} + {b}")
# print('2) здесь мы сложим {} + {}' .format(a, b))
# print('3) здесь мы сложим %d + %d'% (a, b))  #тип_число
# print('4) здесь мы сложим ' +str(a) + ' + ' + str(b))
# print('5) здесь мы сложим', a, '+', b)
# print('6) здесь мы сложим %s + %s'% (a, b))  #тип строка

# all(все) => True / any(один из) => True

# изменяемые - List (список), dict (словарь), set (множества)
# неизменяемые - frozenset, int, float, bool, str, tuple (кортеж), complex
# id(a) - ID-объекта (местоположение объекта в пямяти) - доказательство что числа неизм. тип данных
# интерперитируемый (строчка за строчкой)
# python - состоит из объектов

# def func(l=None):
#     l = [1]
#     l.append(1)
#     return l
# print(func())
# print(func())

# x = lambda a,b: a+b   - лямбда функция (безымянная)
# print(x(1, 2))

# ключ от словаря должен поддерживать __hash__()

# тернарный оператор
# выражение_1 if условие else выражение_2
# выражение_True
# print('YES') if 1 > 0 else print('NO')

# is / ==    is указывает на равность ID, == на равность элементов
# a = ('tr',)
# b = ('tr',)
# print(a is b)

# Функция Reduce()
# reduce(функция, итерируемый объект, начальное значение) - синтаксис
# Применяет функцию двух аргументов к элементам итерируемого объекта.
# Функции требуется два аргумента, первый из которых является первым элементом в
# итерируемый объект(если начальное значение не указано) а второй - вторым элементом
# в итерируемый объект. Если начальное значение указано, то оно становится первым
# аргументом функции функции, а первый элемент в  итерируемый объект становится вторым элементом.
# Функция reduce "уменьшает"  итерируемый объект до одного значения.
#
# from functools import reduce
# items = [2, 3, 4, 5]
#
#
# def custom_sum(first, second):
#     return first + second
#
#
# result = reduce(custom_sum, items, 10)
# print(result)
# items_max = reduce(lambda a, b: a if (a > b) else b, items)
# print(items_max)
#
# items_multiplication = reduce(lambda num1, num2: num1 * num2, items)
# print(items_multiplication)


# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))

# f1 = lambda x, y, z: x + y + z
# f2 = lambda x, y, z=3: x + y + z
# f3 = lambda *args: sum(args)
# f4 = lambda **kwargs: sum(kwargs.values())
# f5 = lambda x, *, y=0, z=0: x + y + z


# print(f1(1, 2, 3))
# print(f2(1, 2))
# print(f2(1, y=2))
# print(f3(1, 2, 3, 4, 5))
# print(f4(one=1, two=2, three=3))
# print(f5(1))
# print(f5(1, y=2, z=3))
# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
#
# new_strings = list(map(lambda x, y: x*y, strings, numbers))


# dict1 = {'x': 1}
# dict2 = {'y': 2}
# dict3 = {'x': 3, 'y': 4}
#
# result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))

# print('{:,}'.format(int(input()))) - запятая через 3 символа


# import requests
# from lxml import html
# page = requests.get('https://gismeteo.by', headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
# }).text
#
# tree = html.fromstring(page)
# city = tree.xpath('//a[@class="city-link link"]//text()')[0]
# time = tree.xpath('//div[@class="current-time"]//text()')[0]
# descr = tree.xpath('//div[@class="weather-description"]//text()')[0]
# degrees = ''.join(tree.xpath('//div[@class="temperature"]//text()')[:2])
# print(page)
#
# import requests
# from lxml import html
#
# page = requests.get('https://it-math.ru/spisok-literatury-python/', headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
# }).text
# pars_list_page = html.fromstring(page)
# pars_list = pars_list_page.xpath('//div[@class="entry-content cf"]//text()')
# print(pars_list)
# pars_list_redact = map(lambda x: x.replace('\n', '\n\n'), pars_list[2:-4])
# print(list(pars_list_redact))
# pars_new_list = []
# count = 0
# for i in list(pars_list_redact):
#     if i == '\n\n':
#         count += 1
#         pars_new_list.append('\n\n'+str(count))
#     else:
#         pars_new_list.append(i)
# print(pars_new_list)
# result = " ".join(map(str, pars_list_redact))
# print(result)

# list_2 = list_1.replace("\r", "")
# print(list_2)
# list_3 = list_2.replace("\n", "")
# print(list_3)

# time = tree.xpath('//div[@class="current-time"]//text()')[0]
# descr = tree.xpath('//div[@class="weather-description"]//text()')[0]
# degrees = ''.join(tree.xpath('//div[@class="temperature"]//text()')[:2])

# import requests
# from lxml import html
# page = requests.get('https://ronex.by/catalog/skladskaya_tekhnika/', headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
# }).text
#
# tree = html.fromstring(page)
# # city = tree.xpath('//a[@class="city-link link"]//text()')[0]
# time = tree.xpath('//div[@class="article_block muted font_sxs"]//text()')
# # descr = tree.xpath('//div[@class="weather-description"]//text()')[0]
# degrees = ''.join(tree.xpath('//div[@class="temperature"]//text()')[:2])
# feeling = ''.join(tree.xpath('//div[@class="item-value"]//text()')[:2])
# wind = tree.xpath('//div[@class="item-value"]//text()')[4]
# print(page)


