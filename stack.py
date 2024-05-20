from Deck import Deck

class Stack():

   def __init__(self, cards):
      self.Deck = cards
      self.waste = []

   def AddStock(self):
      if self.Deck:
         top_card = self.Deck[-1]
         print(top_card)
         return f"{len(self.Deck)} card(s)"
      else:
         return "empty"

   def Wstock(self):
      if not self.Deck and not self.waste:
         print("Stock Pile is Empty!")
         return False
      if not self.Deck:
         self.waste.reverse()

         self.Deck = self.waste.copy()
         self.waste.clear()

      self.waste.append(self.Deck.pop())
      return True

   def GetW(self):
      return self.waste[-1] if self.waste else "empty"

   def WasteCardPop(self):
      return self.waste.pop() if self.waste else None
