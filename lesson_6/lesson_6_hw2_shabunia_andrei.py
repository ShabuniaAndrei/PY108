lst_1 = [1, 3, 3, 3, 3, 4, 4, 8, 8, 6, 5, 5, 1, 1]
lst_new = []
for number in lst_1:
    if lst_1.count(number) > 2 and lst_new.count(number) == 0:
        lst_new.append(number)
print(f'ответ: {lst_new}')

