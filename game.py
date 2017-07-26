from deck import Stack
from deck import Card
from deck import Deck

class Game():
    def __init__(self):
        self.deck = Deck()
        self.mesa = Mesa()

        self.players = []
        self.players.append(Player('Player 1'))
        self.players.append(Player('Player 2'))
#        self.players.append(Player('Player 3'))
#        self.players.append(Player('Player 4'))

        self.current_player = self.players[0]
        self.winning_player = self.players[0]
        self.tento_end = False

    def print_score(self):
        for player in self.players:
            print(player.name + ' :' + str(player.score))

    def deal_cards(self):
        for player in self.players:
            player.hand.empty()

        self.deck.empty()
        self.deck.new_deck()
        self.deck.shuffle()

        for player in self.players:
            player.draw_cards(self.deck,3)

        #self.mesa.vira = self.deck.pop() #só no truco paulista
    def game_round(self):
        self.mesa.empty()
        play_count = 0
        while play_count < len(self.players):
            self.player_action(self.current_player, self.mesa, self.players)
            self.next_player()
            play_count += 1
        print('fim de rodada \n')
        self.evaluate_round()
        self.rodada += 1

    def player_action(self, player, mesa, other_players):
        print(player.name + ' cards:')
        print(str(player.hand))
        play = int(input(player.name + "'s turn:")) - 1
        if self.beats(mesa, player.hand[play]):
            for other_player in other_players:
                other_player.is_winning = False
            player.is_winning = True
            self.winning_player = player
        player.play_card(play, mesa)
        print('Mesa: ' + str(mesa))
#        print('Winning player: ' + self.winning_player.name + '\n')

    def beats(self, stack, played_card):
        if stack.is_empty():
            return True

        for card in stack:
            if played_card.rank <= card.rank:
                return False
                break
        return True

    def next_player(self):
        if self.mesa.is_empty():
            for player in self.players:
                if player.is_winning:
                    self.current_player = player

        else:
            index = self.players.index(self.current_player)
            index += 1
            index = index % len(self.players)
            self.current_player = self.players[index]

    def current_name(self):
        print(self.current_player.name)

    def evaluate_round(self):
        for player in self.players:
            if player.is_winning:
                #print(player.name + ' ganhou\n')
                if self.rodada == 0:
                    player.won_first = True
                    print(player.name + ' ganhou a 1a rodada \n')
                    self.check_end()
                elif self.rodada == 1:
                    player.won_second = True
                    print(player.name + ' ganhou a 2a rodada \n')
                    self.check_end()
                elif self.rodada == 2:
                    player.won_third = True
                    print(player.name + ' ganhou a 3a rodada \n')
                    self.check_end()
        for player in self.players:
            player.is_winning = False

    def check_end(self):
        for player in self.players:
            if player.won_first and player.won_second:
              #  print('aaaaaaaaaaaaa \n')
                self.end_tento(player)
            elif player.won_first and player.won_third:
              #  print('bbbbbbbbb \n')
                self.end_tento(player)
            elif player.won_second and player.won_third:
               # print('cccccccccc \n')
                self.end_tento(player)

    def end_tento(self, winning_player):
        self.tento_end = True
        winning_player.score += 1
        self.current_player = winning_player
        for player in self.players:
            player.reset_win_flag
        self.rodada = 0

    def game_tento(self):
        self.rodada = 0
        self.deal_cards()
        while (self.rodada <= 2) and not self.tento_end:
            print(str(self.rodada + 1)+'a rodada\n')
            self.game_round()
        self.print_score()

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

    def play_card(self, index, mesa):
        self.hand.move_card(mesa, index)

    def draw_cards(self, target, number):
        self.hand.draw_cards(target,number)

    def reset_win_flag(self):
        self.is_winning = False
        self.won_first = False
        self.won_second = False
        self.won_third = False

class Mesa(Stack):
    def __init__(self):
        #self.vira = Card()
        self.cards = []
