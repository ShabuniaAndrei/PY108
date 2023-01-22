def decorator(func):
    def wrapper():
        print('функция-оболочка', func.__name__)
        func()
    return wrapper


def basic():
    print('ОСНОВНАЯ ФУНКЦИЯ')


wrapped = decorator(basic)
print('старт программы')
# basic()
wrapped()
print('конец программы')
#
# print('**')
#
#
# @decorator
# def basic():
#     print('Основная функция')
#
#
# basic()


# def count_func(func):
#     def wr(*args, **kwargs):
#         wr.count += 1
#         res = func(*args, **kwargs)
#         print(f"{func.name} было вызвано {wr.count}")
#         return res
#
#     wr.count = 0
#     return wr
#
#
# print(str(count_func(54)))

# def bold(func):
#     def wr():
#         return "**" + func() + "**"
#     return wr
#
#
# def italic(func):
#     def wr():
#         return "//" + func() + "//"
#
#     return wr
#
#
# @bold
# @italic
# def from_tex():
#     return 'WHERE python'
#
#
# print(from_tex())


#
# def dec(func):
#     def wr(arg):
#         print('Func name', func.__name__, '()', 'with', str(arg))
#         func(arg)
#     return wr
#
#
# @dec
# def print_sqrt(num):
#     print(num**0.5)
#
# print_sqrt(4)

# def error_handler(func):
#     def wrapper(*args, **kwargs):
#         ret = 0
#         try:
#             ret = func(*args, **kwargs)
#         except:
#             print('>> Ошибка в функции', func.__name__)
#         return ret
#
#     return wrapper
#
#
# @error_handler
# def div(a, b):
#     return a / b
#
#
# div(10, 2)
# print(div(20, 9))
