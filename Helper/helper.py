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