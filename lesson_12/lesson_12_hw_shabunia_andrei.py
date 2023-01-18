
def operation(values):
    if type(values) == tuple:
        def count_word():   # подсчет количества длины слов в кортеже
            count_word_len = 0  # счетчик длинны слов
            for value in values:  # итерация по кортежу
                if type(value) == str:  # убираем другие типы данных
                    for let in value:  # итерация по элементу кортежа
                        if let.isalpha():
                            count_word_len += 1
            return f'Длина всех слов кортежа: {count_word_len}'
        return count_word()
    elif type(values) == list:
        def count_alpha_digit():  # подсчет количества букв, цифр и чисел
            count_alpha = 0  # счетчик букв
            count_dig = 0  # счетчик цифр
            count_numb = 0  # счетчик чисел
            for val in values:  # итерация по списку
                if type(val) == str or type(val) == int or type(val) == float:  # убираем другие типы из списка
                    for elem in str(val):  # итерация по элементу списка
                        if elem.isalpha():
                            count_alpha += 1
                        elif elem.isdigit():
                            count_dig += 1
                    if type(val) != str:  # оставляем тип int и float
                        count_numb += 1
            return f'Количество элементов в списке:  {count_alpha} букв(а), {count_dig} цифр(а) и {count_numb} числа(о)'
        return count_alpha_digit()
    elif type(values) == int or type(values) == float:
        def count_odd_digit():  # подсчет количетва нечётных цифр в числе
            count_odd = 0  # счетчик нечетных цифр
            for num in range(len(str(values))):
                if str(values)[num] == '.':   # обработка '.' если число float
                    continue
                elif int(str(values)[num]) % 2 != 0:
                    count_odd += 1
            return f'Количество нечётных цифр в числе: {count_odd}'
        return count_odd_digit()
    elif type(values) == str:
        def count_letters():  # подсчет количетва букв в строке
            count_letter = 0  # счетчик букв
            for val in values:  # итерация по строке
                if val.isalpha():
                    count_letter += 1
            return f'Количество букв в строке: {count_letter}'
        return count_letters()
    else:
        return 'Вы передали в функцию неверный тип данных'   # при передаче в функцую иного типа данных


entered_data = [True, 'Hello Python!', False, 434, 'Привет_98', 4.4]    # передаваемый тип данных
print(operation(entered_data))
