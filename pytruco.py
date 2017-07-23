from deck import Deck
from deck import Card
from deck import Hand
from deck import Stack

cardA = Card(0,0)
cardB = Card(0,1)
cardC = Card(0,2)

stack1 = Stack()
stack2 = Stack()
deck = Deck()

#print('stack1: \n' + str(stack1) + '\n')
#print('stack2: \n' + str(stack2) + '\n')

stack1.add_card(cardA)
stack1.add_card(cardB)
stack1.add_card(cardC)

stack1.shuffle()
#print('stack1: \n' + str(stack1) + '\n')
#print('stack2: \n' + str(stack2) + '\n')

#stack1.move_card(stack2, 0)

#print('stack1: \n' + str(stack1) + '\n')
#print('stack2: \n' + str(stack2) + '\n')

#stack1.move_card(deck,0)

#stack1.order()

deck.shuffle()
print(str(deck))

deck.order()
print(str(deck))

deck.order('suit')
print(str(deck))
