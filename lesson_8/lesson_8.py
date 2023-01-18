# def func():
#     lst = [1, 4, 5, 6]
#     print(sum(lst))
#
#
# func()
#
#
# def lite_sum(a, b):
#     print(a + b)
#
#
# lite_sum(1, 2)

# def func_1():
#     global a
#     a = 1
#     b = 2
#     return a+b
#
#
# def func_2():
#     c = 3
#     return a+c
#
#
# print(func_1())
# print(func_2())

# def simple_fun(a, b): return a + b
#
#
# print(simple_fun(1, 3))

# import random
# print(random.choice([1, 2, 3, 4]))

# hel = lambda x, y: x + y
# print(hel(3, 5), type(s))
# 2  400  100

# def is_year_leap(n):
#     return n % 4 == 0 and n % 100 == 0 or n % 400 == 0
#
#
# print(is_year_leap(int(input())))
# import math
#
#
# def square(a):
#     per = 4*a
#     pl = a**2
#     di = math.sqrt(2)*a
#     return per, pl, di
#
#
# print(square(int(input('Введите сторону квадрата: '))))


# def season(month):
#     global season_name
#     if 3 <= month < 6:
#         season_name = 'spring'
#     elif 6 <= month < 9:
#         season_name = 'summer'
#     elif 9 <= month < 12:
#         season_name = 'autm'
#     elif month == 12:
#         season_name = 'winter'
#     elif month < 3:
#         season_name = 'winter'
#     return season_name
#
#
# print(season(int(input('Введите месяц: '))))

# def is_prime(a):
#     d = 2
#     while a % d != 0:
#         d += 1
#     return d == a
#
#
# print(is_prime(17))
# import random
#
#
# def middle_number():
#     count = 0
#     for i in range(10):
#         n = random.randint(1, 10)
#         print(n, end=' ')
#         count += n
#     return count
#
#
# print(f'Сумма: {middle_number()}')

# def avg_fun(lst, n):
#     s = 0
#     for i in range(n):
#         s += lst[i]
#     return s/n
#
#
# print(avg_fun([1, 2, 3], 3))

# import random
# N = 10
#
# my_lst = [0] * 10
# for i in range(N):
#     my_lst[i] = random.randint(1, 100)
#
#
# def avf_func_1(my_lst):
#     s = 0
#     for i in range(N):
#         s += my_lst[i]
#     return s / N
#
#
# print(my_lst)
# print(avf_func_1(my_lst))