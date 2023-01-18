import random
print("Задача №1 Лотерея")
lucky_num = int(input('Введите счастливый номер от 1 до 5 : '))
print(f"Ваш номер равен: {lucky_num}")
roulette = random.randint(1, 5)
print(f"Призвой номер: {roulette}")
if roulette == lucky_num:
    print(f"!!!Поздравляем, вы выйграли 1млн$!!!")
elif roulette != lucky_num and 1 <= lucky_num <= 5:
    print(f"Попробуйте вашу удачу в следующий раз!")
else:
    print(f"Вы ввели некорректное число")
print()

print("Задача №2 Знаки зодиака")
date_day = int(input('Введите день рождения: '))
date_mounth = int(input('Введите месяц рождения: '))
if 21 <= date_day <= 31 and date_mounth == 3 or 1 <= date_day <= 19 and date_mounth == 4:
    print('Вы Овен')
elif 20 <= date_day <= 30 and date_mounth == 4 or 1 <= date_day <= 20 and date_mounth == 5:
    print('Вы Телец')
elif 21 <= date_day <= 31 and date_mounth == 5 or 1 <= date_day <= 20 and date_mounth == 6:
    print('Вы Близнецы')
elif 21 <= date_day <= 30 and date_mounth == 6 or 1 <= date_day <= 22 and date_mounth == 7:
    print('Вы Рак')
elif 23 <= date_day <= 31 and date_mounth == 7 or 1 <= date_day <= 22 and date_mounth == 8:
    print('Вы Лев')
elif 23 <= date_day <= 31 and date_mounth == 8 or 1 <= date_day <= 22 and date_mounth == 9:
    print('Вы Дева')
elif 23 <= date_day <= 30 and date_mounth == 9 or 1 <= date_day <= 22 and date_mounth == 10:
    print('Вы Весы')
elif 23 <= date_day <= 31 and date_mounth == 10 or 1 <= date_day <= 21 and date_mounth == 11:
    print('Вы Скорпион')
elif 21 <= date_day <= 30 and date_mounth == 11 or 1 <= date_day <= 21 and date_mounth == 12:
    print('Вы Стрелец')
elif 22 <= date_day <= 31 and date_mounth == 12 or 1 <= date_day <= 19 and date_mounth == 1:
    print('Вы Козерог')
elif 20 <= date_day <= 31 and date_mounth == 1 or 1 <= date_day <= 18 and date_mounth == 2:
    print('Вы Водолей')
elif 19 <= date_day <= 28 and date_mounth == 2 or 1 <= date_day <= 20 and date_mounth == 3:
    print('Вы Рыбы')
else:
    print('Дата некорректна, попробуйте еще раз')
print()

print("Задача №3 Треугольник")
ab = int(input("Введите сторону AB: "))
bc = int(input("Введите сторону BC: "))
ca = int(input("Введите сторону CA: "))
if ab + bc > ca and ab + ca > bc and bc + ca > ab:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
print()

print("Задача №4 Калькулятор")
num_1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
num_2 = float(input("Введите второе число: "))
if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "*":
    print(num_1 * num_2)
elif operation == "/":
    print(num_1 / num_2)
else:
    print("Вы ввели некорректную операцию")
print()

print("Задача №5 Доспехи и Щит")
color_armor = input("Введите цвет доспехов (red/yellow/black): ")
color_shield = input("Введите цвет щита (red/yellow/black): ")
is_color_armor = (color_armor == "red")
is_color_shield = (color_shield == "black")
if color_armor != "red" and color_armor != "yellow" and color_armor != "black":
    print('Вы ввели некорректный цвет')
elif color_shield != "red" and color_shield != "yellow" and color_shield != "black":
    print('Вы ввели некорректный цвет')
elif not is_color_armor and is_color_shield:
    print('Подходит!! Цвет доспехов: не красный, цвет щита: чёрный')
else:
    print('Переоденься!!!')