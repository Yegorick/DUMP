from PIL import ImageTk

from tkinter import DISABLED, Canvas, Button, LEFT


class Hand(Canvas):
    def __init__(self, cards, table=None, img=None) -> None:
        super().__init__()
        self.cards = list(cards)
        self.table = table

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


    def add_cards(self, *cards):
        for card in cards:
            self.cards.append(card)
    
   
    def __str__(self) -> str:
        return str(self.cards)


class PCHand(Hand):
    def __init__(self, cards, img) -> None:
        super().__init__(cards, img=img)
        self.cards.sort(key=self.sort_by_value)
        for btn in self.btns:
            btn["state"] = DISABLED

    def sort_by_value(self, card):
        return card.value

    def move(self):
        return self.cards.pop(0)
