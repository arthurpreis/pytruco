from deck import Deck
from deck import Card
from deck import Hand

deck = Deck('truco') #criar e embaralhar o baralho está ok
deck.shuffle()        
print(deck)

hand = Hand("alice") #criar uma mão p um jogador tbm
deck.deal([hand], 5) #retira cartas do baralho e vai pra mao
print(hand) 

print(deck[4]) #nao indexaveis!
print(hand[0])
