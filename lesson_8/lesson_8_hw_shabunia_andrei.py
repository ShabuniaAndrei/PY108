import math
print("Задача 1: Калькулятор")


def func_1(operation=input('Введите операцию (+,-,/,*): '), num_1=float(input('Введите первое число: ')),
           num_2=float(input('Введите второе число: '))):
    if operation == '+':
        result = f'{num_1} + {num_2} = {num_1 + num_2}'
    elif operation == '-':
        result = f'{num_1} - {num_2} = {num_1 - num_2}'
    elif operation == '/' and num_2 == 0:
        result = 'Ошибка, на ноль делить нельзя'
    elif operation == '/':
        result = f'{num_1} / {num_2} = {num_1 / num_2}'
    elif operation == '*':
        result = f'{num_1} * {num_2} = {num_1 * num_2}'
    return result


print(f'Ответ: ', func_1())
print('-'*10)
print('Задача 2: Найти площади прямоугольника, треугольника или круга')


def func_2(figure=input('Выберите фигуру (прямоугольник, треугольник, круг): ')):
    if figure == 'круг':
        radius = int(input('Введите радиус круга: '))
        result_pl = f'Площадь круга: {math.pi * radius ** 2}'
    elif figure == 'треугольник':
        side_1 = int(input('Введите длинну стороны AB: '))
        side_2 = int(input('Введите длинну стороны BC: '))
        side_3 = int(input('Введите длинну стороны CD: '))
        p = 1 / 2 * (side_1 + side_2 + side_3)  # полупериметр треугольника
        result_pl = f'Площадь треугольника: {math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))}'
    elif figure == 'прямоугольник':
        side_1 = int(input('Введите длинну стороны AB: '))
        side_2 = int(input('Введите длинну стороны BC: '))
        result_pl = f'Площадь прямоугольника: {side_1 * side_2}'
    else:
        result_pl = 'Вы ввели неверную фигуру'
    return result_pl


print(func_2())
print('-'*10)
print('Задача 3: Дан список. Пользователь вводит фамилию. Если есть - удалить, если нет: "Такой фамилии не обнаружено"')


def func_3(lst_surname=['Иванов', 'Петров', 'Сидоров'], surname=input('Введите фамилию: ')):
    if surname in lst_surname:
        lst_surname.remove(surname)
        result_lst = f'Скорректированый список: {lst_surname}'
    else:
        result_lst = 'Такой фамилии не обнаружено'
    return result_lst


print(f'Ответ: ', func_3())
print('-'*10)
print('Задача 4: Вводятся три разных числа. Найти какое из низ является средним')


def func_4(num_1=int(input('Введите первое число: ')), num_2=int(input('Введите второе число: ')),
           num_3=int(input('Введите третье число: '))):
    if num_1 > num_2 > num_3 or num_3 > num_2 > num_1:
        resul_sr = f'Cреднее число: {num_2}'
    elif num_2 > num_3 > num_1 or num_1 > num_3 > num_2:
        resul_sr = f'Cреднее число: {num_3}'
    elif num_2 > num_1 > num_3 or num_3 > num_1 > num_2:
        resul_sr = f'Cреднее число: {num_1}'
    else:
        resul_sr = 'Ошибка сравнения'
    return resul_sr


print(f'Ответ: ', func_4())
print('-'*10)
print('Задача 5: Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести  нечетное')


def func_5(num_1=int(input('Введите первое: ')), num_2=int(input('Введите второе: '))):
    if num_1 % 2 == 0:
        if num_2 % 2 == 0:
            result_sr2 = f'оба четные'
        else:
            result_sr2 = f'{num_1} - четное, {num_2} - нечетное'
    elif num_2 % 2 == 0 and num_1 % 2 != 0:
        result_sr2 = f'{num_2} - четное, {num_1} - нечетное'
    else:
        result_sr2 = f'оба нечетные'
    return result_sr2


print(f'Ответ: ', func_5())
print('-'*10)
print('Задача 6: Сформировать из введеного числа обратное по порядку входящих в него цифр и вывести')


def func_6(number=input('Введите число: ')):
    result_6 = number[::-1]
    return result_6


print(f'Ответ: ', func_6())
print('-'*10)
print('Задача 7: Принадлежит ли точка кругу')


def func_7(coord_x=int(input('Введите значение по оси X: ')), coord_y=int(input('Введите значение по оси Y: ')),
           radius=int(input('Введите радиус круга: '))):
    if radius > math.sqrt(coord_x**2+coord_y**2):
        result_7 = 'Точка принадлежит кругу'
    else:
        result_7 = 'Точка не принадлежит кругу'
    return result_7


print(f'Ответ: ', func_7())
print('-'*10)
print('Задача 8: Найти факториал числа n')


def func_8(n=int(input('Введите число: '))):
    count = 1
    for i in range(2, n+1):
        count *= i
    return count


print(f'Ответ: ', func_8())
print('-'*10)
print('Задача 9: Найти сумму ряда чисел от 1 до 100')


def func_9(count=0):
    for num in range(1, 101):
        count += num
    return f'Ответ: {count}'


print(func_9())
print('-'*10)
print('Задача 10: Введите программу, которая выводит числа от 0 о 100 пропуская числа, кратные 7')


def func_10():
    lst = []
    for i in range(101):
        if i % 7 != 0 or i == 0:
            lst.append(i)
    return lst


print(f'Ответ: {func_10()}')
