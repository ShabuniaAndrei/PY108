print(145*'-')
print('Задача №1 (Перемножить все нечётные значения от 1 до 30)')
total = 1
for i in range(1, 31):
    if i % 2 != 0:
        total *= i
print(f'ответ: {total}')
print(145*'-')
print('Задача №2 (Записать в массив все числа в диапазоне от 1 до 100 кратные 5)')
multiple_5 = []
for i in range(1, 101):
    if i % 5 == 0:
        multiple_5.append(i)
print(f'ответ: {multiple_5}')
print(145*'-')
print('Задача №3 (Вывести на экран все четные значения в диапазоне от 1 до 71)')
even_numbers = []
for i in range(1, 72):
    if i % 2 == 0:
        even_numbers.append(i)
print(f'ответ: {even_numbers}')
print(145*'-')
print('Задача №4 (Новый массив из элементов встречающихся более двух раз)')
list_1 = [int(number) for number in input('Введите массив чисел через пробел: ').split()]  # Задача 4
print(f'Введенный массив: {list_1}')
list_new = []
for number in list_1:
    if list_1.count(number) > 2:
        list_new.append(number)
        while list_new.count(number) > 1:
            list_new.remove(number)
print(f'ответ: {list_new}')
print(145*'-')