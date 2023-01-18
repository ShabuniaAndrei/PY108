# d = {'dict': 1, 'dictionary': 2}  Словарь
# d_1 = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])
# d_3 = dict.fromkeys(['a', 'b'], 100)
# print(d)
# print(d_3)
# gen_lst = [i*3 for i in range(5)]
# print(gen_lst)
# gen_d = {a: a*3 for a in range(1, 5)}
# gen_d_2 = {a*3 for a in range(1, 5)}
# print(gen_d, type(gen_d))
# print(gen_d, type(gen_d_2))
# print(d1.get('person_3', 'где пользователь?'))
# d1.items()
# d1.keys()
# d1.values()
# for i in d1.items():  ## итерация по ключам
# for k, v in d1.items(): ## итерация по ключам и значениям
#     print(k, v)
# age = 39
# d1 = {'person_1': {'name': 'fiodar', 'age': age, 5:10}, 'person_2': {'name': 'fiodsar'}}
# d2 = {'name': 'MAx'}
# # for name in d1:
# #     print(d1)
# # k_in_d1 = 'name' in d1
# # print(k_in_d1)
# if 'person_2' in d1:
#     del d1['person_2']
# l1 = ['adress', 'house_numb', 'city']
# l2 = ['libnehta', '68', 'Minsk']
# my_dict = dict(zip(l1, l2))
# print(my_dict)
# list_of_keys = my_dict.keys()
# list_of_keys.sort()
# print(list_of_keys, type(list_of_keys))
#
# for i in my_dict:
#     print(i)
#
# for i in my_dict.items:  # кортедж
#     print(i)

# person = {'name': 'Andrei', 'age': 34, 'city': 'Minsk'}
# print(person)

# car = {'BMW': ['325', '535', '740'], 'Tesla': ['Model_X', 'Model_S', 'Model_Y']}
# print(car['BMW'][0], car['BMW'][2])
# print(car['Tesla'][0], car['Tesla'][2])
# x1 = {'a': 2, 'b': 4, 'c': 5, 'd': 6}
# count = 0
# d2 = {'b': 4, 'c': 5, 'd': 6}
# d2 = {'b': 4, 'c': 5, 'd': 6}
# for n in d1.values():
#     for k in d2.values():
#         count += n*k
# print(count)
# print(2*4+2*5+2*6)

# s = 'phytonist'
# gen_lst = {i: s.count(i) for i in s}
# print(gen_lst)
#
# py_dict = {}
# for i in s:
#     c = s.count