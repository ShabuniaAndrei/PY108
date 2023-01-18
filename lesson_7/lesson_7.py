# import math
# a, b = int(input()), int(input())
# print(math.sqrt(a**2+b**2))

# a, b, c = input(), input(), input()
# if a > b > c or c > b > a:
#     print('b - среднее число')
# elif b > c > a or a > c > b:
#     print('c - среднее число')
# elif b > a > c or c > a > b:
#     print('a - среднее число')
# else:
#     print('ошибка')

# a, b = int(input()), int(input())
# if a % 2 == 0:
#     if b % 2 == 0:
#         print(f'оба четные')
#     else:
#         print(f'{a} - четное, {b} - нечетное')
# elif b % 2 == 0 and a % 2 != 0:
#         print(f'{b} - четное, {a} - нечетное')
# else:
#     print(f'оба нечетные')

# s = str(input())
# print(s[::-1])
# num = 456
# i = 0
# while num > 0:
#     i = i*10 + num%10
#     num = num //10
# print(i)

# s = '   djg asdfj   klahrt  ni '
# l = s.split()
# s1 = ''.join(l)
# print(s1)

# s = input()
#
# i = 0
# while s[i] == ' ':
#     i += 1
# s = s[i:]
#
# i = len(s)
# while s[i - 1] == ' ':
#     i -= 1
# s = s[:i]
#
# s_new = s[0]
# i = 1
# while i < len(s):
#     if s[i] != ' ':
#         s_new += s[i]
#     elif s[i - 1] != ' ':
#         s_new += ''
#     i += 1
# print(s_new + '!')

# st = 'ПриВет Мир'
# x = ''
# for i in st:
#     if i.islower():
#         x += i
# print(x)
# cont = 0
# for i in range(101):
#     cont += i
# print(cont)
# n = int(input())
# cont = 1
# for i in range(2, n+1):
#     cont *= i
# print(cont)
#
# n = int(input())
# cont = 1
# while n > 1:
#     cont *= n
#     n -= 1
# print(cont)
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2-4*a*c
# if d > 0:
#     x1 = (-b+math.sqrt(d))/(2*a)
#     x2 = (-b-math.sqrt(d))/(2*a)
#     print(x1, x2)
# elif d == 0:
#     x = -b/2*a
#     print(x)
# else:
#     print('корней нет')

# a = ['he', 2, True, 2, '2']
# a_new = []
# for num in a:
#     if a.count(num) == 1:
#         a_new.append(num)
# print(a_new)

# for i in l1:
#     if i in l2:
#         l3 +=[i]
# print(l3)

# l1 = [1, 2, True, 'he']
# l2 = [5, 2, False, 'he']
# l3 = []
# for n in l1:
#     for j in l2:
#         if n == j:
#             l3.append(n)
# print(l3)

# for elem_1 in l1:
#     if elem_1 in l3:
#         continue
#     for elem_2 in l2:
#         if elem_1 == elem_2:
#             l3.append(elem_1)
#             break

pr = 1
for i in range(1, 31):
    if i % 2 !=0:
        pr*=i
print(pr)