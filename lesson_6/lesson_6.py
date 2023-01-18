
# st = input()
# sym = input()
# res = ''
# for s in st:
#     if s != sym:
#         res += s
# print(res)

# for i in range(100, 1000):
#     if i % 100 == 0:
#         print(i)

# for i in range(94, 351):
#     if i % 5 == 0:
#         print(i)

# lst = [1, 2, 3, 4]
# lst.append(4)
# l = lst.count(4)
# l1 = lst.index(4)
# l2 = lst.pop(4)
# l3 = lst.remove(4)
# l5 = lst.reverse()
# print(lst)

# lst = [123, 432, 657, 345]
# for i in lst:
#     if i == 657:
#         print(1111)
#     else:
#         print(2)

# for number in range(10):
#     if number == 5:
#         print(9999999999)
#     print(f'1')
# print('Какойтокод')

# sum_n = 0
# sum_ch = 0
# ls = [2, 1, 4, 5, 1, 7, 1]
# for i in ls:
#     if i%2 == 0:
#         sum_ch += 1
#     else:
#         sum_n += 1
# if sum_n > sum_ch:
#     print(sum(ls))
# else:
#     print(ls[1]*ls[3]*ls[6])

# for x in range(10, 510, 100):  # [10, 110, 210, 310, 410]
#     for y in range(10, 51, 10):  # [10, 20, 30, 40, 50]
#         print(x+y)
#     print('r13r23r2')
# print('4124124')

# for x in range (1, 10):
#     for y in range(1, 10):
#         print(x*y, '', end = '')
#     print()

# Задача While с помощью списков while <==> for,  for <==> while

# n = int(input())
# while n > 0:
#     if n > n//10:
#         n = n // 10
# print(n)

# 28n+30k+31m=365
# a5+b5+c5+d5=e5.
# n = int(input())
# for i in range(1, n+1):
#     for j in range(i):
#             print(j+1, end='')
#     for k in range(i-1, 0, -1):
#             print(k, end='')
#     print(':thumbs_up:')


# 19/2 = 9 с остатком 1
# 9/2 = 4 c остатком 1
# 4/2 = 2 без остатка 0
# 2/2 = 1 без остатка 0
# 1/2 = 0 с остатком 1


# s = int(input())
# d = ''
# while s != 0:
#     d = str(s % 2) + d
#     s = s-(s-s//2)
s = []
n = int(input())
for i in range(0, n):
    s.append(int(input()))
del s[1::2]
print(s)