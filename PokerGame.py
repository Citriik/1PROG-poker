from Card import Card
import random

class PokerGame:
    big_blind = 10

    def __init__(self, players):
        self.players = players
        self.turn_id = 0
        self.pot = 0

    def start(self):
        # Create the cards
        self.cards = []

        for i in range(52):
            self.cards.append(Card(i % 14 + 1, i // 14))

        random.shuffle(self.cards)

        self.next_turn()

    def next_turn(self):
        playing_players = self.players
        need_big_blind = True
        need_small_blind = True
        max_bet = self.big_blind

        # Deal the cards to the players
        for player in self.players:
            player.set_cards(self.cards[:2])
            self.cards = self.cards[2:]

        # Middle cards (flop 3 first, then turn end river)
        self.flop = self.cards[:3]
        self.cards = self.cards[3:]

        self.turn = self.cards.pop()
        self.river = self.cards.pop()

        inside_turn = 0

        while(len(playing_players) >= 2 and inside_turn <= 3):
            for player in playing_players.copy():
                if inside_turn >= 1:
                    self.prin_center_card(inside_turn)
                    print('\n')
                print("\n{} c'est a vous.".format(player.name))
                print("Pot actuel: {}".format(self.pot))
                print("Vos jetons: {}".format(player.points))
                print("Vos cartes: {}".format(player.get_cards()))
                
                if need_big_blind:
                    print("Vous payez la big blind de {}".format(self.big_blind))
                    self.pot += self.big_blind
                    player.points -= self.big_blind
                    need_big_blind = False
                    continue
                
                if need_small_blind:
                    print("Vous payez la small blind de {}".format(self.big_blind // 2))
                    self.pot += self.big_blind // 2
                    player.points -= self.big_blind // 2
                    need_small_blind = False
                
                self.print_actions()
                selected_action = ''
                while selected_action == '':
                    try:
                        selected_action = int(input("\nAction choisie: "))

                        if selected_action < 1 or selected_action > 3:
                            raise Exception
                    except:
                        print("Entrez un nombre compris entre 1 et 3.")
                        selected_action = ''

                if selected_action == 1:
                    bet = max_bet if player.points >= max_bet else player.points
                    self.pot += bet
                    player.points -= bet

                elif selected_action == 2:
                    bet = 0
                    while bet == 0:
                        try:
                            bet = int(input("\nMise: "))

                            if bet <= 0:
                                print("Entrez un nombre supérieur à 0.")
                                raise Exception
                            elif bet > player.points:
                                print("Vous ne pouvez pas miser plus de jetons que vous en avez !")
                                raise Exception
                            elif bet < max_bet:
                                print("Vous ne pouvez pas miser moins que {}.".format(max_bet))
                                raise Exception
                        except:
                            bet = 0
                    
                    self.pot += bet
                    player.points -= bet

                elif selected_action == 3:
                    playing_players.remove(player)

            inside_turn += 1
        
        for player in self.players.copy():
            if player.points <= 0:
                self.players.remove(player)


    def print_actions(self):
        print("\n1: Suivre")
        print("2: Miser")
        print("3: Se coucher")

    def prin_center_card(self, inside_turn):
        if inside_turn >= 1:
            print('\nCartes au centre:')
            str_cards = []

            for card in self.flop:
                str_cards.append(str(card))

            print(', '.join(str_cards), sep='', end='')

        if inside_turn >= 2:
            print(', {}'.format(str(self.turn)), sep='', end='')

        if inside_turn >= 3:
            print(', {}'.format(str(self.river)))