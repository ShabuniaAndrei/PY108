# import random
# n = str(random.randint(100,999))
# n1 = int(n[0])
# n2 = int(n[1])
# n3= int(n[2])
# n4=n1+n2+n3
# print(n, n4)
# z = 293
# n11 = z//100
# n21 = (z//10)%10
# n23 = z%10

# import random
# n = random.randint(100,999)
# print(f" Значение числа n равно: {n}")
# n1=n//100
# n2=n//10%10
# n3=n%10
# print(n1, n2, n3)
# print(n1+n2+n3)

# print(len([number for number in input().split()]))



# # объявление функции
# def is_one_away(word1, word2):
#     str_w1 = []
#     str_w2 = []
#     w1_len = len(word1)
#     w2_len = len(word2)
#     count = 0
#     for i in word1:
#         for n in i:
#             str_w1.append(n)
#     for i in word2:
#         for n in i:
#             str_w2.append(n)
#     for j in str_w1:
#         for k in str_w2:
#             if j == k:
#                 del [j]
#     if count+1 == w1_len and w1_len == w2_len:
#         flag = True
#     else:
#         flag = False
#     return flag
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))

# from math import sqrt
# def solve(a, b, c):
#     d = b**2-4*a*c
#     if d == 0:
#         x1 = -b / (2 * a)
#         return x1, x1
#     else:
#         if ((-b - sqrt(d)) / (2 * a)) < ((-b + sqrt(d)) / (2 * a)):
#             x1 = ((-b - sqrt(d)) / (2 * a))
#             x2 = ((-b + sqrt(d)) / (2 * a))
#         else:
#             x1 = ((-b + sqrt(d)) / (2 * a))
#             x2 = ((-b - sqrt(d)) / (2 * a))
#     return x1, x2
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# for i in (solve(a, b, c)):
#     print(i)


# n = input()
# if len(n) == 5:
#     print(int(n[::-1]))
# else:
#     k = n[0]+n[:-6:-1]
#     print(int(k))
count = 1
sum_fac = 0
n = int(input())
for i in range(1, n+1):
    count *= i
    sum_fac += count
print(sum_fac)
