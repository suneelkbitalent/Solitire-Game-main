from Card import Card
from stack import Stack
from Deck import Deck
class Tableau():
   def __init__(self, card_list):
      self.HiddenCards = {}
      for x in range(7):
         self.HiddenCards[x] = card_list[x]

      self.ShowedCards= {}
      for x in range(7):
         self.ShowedCards[x] = [self.HiddenCards[x].pop()]

   def ShowCardsFlip(self, col):
      if len(self.HiddenCards[col]) > 0:
         card = self.HiddenCards[col].pop()
         self.ShowedCards[col].append(card)

   def LenPile(self):
      LenPiles = []
      for x in range(7):
         LenPiles.append(len(self.ShowedCards[x]) + len(self.HiddenCards[x]))

      max_length = max(LenPiles)
      return max_length

   def Card_T(self, cards, col):
      col_cards = self.ShowedCards[col]
      if (
            (not col_cards and cards[0].val == 13) or
            (col_cards and col_cards[-1].Attach(cards[0]))
      ):
         col_cards.extend(cards)
         return True

      return False

   def ColToCol(self, c1, c2):
      card_1 = self.ShowedCards[c1]

      for index, card in enumerate(card_1):
         CardRemain = card_1[index:]
         if self.Card_T(CardRemain , c2):
            self.ShowedCards[c1] = card_1[:index]
            if index == 0:
               self.ShowCardsFlip(c1)
            return True
      return False

   def ColToStack(self, foundation, col):
      col_cards = self.ShowedCards[col]

      if not col_cards:
         return False

      top_card = col_cards[-1]

      if foundation.PileCards(top_card):
         col_cards.pop()
         if not col_cards:
            self.ShowCardsFlip(col)
         return True

      return False

   def StackTotable(self, PWaste, col):
      card = PWaste.WasteCardPop()

      if card and self.Card_T([card], col):
         return True

      return False
