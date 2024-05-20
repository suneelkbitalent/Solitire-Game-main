from stack import Stack

class Solitire():

   def __init__(self):
      self.solitire_stack = {suit: [] for suit in ["club", "heart", "spade", "diamond"]}

   def PileCards(self, card):
      stack = self.solitire_stack[card.suit]

      if not stack:
         if card.val == 1:
            stack.append(card)
            return True
      elif card.val == stack[-1].val + 1:
         stack.append(card)
         return True

      return False

   def Receive_card(self, suit):
      stack = self.solitire_stack[suit]
      return suit[0].upper() if not stack else stack[-1]

   def WinCondition(self):
      for stack in self.solitire_stack.values():
         if not stack or stack[-1].val != 13:
            return False
      return True
