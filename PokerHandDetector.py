class PokerHandDetector:
    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(key=lambda x: x.value)
    
    def get_hand(self):
        hand = ''

        # One pair
        if self.has_same_cards(2, 1):
            hand = 'pair'
        
        # Two pair
        if self.has_same_cards(2, 2):
            hand = 'twopair'
        
        # Three of a kind
        if self.has_same_cards(3, 1):
            hand = 'threeofakind'
        
        straight_cards = self.get_straight()
        # Straight
        if len(straight_cards) > 0:
            hand = 'straight'
        
        # Flush
        if self.is_flush(self.cards):
            hand = 'flush'
        
        # Full House
        if self.has_same_cards(2, 1) and self.has_same_cards(3, 1):
            hand = 'fullhouse'
        
        # Four of a kind
        if self.has_same_cards(4, 1):
            hand = 'fourofakind'
        
        # Straight Flush
        if len(straight_cards) > 0 and self.is_flush(straight_cards):
            card_values = list(map(lambda x: x.value, straight_cards))

            # Royal Flush
            if 14 in card_values:
                hand = 'royalflush'
            else:
                hand = 'straightflush'

        return hand

    def has_same_cards(self, number_of_cards, number_of_time):
        found = 0
        card_values = list(map(lambda x: x.value, self.cards))

        for card in set(card_values):
            if card_values.count(card) == number_of_cards:
                found += 1
        
        return found == number_of_time

    def is_flush(self, cards):
        card_types = list(map(lambda x: x.type, cards))

        for i in range(4):
            if card_types.count(i) >= 5:
                return True
        
        return False

    def get_straight(self):
        card_values = list(map(lambda x: x.value, self.cards))

        count = 0

        for i in range(len(card_values)):
            if card_values[i] + 1 == card_values[i + 1]:
                count += 1

            if count == 4:
                return self.cards[i - 3:i + 2]

            if card_values[i] + 1 != card_values[i + 1] and i >= 2:
                return []