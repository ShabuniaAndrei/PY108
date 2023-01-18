import math
apple_ann = 2 #Задача №1
apple_pol = 5
print("Количество яблок у Анны: {}, Количество яблок у Пола: {}" .format(apple_ann,apple_pol))
print()

lenght = int(input("Введите длину ребра куба: ")) #Задача №2 решение 1
V_cube = lenght**3
S_cube = 4*lenght**2
print(f"Объём куба равен: {V_cube}")
print(f"Площадь боковой поверхности куба: {S_cube}")
print()

lenght = int(input("Введите длину ребра куба: ")) #Задача №2 решение 2
print(f"Объём куба равен: {math.pow(lenght,3)}")
print(f"Площадь боковой поверхности куба: {4*math.pow(lenght,2)}")
print()

day=(2-1)*19 #Задача №3
print("Количество потребовавшихся дней улитке: " +str(day))