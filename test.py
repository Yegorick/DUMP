class Card:
    def __init__(self, mast, value, koz = False,) -> None:
        self.koz = koz
        self.mast = mast
        self.value = value
        
    def __str__(self) -> str:
        return self.mast + str(self.value)
    
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


c1 = Card("asd", 10)
c2 = Card("asd", 11)

v = [c2, c1]

def sort_value(el):
    return el.value

print(v)

v.sort(key=sort_value)

print(v)
