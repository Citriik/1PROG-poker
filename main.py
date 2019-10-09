from PokerGame import PokerGame
from Player import Player
from Card import Card
from PokerHandDetector import PokerHandDetector

def main():
    players = []

    # Create the 5 players
    for i in range(5):
        player_name = ''

        while player_name == '':
            player_name = input('Nom du jour {}: '.format(i + 1))

        players.append(Player(player_name))
    
    # Create and start the game
    poker_game = PokerGame(players)

    poker_game.start()

if __name__ == '__main__':
    main()