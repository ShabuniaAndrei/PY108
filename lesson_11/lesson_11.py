# a = (1, 2, 3)
# b = [1, 2, 3]
# print(a.__sizeof__())  #размер
# print(b.__sizeof__())  #размер

# a = (2, 43, 34, 3, 6, 7, 8, 9, 3, 7)
# q1, q2 = a[0], a[0]
# for i in a:
#     if i > q1:
#         q1 = i
# for i in a:
#     if i < q2:
#         q2 = i
# print(q1, q2)

# import random
# a = tuple([random.randint(0, 5) for i in range(5)])
# b = tuple([random.randint(-5, 0) for k in range(5)])
# c = a + b
# print(c.count(0))
# print(a)
# print(b)
# print(c)

# lst = ('привет', 'word', 'hi', 'python')
# lst = ', '.join(lst)
# print(lst)
# print(*lst, sep=', ')

# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
#
# if sum(A) > sum(B):
#     print(f'сумма больше в А')
# else:
#     print(f'сумма больше в В')
# print(f'max_A = {A.index(max(A))}, min_A = {A.index(min(A))}')
# print(f'max_B = {B.index(max(B))}, min_B = {B.index(min(B))}')
#
# q1, q2, q3, q4 = A[0], B[0], A[0], B[0]
# for i in A:
#     if i > q1:
#         q1 = i
# # for i in A:
# #     if i < q2:
# #         q2 = i
# # for i in B:
# #     if i > q1:
# #         q3 = i
# # for i in B:
# #     if i < q2:
# #         q4 = i
# # print(A.index(q1), A.index(q2))
# # print(B.index(q3), B.index(q4))
#
# a = {3, 'b', ('a', 'b', 8)}
# b = {777}
# # a.add('HELLO')
# # a.discard(8)
# # a.remove(3)
# # a.pop()
# # print(a)
# # a = a.union(b)
# # print(a)
# # print(a|b)
# # print(a.isdisjoint(b))
# # myset = frozenset(,)
#
# count = 0
# q = a[0]
# a = (1, 4, 6, 'a', ('k', 'b'))
# b = set(a)
# if len(a) == len(b):
#     print('уникальна')
# else:
#     print('есть дубли')
# a = {1, 4, 6, 'a', ('k', 'b')}
# b = frozenset([1, 78, ('k', 'b')])
# print(a)
# print(b)
# print(a | b)
# print(a & b)

def fact(n):
    if n != 0:
        return n*fact(n-1)
    else:
        return 1


print(fact(6))