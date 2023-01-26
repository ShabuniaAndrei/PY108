class Card_Deck:

    def __iter__(self):
        self.count = 0
        return self

    def __init__(self):
        self.card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Kороль', 'Туз']
        self.suit = [' Пик', ' Треф', ' Бубен', ' Червей']

    def __next__(self):
        if self.count < 52:
            self.name = self.card[self.count % 13]+self.suit[self.count//13]
            self.count += 1
            return self.name
        else:
            raise StopIteration


card_iterator = Card_Deck()
element = iter(card_iterator)

try:
    for i in range(53):
        print(next(element))
except StopIteration:
    print('StopIteration')