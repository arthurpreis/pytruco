from stack import Stack
from card import Card
from deck import Deck
from player import Player

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

        self.truco_flag = False
        self.seis_flag = False
        self.nove_flag = False
        self.doze_flag = False

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
            self.current_player = self.next_player(self.current_player)
            play_count += 1
        print('fim de rodada \n')
        self.evaluate_round()
        self.rodada += 1

    def player_action(self, player, mesa, other_players):
        print(player.name + ' cards:')
        #print(str(player.hand))
        player.print_hand()
        while True:
            try:
                play = self.parse_player_input()
                break
            except InvalidInput:
                print('Invalid Input, try again')
        if self.beats(mesa, player.hand[play - 1]):
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

    def next_player(self, current_player):
        index = self.players.index(current_player)
        index += 1
        index = index % len(self.players)
        return self.players[index]

    def current_name(self):
        print(self.current_player.name)

    def evaluate_round(self):
        for player in self.players:
            if player.is_winning:
                self.current_player = player
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
        winning_player.score += self.tento_value()
        self.current_player = winning_player
        for player in self.players:
            player.reset_win_flag()
        self.rodada = 0

    def game_tento(self):
        self.rodada = 0
        self.deal_cards()
        while (self.rodada <= 2) and not self.tento_end:
            print(str(self.rodada + 1)+'a rodada\n')
            self.game_round()
        self.print_score()

    def game_mao(self):
        for player in self.players:
            if player.won_game():
                return
        self.tento_end = False
        self.game_tento()

    def tento_value(self):
        if self.truco_flag:
            return 3
        elif self.seis_flag:
            return 6
        elif self.nove_flag:
            return 9
        elif self.doze_flag:
            return 12
        else:
            return 1

    def reset_truco_flags(self):
        self.truco_flag = False
        self.seis_flag = False
        self.nove_flag = False
        self.doze_flag = False

    def parse_player_input(self):
        s = input()
        valid_inputs = ['1', '2', '3', 't', 'y', 'n', 'f', 'T', 'Y', 'N', 'F']
        if s in valid_inputs:
            #print('valid input')
            if (s == '1') or (s == '2') or (s == '3'):
                return int(s)
            else:
                return s
        else:
            #print('invalid input')
            raise InvalidInput

    def ask_truco(self):
        self.current_player.has_accepted = True
        ask_player = self.next_player(self.current_player)
        if ask_player.accept_truco():
            self.truco_flag = True
        else:
            self.end_tento(self.current_player)


class Mesa(Stack):
    def __init__(self):
        #self.vira = Card()
        self.cards = []
