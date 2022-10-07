class Card:
    def __init__(self, mast, value, koz = False,) -> None:
        self.koz = koz
        self.mast = mast
        self.value = value

    def move(self):
        print(self.koz, self.mast, self.value)
        
    def __str__(self) -> str:
        return self.mast + " " + str(self.value)
    
    def __repr__(self) -> str:
        return self.mast + " " + str(self.value)
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Нужно передать карту")
        
        return self.value < other.value
    
    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Нужно передать карту")
        
        return self.value > other.value
        
    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Нужно передать карту")
        
        return self.value == other.value
