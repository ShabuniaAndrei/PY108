# import random
# c = [i for i in range(10)]
# print(c)
# print(c[0])
# print(c[-1])
# c.append([12, 13])
# c += ('HI')
# c.insert(1, 'YES')
# print(c)
# c[0] = 5
# del c[3], c[5]
# print(c)
# print(c.pop(0))
# print(c)
# c[-3].remove(13)  $$
# import copy

# elem = [1, 3, 6, 'a', 'b', 'abc', 123, 456]
# del elem[4:]
# if 3 in elem:
#     print('1111')
# my_list1 = ['hello']
# my_list2 = ['world']
# res = my_list1 + my_list2
# my_list1.extend([7, 8])
# my_list1.extend('45')
# print(my_list1)
# ls5 = copy.deepcopy(my_list1)
# print(ls5+[2, 4])
# lst = [1, 2, 3, 4, 5, 6]
# new_lst = lst[:-1]

# l1 = [1, 2, 3, 'meow']
# i = 0
# while i < len(l1)-1:
#     print(l1[i])
#     i += 1

# append()
# extend()
# insert(1, 222)
# remove('hi')
# clear()
# index
# pop

# el = [[1, '1'], ['1', 1]]
# print(el[0][1])

# lst = (1, 4, 5, 20, 50)
# for i in lst:
#     if lst.index(20):
#         i = lst.index(20)
#         lst[i] == 200
# print(lst)


# lst = (7, 2, 3, 4, 5, 6, 1)    # решить через функции
# count_1 = 0
# count_2 = 0
# for i in lst:
#     if i % 2 == 0:
#         count_1 += 1
#     else:
#         count_2 += 1
# if count_1 > count_2:
#     print(sum(lst))
# else:
#     print(13*lst[6])

# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1,2]]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# a = [4, 6, 'py', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
# c = a + b
# c.insert(3, 6)
# for i in c:
#     if str(i).isalpha:
#         c.remove(i)
# print(c)
