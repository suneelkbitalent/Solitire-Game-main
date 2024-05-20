from Deck import Deck
from Card import Card
from stack import Stack
from solitire import Solitire
from tableau import Tableau

class Interface:
# initialization 

    def __init__(self):
        self.d = Deck()
        self.t = Tableau([self.d.Dcard(x) for x in range(1, 8)])
        self.f = Solitire()
        self.sw = Stack(self.d.Dcard(24))
#main manu
    def menu(self):
        print("*******************************@@@@@@@")
        print("Welcome to Our Pro Solitaire!\n")
        print("@@@@@@@*******************************")
        print("Instructions are :")
        print("\twd - Move a card from waste to Deck")
        print("\ttf #T - Move a card from table to Deck")
        print("\tmove – Move a card to the waste pile")
        print("\twt #T - Move a card from waste to table")
        print("\ttt #T1 #T2 - Move a card from one table column to another")
        print("\th - Help")
        print("\tq - Quit")
        print("**********************************")
        print("\nNOTE: This deck contains red Hearts/Diamonds and black Spades/Clubs.\n")

# Displaying the current state of game.

    def game_display(self):
        print("Waste\t\t\tStock\t\t\t\tDeck")
        print("{}\t{}\t\t{}\t{}\t{}\t{}".format(
            self.sw.GetW(), self.sw.AddStock(),
            self.f.Receive_card("club"), self.f.Receive_card("heart"),
            self.f.Receive_card("spade"), self.f.Receive_card("diamond")))
        print("\nColumns \n \t1\t2\t3\t4\t5\t6\t7\n")

        for x in range(self.t.LenPile()):
            print_str = ""
            for col in range(7):
                HCards = self.t.HiddenCards[col]
                shown_cards = self.t.ShowedCards[col]
                if len(HCards) > x:
                    print_str += "\tx"
                elif len(shown_cards) + len(HCards) > x:
                    print_str += "\t" + str(shown_cards[x - len(HCards)])
                else:
                    print_str += "\t"
            print(print_str)

# run the game, take input and do corresponding action 

    def run_game(self):
        self.menu()
        self.game_display()

        while not self.f.WinCondition():
            input_user = input("Enter a input or type 'h' for help: ").lower().replace(" ", "")

            if input_user == "q":
                print("Game is exited.")
                break
 
            elif input_user == "h":
                self.menu()
            
            elif input_user == "move":
                if self.sw.Wstock():
                    self.game_display()
            elif input_user == "wd":
                if self.f.PileCards(self.sw.GetW()):
                    self.sw.WasteCardPop()
                    self.game_display()
                else:
                    print("Sorry, you can't move a card from waste to Deck.")
            elif "wt" in input_user and len(command) == 3:
                col = int(command[-1]) - 1
                if self.t.StackTotable(self.sw, col):
                    self.game_display()
                else:
                    print("Sorry, you can't move a card from waste to tableau column.")
            elif "tf" in input_user and len(command) == 3:
                col = int(command[-1]) - 1
                if self.t.ColToStack(self.f, col):
                    self.game_display()
                else:
                    print("Sorry, you can't move a card from the tableau column to the Deck.")
            elif "tt" in input_user and len(command) == 4:
                c1, c2 = int(command[-2]) - 1, int(command[-1]) - 1
                if self.t.ColToCol(c1, c2):
                    self.game_display()
                else:
                    print("Sorry, you can't move a card from that tableau column.")
            else:
                print("Invalid command! Please enter a valid command.")

        if self.f.WinCondition():
            print("Congratulations! You won!")


