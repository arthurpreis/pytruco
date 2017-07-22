import random

class Card():
    
    #truco
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["4", "5", "6", "7", "Queen", "Jack", "King", "Ace",
        "2", "3"]
        
    def __init__(self, suit=0, rank=0):        
        self.suit = suit
        self.rank = rank
        
        #TODO: criterio de visibilidade
    
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
        #TODO: localizacao pt-br
        
    def __cmp__(self, other):
        if self.rank > other.rank: 
            return 1
        if self.rank < other.rank: 
            return -1
                
        if self.suit > other.suit: 
            return 1
        if self.suit < other.suit: 
            return -1
                    
        return 0
        
    def get_rank(self):
        return self.rank
        
    def get_suit(self):
        return self.suit
        
class Deck(Card):
    def __init__(self, game_mode=''):
        self.cards = []
        self.game = game_mode
        if (self.game == ''):
            for suit in range(4):
                for rank in range(0, 13):
                    self.cards.append(Card(suit, rank))
        elif (self.game == 'truco'):
            for suit in range(4):
                for rank in range(0,10):
                    self.cards.append(Card(suit,rank))
    
    def __str__(self):
        if self.is_empty():
            print('is empty')
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s
    
    def print_deck(self):
        for card in self.cards:
            print(card)            

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() #comprar carta
    
    def is_empty(self):
        return (len(self.cards) == 0)
    
    def add_card(self, cards):
        self.deck.append(cards)
        
    def deal(self, hand, num_cards=3):
        for i in range(num_cards):
            if self.is_empty(): 
                break   # break if out of cards
            card = self.draw()           # take the top card
            hand.append(card)              # add the card to the hand
        #TODO: juntar com a funcao draw e coloque parametro de n de cartas
    
class Hand(Deck):
    
    def __init__(self, name=""):
       self.cards = []
       self.name = name
    
    def add(self,card):
        self.cards.append(card)
        
    def draw_card(self,deck):
        card = deck.draw()
        self.cards.append(card)
        
