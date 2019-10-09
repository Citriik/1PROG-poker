class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.points = 300

    def set_cards(self, cards):
        self.cards = cards

    def __str__(self):
        return '{}: {}'.format(self.name, self.get_cards())

    def get_cards(self):
        str_cards = []

        for card in self.cards:
            str_cards.append(str(card))

        return ', '.join(str_cards)