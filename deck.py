import random
from pprint import pprint

class Deck():

    def __init__(self):
        self.values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.ranks =  ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.suits= ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.cards = [(x,) + y for x in self.suits for y in zip(self.ranks, self.values)]

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def pick_a_card(self):
        return self.cards.pop()



