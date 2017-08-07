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
