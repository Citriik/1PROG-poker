CARD_VALUES = {
    1: 'As',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'Valet',
    12: 'Dame',
    13: 'Roi',
    14: 'As'
}

CARD_TYPES = {
    0: '♠️',
    1: '♣️',
    2: '♥',
    3: '♦'
}

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        return '{}{}'.format(CARD_VALUES[self.value], CARD_TYPES[self.type])

    def __repr__(self):
        return self.__str__()