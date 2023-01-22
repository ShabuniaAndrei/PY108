from functools import reduce
print(130 * "-")
'''
Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя 
(вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
После этого выводится результат её выполнения.
Доп условие: 
Входящее значение - кортеж состоящий из: str, вложенными списками из чисел int, float и другими элементами.
Если элемент str => вывести список состоящий из слов с длинной букв меньше 4 в алфавитном порядке.
Если элемент явл. списком состоящим только из чисел int => перемножить их между собой, вывести результат.
Если элемент явл. списком состоящим только из чисел float => округлить числа до десятых, результат вывести списком.
При ином значении типа элемента обработать ошибку некорректного значения.
'''


def debug(func):
    def wrapper(*args):
        print(f'Имя функции: "{func.__name__}", Передаваемые аргументы: {list(args)}'
              f'\nЗначение которое возвращает функция: {(func(*args))}\n{130 * "-"}')
        func(*args)
    return wrapper


@debug
def filter_words(*args):  # вывод слов с длинной букв менее 4ти в алфавитном порядке
    return list(filter(lambda num: len(num) < 5, sorted(str(*args).split())))


@debug
def multiply_numbers(*args):  # умножение чисел
    return reduce(lambda a, b: a * b, args)


@debug
def rounding_numbers(*args):  # округление до десятых значений чисел
    return list(map(lambda x: round(x, 1), args))


input_value = ([2, 3, 4, 5], 5, (4, 5, 6), 'Который при каждом вызове функции выводит её имя со всеми аргументами',
               [9.77, 2.165, 8.88, 4.595], {'Hi', 'Python'}, True, [9.77, '2.165', 8.88, 4.595])

for value in input_value:
    try:
        if isinstance(value, str):
            filter_words(value)
        else:
            if all(type(i) is int for i in value) and type(value) == list:
                multiply_numbers(*value)
            elif all(type(i) is float for i in value) and type(value) == list:
                rounding_numbers(*value)
            else:
                print(f'{value} - Некорректное значение элемента\n{130 * "-"}')
    except TypeError:
        print(f'"{value}" - Некорректное значение элемента\n{130 * "-"}')
