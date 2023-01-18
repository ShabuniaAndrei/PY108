import random
number = random.randint(1, 10)
color = random.randint(1, 2)
i = 0
while i < 5:
    print(45*'-')
    print(f"У вас 5 попыток, это ваша {i+1} попытка:")
    player_number = int(input('Введите число от 1 до 10: '))
    player_color = int(input('Введите число 1(красный) или 2(чёрный): '))
    print(45*'-')
    if player_number == number and player_color == color:
        print('!! YOU WIN !!!')
        break
    else:
        print('YOU LOSE!')
        i += 1
else:
    print(45*'*')
    print(f'Правильная комбинация: {number} {color}')
    print(45*'*')