print('Задача 1:')
numbers = set([i for i in range(10)])
print(f'Сумма цифр от 0 до 9 =  {sum(numbers)}')

print('Задача 2:')
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
for i in set(long_word):
    print(f"Количество повторений символов: '{i}' : {long_word.count(i)}")

print('Задача 3:')


def week_temp(*args):
    sum_temp = sum(args)
    days = len(args)
    return int(sum_temp / days)


print(f'Средняя температура: {week_temp(26, 29, 34, 32, 28, 26, 23)}')
