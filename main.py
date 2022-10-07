from tkinter import Tk, Button, LEFT
from PIL import ImageTk

from hands import *
from game import new_game
from table import Table

class App(Tk):
    def __init__(self, cards: list = None) -> None:
        super().__init__()
        


pl_hand, comp_hand = new_game()

window = App()

table = Table(800, 300)
player = Hand(pl_hand, table)
computer = PCHand(comp_hand, img="back")

computer.pack()
table.pack()
player.pack()

table.create_image(10, 100, image=ImageTk.PhotoImage(file="imgs/back.jpg"))
window.mainloop()


