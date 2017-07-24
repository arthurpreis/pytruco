import random

class Card():
    
    #truco
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["4", "5", "6", "7", "Queen", "Jack", "King", "Ace",
        "2", "3"]
        
    def __init__(self, suit=0, rank=0):        
        self.suit = suit
        self.rank = rank      
 
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
                
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

    #======== comparações por naipe ========    
    def suit_gt(self, other):
        if self.suit > other.suit: 
            return True
        else:
            return False
            
    def suit_lt(self, other):
        if self.suit < other.suit: 
            return True
        else:
            return False
    
    def suit_eq(self, other):
        if self.suit == other.suit: 
            return True
        else:
            return False       
    
    def suit_neq(self, other):
        if self.suit != other.suit: 
            return True
        else:
            return False                 
    #================================
    
    #=======comparações por valor======
    def rank_gt(self, other):
        if self.rank > other.rank: 
            return True
        else:
            return False
            
    def rank_lt(self, other):
        if self.rank < other.rank: 
            return True
        else:
            return False
    
    def rank_eq(self, other):
        if self.rank == other.rank: 
            return True
        else:
            return False       
    
    def rank_neq(self, other):
        if self.rank != other.rank: 
            return True
        else:
            return False     
    
        
     #TODO: criterio de visibilidade
     #TODO: localizacao pt-br
 
 
 #================ STACK =======================
 # Hand (player), Deck e mesa vao herdar       
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
        
class Deck(Stack):
    def __init__(self):
        self.cards = []
        self.new_deck()
    
    def new_deck(self):
        for suit in range(4):
            for rank in range(0,10):
                self.cards.append(Card(suit,rank))
