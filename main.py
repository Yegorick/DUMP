from tkinter import Tk, Button, LEFT
from PIL import ImageTk

from hands import *
from game import new_game

class App(Tk):
    def __init__(self, cards: list = None) -> None:
        super().__init__()
    #    self.card_list = cards
    #    self.imgs = [ImageTk.PhotoImage(file=f"imgs/{card.mast}/{card.value}.jpg") for card in cards]
    #    self.btns = []
    #    for i, img in enumerate(self.imgs):
    #        b = Button(self, image=img, command=lambda m=i: self.get_card(m))
    #        self.btns.append(b)
    #    
    #    for btn in self.btns:
    #        btn.pack(padx=10, pady=10, side=LEFT)
#
    #def get_card(self, i):
    #    self.card_list[i].move()
    #    self.btns[i].destroy()



pl_hand, comp_hand = new_game()

window = App()

player = Hand(pl_hand)
computer = PCHand(comp_hand, "back")

computer.pack()
player.pack()

window.mainloop()

#running = True
#
#while running:
#    computer.move()
#
#    print(player)
#    print(computer) 
#
#    running = False
