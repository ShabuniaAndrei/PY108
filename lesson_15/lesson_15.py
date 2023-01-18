# for e, i in enumerate([1,23,3,4], 4):
#     print(e, i)

# def bmi(heig_weig):
#
#     bmi_ind = int(heig_weig[1])/float(heig_weig[0])**2
#     if bmi_ind > 30:
#         result = 'Вы имеете избыточный вес'
#     elif 25 <= bmi_ind <= 30:
#         result = 'Все ок'
#     elif bmi_ind < 25:
#         result = 'Вам не хватает веса'
#     return result
#
#
# height_weight = input('Введите вначале рост в м, затем вес в кг через пробел: ').split()
# print(bmi(height_weight))

# def figure(sides):
#
#     figure_sides = {3: 'Треугольник', 4: 'Прямоугольник', 5: 'Пятиугольник', 6: 'Шестиугольник',
#                     7: 'Семиугольник', 8: 'Восьмигольник', 9: 'Девятигольник'}
#     return figure_sides[len(sides)]
#
#
# sides_number = input('Введите величину каждой стороны через пробел: ').split()
# print(figure(sides_number))


# def next_day(w):
#     from datetime import datetime, timedelta
#     dt = datetime.strptime(w,'%Y-%m-%d')
#     res = dt + datetime.timedelta(days=1)
#     return res.strftime('%Y-%m-%d')
#
#
# print(next_day('2020-02-29'))

# from datetime import date, timedelta
#
#
# def next_day(*args):
#     dt = date(year, mont, day)
#     dt_n = dt + timedelta(days=1)
#     return dt_n
#
#
# year, mont, day = int(input()), int(input()), int(input())
# print(next_day(year, mont, day))
# def shipping_amount():
#     number_of_purchases = int(input('Введите количество покупок: '))
#     return 10.95+2.95*(number_of_purchases-1)
#
#
# print(shipping_amount())


# def fraction(num, denomin):
#     for i in range(1, num):
#         if num % i == 0 and denomin % i == 0:
#             num = num / i
#             denomin = denomin / i
#     return int(num), int(denomin)
#
#
# numerator, denominator = int(input()), int(input())
# print(*fraction(numerator, denominator))

# def sorting_values(values):
#     lst_dig = sorted([i for i in lst if isinstance(i, int)])
#     lst_alp = sorted([i for i in lst if isinstance(i, str)])
#
#     return values[::-1], lst_dig+lst_alp, values[1:8], values[:5]+values[6:], set(values)
#
#
# lst = ('HELLO', 67, 'word', 'hi', 4, 20, 'python', '3', 'ssss', 444)
# print(sorting_values(lst))


# def operation(lst_1, min_1, max_1):
#     count = 0
#     for i in lst_1:
#         if min_1 < i < max_1:
#             count += 1
#     return count
#
#
# lst_2 = (10.5, 20, 6, 20, 10.5, 20, 8, 11.1, 6, 20, 20)
# min_2, max_2 = int(input()), int(input())
# print(operation(lst_2, min_2, max_2))

# def operation_2(lst_6):
#     count = 0
#     for i in lst_6:
#         if type(i) is list:
#             count += 1
#     return count
#
#
# lst_5 = [[10.5, 20], [20, 10.5, 20], 8, 11.1, [6, 20, 20]]
# print(operation_2(lst_5))
#
#
# def anagram(x, y):
#     if set(x) == set(y) and len(x) == len(y):
#         resul = 'Слова анаграммы'
#     else:
#         resul = 'Слова неанаграммы'
#     return resul
#
#
# x_1, y_1 = input(), input()
# print(anagram(x_1, y_1))
