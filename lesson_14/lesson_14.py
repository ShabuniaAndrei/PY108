# a = 20
# b = 10
# res = a if a > b else b
# print(f'большее значение {res}')

#
# def calc(l=[3]):
#     l.append(2)
#     return l
#
#
# print(calc())
# print(calc())
# print(calc())
# print(calc()+calc())
# print(type(calc()))
# print(sum(calc())+sum(calc()))

# my_str = 'awesome'
# print(list(my_str))

# import csv
# example_file = open('example.csv', encoding='UTF-8')
# exampleReader = csv.reader(example_file, delimiter = ";")
# example_data = list(exampleReader)
# for row in exampleReader:
#     string = f'строка # {str()}' + ' '
#         for value in row:
#             string = string + value
#             print(string)

# ex_file = open('write.csv', 'w', encoding='UTF-8', newline='')
# ex_write = csv.writer(ex_file, delimiter=';')
# ex_data = [['05.04.2015 13:23', 'Яблоки', '73'], ['06.04.2015 13:55', 'Груша', '78']]
# for i in ex_data:
#     ex_write.writerow(i)
# ex_file.close()

import json
# my_str = {"name": "fiodar", "id": "1", "email": "example@gmail.com"}
# for i in my_str:
#     i = json.loads(i)
#     print(i['name'])
#
#
# with open('data.json', encoding='UTF-8') as f:
#     data = json.load(f)
# print(data['name'])
#
# d = {"name": "fiodar", "id": "1", "email": "example@gmail.com"}
# string_my = json.dumps(d, encure_ascii=False)
# print(string_my)
#
# d1 = {"name": "fiodar", "id": "1", "email": "example@gmail.com"}
# with open('d1.json', 'w', encoding='UTF-8') as f:
#     json.dump(d1, f, ensure_ascii=False)
# x = 1
# try:
#     x = 1
# except ArithmeticError:
#     print('ошибка')
# else:
#     print('11')
# finally:
#     print('аа')



# try:
#     a, b = int(input()), int(input())
#     c = a / b
# except ZeroDivisionError:
#     print('ошибка')
# else:
#     print(c**2)
# finally:
#     print('все ок')


try:
    a, b = int(input()), int(input())
    c = a / b
except ZeroDivisionError:
    print('ошибка 0')
except ValueError:
    print('ошибка значения')
else:
    print(c)