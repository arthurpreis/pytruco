from card import Card
from stack import Stack

class Deck(Stack):
    def __init__(self):
        self.cards = []
        self.new_deck()

    def new_deck(self):
        for suit in range(4):
            for rank in range(0,10):
                self.cards.append(Card(suit,rank))
