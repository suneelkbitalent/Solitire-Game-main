import random
from Card import Card

class Deck():

# Class variable representing a deck of 52 cards, each represented by a tuple.

    Deck_list = [(card, suit) for suit in ["club", "diamond", "heart", "spade"] for card in range(1, 14)]


#Constructor

    def __init__(self, num_Card_decks=1):
        self.Deck = self.Deck_list * 
        random.shuffle(self.Deck)

# Method to deal a specified number of cards from the deck.

    def Dcard(self, Cards_n):
        dealt_cards = []
        for x in range(Cards_n):
            if self.Deck:
                dealt_cards.append(self.Deck.pop())
            else:
                break
        return dealt_cards

# Method to reveal and remove the top card from the deck.

    def ShowCardsFlip(self):
       return self.Deck.pop()

# String representation of the Deck object.

    def __str__(self):
       return str(self.Deck)

# Method to show the Card objects. 

    def show(self):
        print(Card.show())
