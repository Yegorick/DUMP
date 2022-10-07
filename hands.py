class Hand:
    def __init__(self, *cards) -> None:
        self.cards = list(cards)
        
    def add_cards(self, *cards):
        for card in cards:
            self.cards.append(card)
    
    def move(self, card=None):
        if card:
            ...
        else:
            
            print(self.cards.pop())
    
    def __str__(self) -> str:
        return str(self.cards)


class PCHand(Hand):
    def __init__(self, *cards) -> None:
        super().__init__(*cards)
        self.cards.sort(key=self.sort_by_value)

    def sort_by_value(self, card):
        return card.value

    def move(self):
        print(self.cards.pop(0))
