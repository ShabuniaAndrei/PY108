def operation(lst):
    lst_str = []  # Новый список из слов (по буквам)
    count_even = 0  # Счетчик суммы четных чисел
    count_gl = 0  # Счетчик гласных
    count_sgl = 0  # Счетчик согласных
    for elem in lst:  # Итерация по данному списку
        if type(elem) is int:  # Проверяем итерируемый объект на принадлежность к целочисленному типу
            if elem % 2 == 0:
                count_even += elem  # Добавление четного числа
            else:
                index = lst.index(elem)  # Находим индекс итерируемого значения
                lst.insert(index, 1)  # Вставляем число 1 на место нечётного числа
                lst.pop(index + 1)  # Удаляем нечётное число из списка
        else:
            lst_str.extend(elem)  # Создаёт итерируемый список из букв
    for num in lst_str:  # Итерация по новому списку
        if num == 'a' or num == 'e' or num == 'i' or num == 'o' or num == 'u' or num == 'y':
            count_gl += 1  # Добавление значения гласного
        else:
            count_sgl += 1  # Добавление значения согласного
    return count_even, lst, count_gl, count_sgl


answer = list(operation([15, 48, 'hello', 6, 19, 'world']))
print(f'Сумма четных цифр: {answer[0]}')
print(f'Замена нечётных на 1: {answer[1]}')
print(f'Количество гласных букв: {answer[2]}')
print(f'Количество согласных букв: {answer[-1]}')
