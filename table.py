from PIL import ImageTk

from tkinter import DISABLED, Canvas, Button, LEFT

class Table(Canvas):
    def __init__(self, width, height):
        super().__init__(width=width, height=height)
        self.cards = []

    def show_cards(self, card):
        self.cards.append(card)
        print(card)
        self.create_image(200, 200, image=ImageTk.PhotoImage(file=f"imgs/{card[1]}/{card[2]}.jpg"))
        self.pack()
        

