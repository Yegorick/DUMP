from tkinter import Tk, Button, LEFT, CENTER, NW
from PIL import ImageTk

from hands import *
from game import new_game
from table import Table

class App(Tk):
    def __init__(self, cards: list = None) -> None:
        super().__init__()
        


pl_hand, comp_hand = new_game()

window = App()

computer = PCHand(comp_hand, img="back")
table = Table(800, 300, "brown", computer)
player = Hand(pl_hand, table)

table.pl = player

computer.pack()
table.pack(anchor=CENTER, expand=1)
player.pack()


window.mainloop()


