# str = 'shcool'
# print(str.find('hcl'))  # если не находит то -1
# str.get('k', str['k'] == None)

# class House:
#     def build(self):
#         pass
#
#     def destroy(self):
#         pass
#
#
# house_item = House()
# print(dir(House))
#
#
# def phone():
#     def_color = 'RED'
#     def_model = 'F100'
#
#     def turn(self):
#         pass
#
#     def call(self):
#         pass
#
#
# class My_Phone:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model


# class Example:
#     a = 1
#     b = 2
#
#     def __init__(self, a_din, b_din):
#         self.a_din = a_din
#         self.b_din = b_din
#
#     def add(self):
#         self.property = 5
#         print(self.property)
#
#     def func_2(self):
#         return self.a + self.b
#
#     def func_deg(self):
#         return self.a ** self.b
#
#
# ex = Example(6, 4)
# print(ex.func_deg(), 3**4)
# print(ex.func_2())


class Calculator:
    # def add_values(self):
    #     self.a = float(input('enter a'))
    #     self.b = float(input('enter b'))

    def __init__(self):
        # self.add_values()
        self.a = float(input('enter a: '))
        self.b = float(input('enter b: '))

    def num_pl(self):
        return self.a + self.b

    def num_mi(self):
        return self.a - self.b

    def num_umn(self):
        return self.a * self.b

    def num_del(self):
        try:
            res = self.a / self.b
            return res
        except ZeroDivisionError:
            return 'Ошибка'


calc = Calculator()     # создали экземпляр класса

x = input('enter +, -, *, /: ')
if x == '+':
    print(calc.num_pl())
elif x == '-':
    print(calc.num_mi())
elif x == '*':
    print(calc.num_umn())
elif x == '/':
    print(calc.num_del())
else:
    print('вы ввели не то')

# переменная = свойства,  функция = метод
