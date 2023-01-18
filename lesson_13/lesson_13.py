# val = 5
# def func():
#     val = 15
#     print(val, end=" ")\
#
# func()
# print(val)

# l = ['a']
# l.extend('abc')
# print(l)
#
# s = 'ab c\nde fg\rkl\r\n'
# print(s.split(), s.splitlines())

# f = open('example.txt', 'r')
# print(f)
# print(*f)
# f.close()

# with open('example.txt', 'r') as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readlines())
import os
# with open('new_file.txt', 'w') as f:
#     print(f)
#     f.write('Hello my friend')
#
# os.rename('new_file.txt', 'my_new_file.txt')

# print(f'Current catalog is {os.getcwd()}')
# print(f'Make directory {os.mkdir("New_DIR")}')
# print(f'{os.chdir("New_DIR")}')
# print(f'{os.mkdir("New_DIR2")}')
# print(f'{os.rmdir("New_DIR")}')
# print(f'{os.remove("new_file.txt")}')

# with open('example.txt') as f:
#     # st = f.readlines()[0].replace('_', ' ').split()
#     st = f.readlines()
#     print(st)
#     st = st[0]
#     print(st)
#     st = st.replace('_', ' ')
#     print(st)
#     st = st.split()
#     print(st)
#     sum_digit = 0
#     for i in st:
#         if i.isdigit():
#             sum_digit += int(i)
#     print(sum_digit)
#
#
# with open('example.txt') as f:
#     num_list = []
#     world_list = []
#     st = f.readlines()
#     print(st)
#     for i in st:
#         elem = i.strip()
#         print(elem)
#         if elem.isalpha():
#             world_list.append(elem)
#         elif elem.isdigit():
#             num_list.append(int(elem))
#     num_list = sorted(num_list)
#     world_list = sorted(world_list)
#     print(num_list + world_list)

# f_name = input('введи имя файла')
# f = open(f_name, 'w')
# while True:
#     my = input('Введи')
#     if my == ' ':
#         break
#     f.write(my + '\n')
# f.close()
