from stack import Stack

class Player():
    def __init__(self, name = ''):
        self.hand = Stack()
        self.name = name
        self.score = 0
        self.round_pts = 0
        self.turn = False
        self.is_winning = False

        self.won_first = False
        self.won_second = False
        self.won_third = False

        self.has_accepted = False

    def play_card(self, index, mesa):
        self.hand.move_card(mesa, index)

    def draw_cards(self, target, number):
        self.hand.draw_cards(target,number)

    def reset_win_flag(self):
        self.is_winning = False
        self.won_first = False
        self.won_second = False
        self.won_third = False

    def won_game(self):
        if self.score >= 12:
            return True
        else:
            return False

    def print_hand(self):
        for card in self.hand:
            print(str(self.hand.index(card) + 1) + ': ' +
                str(card))

    def accept_truco(self):
        s = str(input(self.name + ', aceita Truco? \n'))

        if (s in ['s', 'S', 'y', 'Y']) :
            return True
        else:
            return False

    def trucar(self, other_players):
        for player in other_players:
            player.has_accepted = False
        self.has_accepted = True
        
        for player in other_players:
            if player.accept_truco():
                player.has_accepted = True
                print(player.name + ' aceitou \n')
            else:
                print(player.name + ' não aceitou \n')
