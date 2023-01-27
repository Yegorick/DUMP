from PIL import ImageTk
from random import randint, choice

from tkinter import DISABLED, Canvas, Button, LEFT
from game import main_deck, trump
from card import Card

class Table(Canvas):
    def __init__(self, width, height, bg, PC):
        global trump
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
        self.create_text(100, 270, text=f"Козырь: {trump}", font="Arial 20", fill="#FFF")

    def show_cards(self, card = None):
        x = 10
        if self.turn == 1:
            self.cards.append(card)
            self.card_imgs.append(ImageTk.PhotoImage(file=f"imgs/{card[1]}/{card[2]}.jpg"))
            
            for img in self.card_imgs:
                self.create_image(x, 10, image=img, anchor="nw")
                x += 30

            self.turn = 0
        else:
            card = self.pc.get_card(self.cards[len(self.cards) - 1])
            if card == None:
                self.pc.take_cards(*self.cards)
                self.end_of_turn()
                self.turn = 1
                self.pl.check()
                return None
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
            if main_deck:
                pc_cards.append(main_deck.pop(main_deck.index(choice(main_deck))))
            else:
                continue

        self.pc.add_cards(*pc_cards)
        self.pc.cards.sort(key=self.pc.sort_by_value)
        self.pc.draw_cards('back')

        for _ in range(6 - len(self.pl.cards)):
            if main_deck:
                card = main_deck.pop(main_deck.index(choice(main_deck)))
                pl_cards.append(card)
            else:
                continue
        self.pl.add_cards(*pl_cards)
        self.pl.draw_cards(None)


    def end_of_turn(self):
        self.delete("all")
        self.cards.clear()
        self.btn_turn = Button(self, text="Ход компьтера", command=self.show_cards)
        self.create_window(self.width - 150, self.height - 20, window=self.btn_turn)
        self.btn_end = Button(self, text="Конец хода", command=self.end_of_turn)
        self.create_window(self.width - 50, self.height - 20, window=self.btn_end)
        del_list = []
        
        for i in self.pl.cards:
            if i == None:
                del_list.append(None)
        
        for i in del_list:
            self.pl.cards.remove(i)

        self.get_crads()
        self.cards = []
        self.card_imgs = []
