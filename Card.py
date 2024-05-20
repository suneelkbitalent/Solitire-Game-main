class Card():
# create a class_list which is representing how the mapping of cards done, where 2-10 are integer and them we have ace, king, queen and jack.
    card_list = {i: str(i) if i>=2 and i <= 10 else {1: "Ace" , 11: "Jack", 12: "Queen", 13: "King"}.get(i, "Unknown") for i in range(1, 14)}

# constructor method of card class
 
   def __init__(self, val, suit):
        self.name = self.CName[val]
        self.suit = suit
        self.title = "%s%s" % (self.name, self.suit)
        self.val = val

# This method is checking if the current card is one less than the given card.

    def ISBelow_True(self, card):
        temp = card.val - 1
        return self.val == temp

# This method is checking if the current card can be attached to the given card.

    def Attach(self, card):
        return card.ISBelow_True(self) and card.ISRightSuit(self)

# This method is checking if the current card has the right suit compared to the given card.

    def ISRightSuit(self, card):
        black_suits = {"club", "spade"}
        red_suits = {"heart", "diamond"}

        return (self.suit in black_suits and card.suit in red_suits) or \
            (self.suit in red_suits and card.suit in black_suits)



    def __str__(self):
        return self.title

# Method to display the suit and value of the card.

    def show(self):
        return self.suit,self.val
