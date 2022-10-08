from PIL import ImageTk

from tkinter import DISABLED, Canvas, Button, LEFT, NORMAL


class Hand(Canvas):
    def __init__(self, cards, table=None, img=None) -> None:
        super().__init__()
        self.cards = list(cards)
        self.table = table

        self.memory = []

        if not img:
            self.imgs = [ImageTk.PhotoImage(file=f"imgs/{card.mast}/{card.value}.jpg") for card in self.cards]
        else:
            self.imgs = [ImageTk.PhotoImage(file=f"imgs/{img}.jpg") for card in self.cards]
        self.btns = []
        for i, img in enumerate(self.imgs):
            b = Button(self, image=img, command=lambda m=i: self.get_card(m))
            self.btns.append(b)
        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=LEFT)

    def get_card(self, i):
        self.table.show_cards(self.cards[i].move())
        self.btns[i].destroy()
        #self.btns.pop(i)
        self.memory.append(self.btns[i])
        self.check()

    def check(self):
        btns = []
        for el in self.memory:
            if el in self.btns:
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

    def get_card(self):
        card = self.cards[0].move()
        self.cards.pop(0)
        self.btns[0].destroy()
        self.btns.pop(0)
        print(card)
        return card
