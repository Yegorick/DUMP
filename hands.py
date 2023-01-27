from PIL import ImageTk

from tkinter import DISABLED, Canvas, Button, LEFT, NORMAL

from card import Card

class Hand(Canvas):
    def __init__(self, cards, table=None, img=None) -> None:
        super().__init__()
        self.cards = list(cards)
        self.table = table
        self.btns = None

        self.memory = []

        self.draw_cards(img)

    def draw_cards(self, img):
        if self.btns:
            for btn in self.btns:
                btn.destroy()
        if not img:
            self.imgs = [ImageTk.PhotoImage(file=f"imgs/{card.mast}/{card.value}.jpg") for card in self.cards]
        else:
            self.imgs = [ImageTk.PhotoImage(file=f"imgs/{img}.jpg") for _ in self.cards]
        self.btns = []
        for i, img in enumerate(self.imgs):
            b = Button(self, image=img, command=lambda m=i: self.get_card(m))
            self.btns.append(b)
        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=LEFT)

    def get_card(self, i):
        self.table.show_cards(self.cards[i].move())
        self.btns[i].destroy()
        self.cards[i] = None
        self.memory.append(self.btns[i])
        self.check()

    def check(self):
        btns = []
        for el in self.btns:
            if el in self.memory:
                continue
            btns.append(el)
        if self.table.turn == 0:
            for btn in btns:
                btn["state"] = DISABLED
        else:
            for btn in btns:
                btn["state"] = NORMAL


    def add_cards(self, *cards):
        for card in cards:
            self.cards.append(card)
    
   
    def __str__(self) -> str:
        return str(self.cards)


class PCHand(Hand):
    def __init__(self, cards, img) -> None:
        cards.sort(key=self.sort_by_value)
        super().__init__(cards, img=img)
        for btn in self.btns:
            btn["state"] = DISABLED

    def sort_by_value(self, card):
        return card.value

    def get_card(self, pl_card):
        for card in self.cards:
            if card.move()[1] == pl_card[1] and card.move() > pl_card:
                self.btns[self.cards.index(card)].destroy()
                self.btns.pop(self.cards.index(card))
                self.cards.pop(self.cards.index(card))
                return card.move()
            elif card.move()[0] == True and pl_card[0] == True and card.move() > pl_card:
                self.btns[self.cards.index(card)].destroy()
                self.btns.pop(self.cards.index(card))
                self.cards.pop(self.cards.index(card))
                return card.move()
        return None
                
    def take_cards(self, *cards):
        new_cards = []
        for i in cards:
            card = Card(i[1], i[2], i[0])
            new_cards.append(card)
        self.cards = self.cards + new_cards
    
    def draw_cards(self, img):
        super().draw_cards(img)
        for btn in self.btns:
            btn["state"] = DISABLED
