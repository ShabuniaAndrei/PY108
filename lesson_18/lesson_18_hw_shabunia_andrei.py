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
        print(f'{40*"="}\nРабота садовника ....')
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
