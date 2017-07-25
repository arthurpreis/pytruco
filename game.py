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
        self.players.append(Player('Player 3'))
        self.players.append(Player('Player 4'))
        self.winning_player = self.players[0]
        self.current_player = self.players[0]

        self.rodada = 0
        self.round_end = False

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
        play_count = 0
        while play_count < len(self.players):
            self.player_action(self.current_player, self.mesa, self.players)
            self.next_player()
            play_count += 1
        print('fim de rodada')
        #self.evaluate_round()

    def player_action(self, player, mesa, other_players):
        print(player.name + ' cards: \n')
        print(str(player.hand))
        play = int(input(player.name + "'s turn:")) - 1
        if self.beats(mesa, player.hand[play]):
            for other_player in other_players:
                other_player.is_winning = False
            player.is_winning = True
            self.winning_player = player
        player.play_card(play, mesa)
        print('Mesa: ' + str(mesa))
        print('Winning player: ' + self.winning_player.name)

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

    def evaluate_round():
        for player in self.players:


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
