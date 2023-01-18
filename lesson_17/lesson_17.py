# class Car:
#
#     def __str__(self):
#         return 'This is Car'
#
#     def star(self):
#         print('запуск')
#
#
# car_a = Car()
# print(car_a)
# print(car_a.__str__())
import string


# class Phone:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('my operator MTS')
#
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#
#     @classmethodmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'Toy_phone')
#             return None
#
#
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')
# my_phone.toy_phone('I785')
# my_phone.model_hash('I785')


# class Human:
#
#     default_name = 'Andrei'
#     default_age = 34
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 1000
#         self.__house = 2
#
#     def info(self):
#         return f'{self.default_name}, ' \
#                f'{self.default_age},' \
#                f'{self.__money}, ' \
#                f'{self.__house}'
#     @staticmethod
#     def default_info():
#         return f'Default name = {Human.default_name}, ' \
#                f'Default age = {Human.default_age}'
#
#     def earn_money(self, salary):
#         self.__money += salary
#         return f'Im {salary}, now budget {self.__money}'
#
#
# print(f'1) {Human.default_info()}')
# max = Human('Maxim', 49)
# print(f'3) {max.earn_money(100)}')
# print(f'3) {max.earn_money(500)}')
# print(f'4 {max.default_info()}')
# #
# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     "пользовательский метод. Вкл. телефон"
#
#     def turn_on(self):
#         self.is_on = True
#
#     """Звонит телефон, если он включен"""
#
#     def call(self):
#         if self.is_on:
#             return f'Calling...'
#
#
# # Подкласс. Унаследованный от родительского
# class MobilePhone(Phone):
#     # добавим новое свойство
#     def __init__(self):
#         super().__init__()
#         metod = self.is_on
#         self.battery = 0
#
#     "пользовательский метод"
#
#     def charge(self, pr):
#         self.battery += pr
#         return f"charging battery {pr}. All battery = {self.battery}"
#
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))
#


# class Camera:
#     def camera(self):
#         pass
#
#
# class Radio:
#     def radio(self):
#         pass
#
#
# class Phone(Camera, Radio):    #наследование идет горизонтально
#     def phone(self):
#         pass
#
#
# print(Phone().__dir__())


# class House():
#
#     def __init__(self, _area, _price):
#         self._area = _area
#         self._price = _price
#
#     def final_price(self, discount, price):
#         final_price = self.price * (100-dis)
#         return dis, final_price
#
# class SmallHouse(House):
#
#     def __init__(self):
#         object = 40


# class Car:
#     def __init__(self, model):
#         self.model = model
#
#         @property
#         def model(self):
#             return self.__model
#
#         @model.setter
#         def model(self, model):
#             if model < 2000:
#                 self.__model = 2000
#             elif model > 2018:
#                 self.__model = 2018
#             else:
#                 self.__model = model
#
#         get getCarModel(self):
#         return f'год {self.model}'
#
# car1 = Car()
# print(car1)

# class Alphabet:
#
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print(self):
#         print(self.letters)
#
#     def letters_num(self):
#         return len(self.letters)
#
#
# class EngAlphabet(Alphabet):
#
#     __letters_num = 0
#
#     def __init__(self):
#         super().__init__('EN', string.ascii_letters)
#
#     def is_en_letter(self, letter):
#         if letter in self.letters:
#             return f'{letter} from ENG Alphabet'
#         return f'{letter} not from ENG Alphabet'
#
#     def letters_num(self):
#         return EngAlphabet.__letters_num
#
#     @staticmethod
#     def example():
#         return f'Hello!'
#
#
# eng_alphabet = EngAlphabet()
# eng_alphabet.print()
# print(eng_alphabet.letters_num())
# print(eng_alphabet.is_en_letter('Q'))
# print(eng_alphabet.is_en_letter('Ф'))

