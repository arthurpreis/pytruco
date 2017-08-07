from card import Card
import random

class Stack():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, index):
        if index < len(self.cards):
            return self.cards[index]
        else:
            raise RuntimeError('card at position {0} was requested, but deck only have {1} cards!'.format(index+1, len(self.cards)))

    def __getitem__(self, index):
        # These three methods are equivalent:
        # return self.get_card(index)
        # return self.cards[index]
        return self.cards.__getitem__(index)

    def __str__(self):
        if self.is_empty():
            return 'is empty'
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s

    def is_empty(self):
        return (len(self.cards) == 0)

    def shuffle(self):
        random.shuffle(self.cards)

    def empty(self):
        self.cards = []

    def move_card(self, target, index = -1):
        card = self.cards.pop(index)
        target.add_card(card)
        #TODO: mover fatias

    def draw_cards(self, target, number):
        for i in range(number):
           self.cards.append(target.cards.pop())

    def pop(self):
        return self.cards.pop()

    def order(self, mode = 'rank'):
        if (mode == 'rank'):
            self.cards = sorted(self.cards, key=lambda card: card.rank)
        elif (mode == 'suit'):
            self.cards = sorted(self.cards, key=lambda card: card.suit)

    def index(self, obj):
        return self.cards.index(obj)
