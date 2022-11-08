from PIL import ImageTk
from random import randint

from tkinter import DISABLED, Canvas, Button, LEFT
from game import deck, koz
from card import Card

class Table(Canvas):
    def __init__(self, width, height, bg, PC):
        super().__init__(width=width, height=height, bg=bg)
        self.width = width
        self.height = height
        self.cards = []
        self.card_imgs = []
        self.turn = 1
        self.pc = PC
        self.btn_turn = Button(self, text="Ход компьтера", command=self.show_cards)
        self.create_window(self.width - 150, self.height - 20, window=self.btn_turn)
        self.btn_end = Button(self, text="Конец хода", command=self.end_of_turn)
        self.create_window(self.width - 50, self.height - 20, window=self.btn_end)
        self.pl = None

    def show_cards(self, card = None):
        x = 10
        if self.turn == 1:
            self.cards.append(card)
            print(card)
            self.card_imgs.append(ImageTk.PhotoImage(file=f"imgs/{card[1]}/{card[2]}.jpg"))
            for img in self.card_imgs:
                self.create_image(x, 10, image=img, anchor="nw")
                x += 30
            self.turn = 0
        else:
            card = self.pc.get_card()
            self.cards.append(card)
            self.card_imgs.append(ImageTk.PhotoImage(file=f"imgs/{card[1]}/{card[2]}.jpg"))
            for img in self.card_imgs:
                self.create_image(x, 10, image=img, anchor="nw")
                x += 30
            self.turn = 1
            self.pl.check()
    
    def get_crads(self):
        pc_cards = []
        pl_cards = []
        for _ in range(6 - len(self.pc.cards)):
            if deck[1]["values"] or deck[2]["values"] or deck[3]["values"] or deck[4]["values"]:
                mast = randint(1, 4)
                if mast == koz:
                    card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)), True)
                else:
                    card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)))
            pc_cards.append(card)
        self.pc.add_cards(*pc_cards)
        self.pc.cards.sort(key=self.pc.sort_by_value)
        self.pc.draw_cards('back')
        for _ in range(6 - len(self.pl.cards)):
            if deck[1]["values"] or deck[2]["values"] or deck[3]["values"] or deck[4]["values"]:
                mast = randint(1, 4)
                if mast == koz:
                    card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)), True)
                else:
                    card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)))
            pl_cards.append(card)
        self.pl.add_cards(*pc_cards)
        self.pl.draw_cards(None)


    def end_of_turn(self):
        self.delete("all")
        self.cards.clear()
        self.btn_turn = Button(self, text="Ход компьтера", command=self.show_cards)
        self.create_window(self.width - 150, self.height - 20, window=self.btn_turn)
        self.btn_end = Button(self, text="Конец хода", command=self.end_of_turn)
        self.create_window(self.width - 50, self.height - 20, window=self.btn_end)
        self.get_crads()

