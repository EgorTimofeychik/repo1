class CardDeck:
    def __init__(self):
        self.cards = [
            '2 Пик', '3 Пик', '4 Пик', '5 Пик', '6 Пик', '7 Пик',
            '8 Пик', '9 Пик', '10 Пик', 'Валет Пик', 'Дама Пик', 'Король Пик', 'Туз Пик',
            '2 Червей', '3 Червей', '4 Червей', '5 Червей', '6 Червей', '7 Червей',
            '8 Червей', '9 Червей', '10 Червей', 'Валет Червей', 'Дама Червей', 'Король Червей', 'Туз Червей',
            '2 Крестей', '3 Крестей', '4 Крестей', '5 Крестей', '6 Крестей', '7 Крестей',
            '8 Крестей', '9 Крестей', '10 Крестей', 'Валет Крестей', 'Дама Крестей', 'Король Крестей', 'Туз Крестей',
            '2 Бубей', '3 Бубей', '4 Бубей', '5 Бубей', '6 Бубей', '7 Бубей',
            '8 Бубей', '9 Бубей', '10 Бубей', 'Валет Бубей', 'Дама Бубей', 'Король Бубей', 'Туз Бубей'
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        card = self.cards[self.index]
        self.index += 1
        return card


deck = CardDeck()
for card in deck:
    print(card)