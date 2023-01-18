import math
print('Задача 1: По двум введенным пользователем катетам вычислить длину гипотенузы')
a, b = int(input('Введите длину первого катета: ')), int(input('Введите длину второго катета: '))
print(f'Ответ: {math.sqrt(a**2+b**2)}')
print()
print('Задача 2: Вводятся три разных числа. Найти какое из низ является средним')
a, b, c = int(input('Введите первое: ')), int(input('Введите второе: ')), int(input('Введите третье: '))
if a > b > c or c > b > a:
    print(f'Ответ: Cреднее число: {b}')
elif b > c > a or a > c > b:
    print(f'Ответ: Cреднее число: {c}')
elif b > a > c or c > a > b:
    print(f'Ответ: Cреднее число: {a}')
else:
    print('Ошибка сравнения')
print()
print('Задача 3: Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести  нечетное')
a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
if a % 2 == 0:
    if b % 2 == 0:
        print(f'Ответ: оба четные')
    else:
        print(f'Ответ: {a} - четное, {b} - нечетное')
elif b % 2 == 0 and a % 2 != 0:
        print(f'Ответ: {b} - четное, {a} - нечетное')
else:
    print(f'Ответ: оба нечетные')
print()
print('Задача 4: Сформировать из введеного числа обратное по порядку входящих в него цифр и вывести')
number = input('Введите число: ')
print(f'Ответ: {number[::-1]}')
print()
print('Задача 5: Найти площади прямоугольника, треугольника или круга')
figure = input('Выберите фигуру (прямоугольник, треугольник, круг): ')
figure = figure.lower()
if figure == 'круг':
    radius = int(input('Введите радиус круга: '))
    print(f'Площадь круга равна: {math.pi*radius**2}')
elif figure == 'треугольник':
    side_1 = int(input('Введите длинну стороны a: '))
    side_2 = int(input('Введите длинну стороны b: '))
    side_3 = int(input('Введите длинну стороны c: '))
    p = 1/2*(side_1+side_2+side_3)  #полупериметр треугольника
    print(f'Площадь треугольника равна: {math.sqrt(p*(p-side_1)*(p-side_2)*(p-side_3))}')
elif figure == 'прямоугольник':
    side_1 = int(input('Введите длинну стороны a: '))
    side_2 = int(input('Введите длинну стороны b: '))
    print(f'Площадь треугольника равна: {side_1*side_2}')
else:
    print('Вы ввели неверную фигуру')
print()
print('Задача 6: Определить существование треугольника по трем сторонам')
ab, bc, ca = int(input("Введите AB: ")), int(input("Введите BC: ")), int(input("Введите CA: "))
if ab + bc > ca and ab + ca > bc and bc + ca > ab:
    print("Ответ: Треугольник существует")
else:
    print("Ответ: Треугольник не существует")
print()
print('Задача 7: Принадлежит ли точка кругу')
coordinate_x = int(input('Введите значение координаты по оси X: '))
coordinate_y = int(input('Введите значение координаты по оси Y: '))
radius = int(input('Введите радиус круга: '))
if radius > math.sqrt(coordinate_x**2+coordinate_y**2):
    print('Точка принадлежит кругу')
else:
    print('Точка не принадлежит кругу')
print()
print('Задача 8: Вводится строка, состаящая из слов, разделенных пробелами. Посчитать количество слов в ней')
string = input('Введите строку: ')
lst = []
for word in string:
    lst = string.split()
print(f'Ответ: {len(lst)}')
print()
print('Задача 9: Введите строку которая состоит из букв разных регистров. Нужно очистить от заглавных букв')
string = input('Введите строку: ')
print(f'Ответ: {string.lower()}')
print()
print('Задача 10: Введите программу, которая выводит числа от 0 о 100 пропуская числа, кратные 7')
print('Ответ: ')
for i in range(101):
    if i % 7 != 0 or i == 0:
        print(i, end=' ')
print()
print()
print('Задача 11: Найти сумму ряда чисел от 1 до 100')
count = 0
for i in range(1, 101):
    count += i
print(f'Ответ: {count}')
print()
print('Задача 12: Найти факториал числа n')
n = int(input('Введите число: '))
cont = 1
for i in range(2, n+1):
    cont *= i
print(f'Ответ: {cont}')
print()
print('Задача 14: Найти пересечения в 2 списках и записать в 3 список эти пересечения')
l1 = [1, 'Привет', True, 'he4', 23, 2]
l2 = [5, 23, False, 'Привет', 2, 2]
l3 = []
for elem_1 in l1:
    if elem_1 in l3:
        continue
    for elem_2 in l2:
        if elem_1 == elem_2:
            l3.append(elem_1)
            break
print(f'Ответ: {l3}')
print()
print('Задача 15: Дан список с фамилиями. Пользователь вводит фамилию. Если есть в списке - удалить, если нет: "Такой фамилии не обнаружено"')
lst_surname = ['Иванов', 'Петров', 'Сидоров']
print(f'Текущий список: {lst_surname}')
surname = input('Введите фамилию: ')
if surname in lst_surname:
    lst_surname.remove(surname)
    print(f'Отредактированный список: {lst_surname}')
else:
    print('Такой фамилии не обнаружено')
