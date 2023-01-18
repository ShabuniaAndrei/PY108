# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(3))

# def my_func(a):
#     def helper(b):
#         return a + b
#     return helper
#
#
# print(my_func(2)(10))

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
#
#
# mul_2 = mul(3)
# print(mul_2(5))

# def func(*arg):
#     print(arg)
#     count = 0
#     for i in arg:
#         if int(i) % 2 == 0:
#             count += 1
#     return count
#
#
# print(func(4, 5, 6))
# import math
#
#
# def krug(rr):
#     return math.pi*rr**2
#
#
# def pryam(aa, bb):
#     return aa*bb
#
#
# def treug(aa, bb):
#     return 1/2*(aa*bb)
#
#
# n = input('Введите к, п, т: ')
# if n == 'к':
#     r = int(input('введите R: '))
#     print(krug(r))
# elif n == 'п':
#     a, b = int(input('введите А: ')), int(input('введите B: '))
#     print(pryam(a, b))
# elif n == 'т':
#     a, b = int(input('введите А: ')), int(input('введите B: '))
#     print(treug(a, b))
import random


# n = 10   ##
# my_list
#
# def func(a, b):
#     z = list([random.randint(a, b) in range(10)])
#     return z
#
#
# print(func(a=int(input()), b=int(input())))


# def time_sec(n):
#     return f"{n // (60*60*24)}:{n % (60*60*24)//(60*60)}:{n % (60*60)//60}:{n % 60}"
#
#
# print(time_sec(999999))
#
#
# a = 100
# a = 100 % (60*60)
# print(a)
# a = a // 60
# print(a)

# def time(sec):
#     day = sec // (24*3600)
#     sec = sec % (24 *3600)
#     hour = sec // 3600
#     sec = sec % 3600
#     mint = sec // 60
#     sec = sec % 60
#     return f'{day}:{hour}:{mint}:{sec}'
# print(time(3700))

# def witch(s):
#     a = 0
#     b = 0
#     for i in s:
#         if i in 'аеёиоуюяaeoiu'
#             a += 1
#         else:
#             b += 1
#     return f'В строке гласных {a}, а согласных{b}'