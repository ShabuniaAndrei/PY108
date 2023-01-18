print('Задача 1. Покупка дома')


class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = None

    def info(self):
        return f'{self.default_name}, ' \
               f'{self.default_age},' \
               f'{self.__money}, ' \
               f'{self.__house}'

    def buy_house(self, house, discount):
        price = int(house.final_price(discount))
        if self.__money >= price:
            self.__make_deal(house, price)
            return f'ДОМ КУПЛЕН! [оставшиеся средства на счету: {self.__money}$]'
        else:
            return f'Недостаточно средств! Стоимость дома: {price}$ [оставшиеся средства на счету: {self.__money}$]'

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    @staticmethod
    def default_info():
        return f'Default name = {Human.default_name}, ' \
               f'Default age = {Human.default_age}'

    def earn_money(self, amount):
        self.__money += amount
        return f'* Зачисление на счёт {amount}$ [оставшиеся средства на счету: {self.__money}$]'


class House(Human):
    def __init__(self, area, price):
        super().__init__()
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100-discount) / 100
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    alexander = Human('Sasha', 27)
    small_house = SmallHouse(8500)
    print(alexander.buy_house(small_house, 5))
    print(alexander.earn_money(5000))
    print(alexander.buy_house(small_house, 5))
    print(alexander.earn_money(20000))
    print(alexander.buy_house(small_house, 5))

print('\nЗадача 2. Сбор урожая')


class Tomato:
    states = ['Проростание', 'Зачатки цветов', 'Зелёный плод', 'Бурый плод']

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        self._state = self.states[self.states.index(self._state) + 1]
        print(f'Tomato_{self._index} в стадии "{self._state}"')

    def is_ripe(self):
        if self._state == self.states[-1]:
            return True
        return False


class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(index) for index in range(1, amount+1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                return True
            return False

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f'{40*"="}\nРабота садовника....')
        self._plant.grow_all()
        return f'Работа завершена.\n{40*"="}'

    def harvest(self):
        print(f'Пробуем собрать урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            return f'Сбор урожая'
        else:
            return f'Плоды не созрели!'

    @staticmethod
    def knowledge_base():
        return f"{90*'-'}\n Справка по cадоводству: \n    Томаты имеют четыре стадии созревания. Сбор уражая возможен\
 только в последней стадии. \n    Если томаты не созрели пользуйтесь работой садовника. \n{90*'-'}"


if __name__ == '__main__':
    print(Gardener.knowledge_base())

    tomato_bush = TomatoBush(5)
    gardener = Gardener('Николай', tomato_bush)

    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.harvest())
    print(gardener.work())
    print(gardener.harvest())
