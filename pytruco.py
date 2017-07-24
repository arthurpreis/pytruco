from deck import Deck
from deck import Card
from deck import Stack
from game import Game
from game import Player
from game import Mesa

game = Game()
game.print_score()
#while True:
game.deal_cards()

game.start_round()
game.print_score()

game.start_round()
game.print_score()

game.start_round()
game.print_score()
