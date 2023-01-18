# i = 1
# result = 0
# while i <= 10:
#     result = i**2
#     i = i + 1
#     print(result)

# i = 1
# res = 1
# while i < 125:
#     if i%2 ==0:
#         res = res*i
#     i = i + 1
# print(res)

# i = 0
# while i < 15:
#     print(15-i)
#     i += 1

# a = int(input())
# b = int(input())
# while a < b and a < -1:
#     print(a+1)
#     a += 1

# i = 0
# while i < 3:
#     print('i')
#     i+=1
# else:
#     print('2')

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
    if num_2 == 0:
        print("Ошибка, на ноль делить нельзя!")
    else:
        print(num_1 / num_2)
else:
    print("Ошибка, на ноль делить нельзя!")
print()
