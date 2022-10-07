from random import randint

from card import *

def new_game():
    deck = {1:{"mast":"Черви", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        2:{"mast":"Буби", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        3:{"mast":"Пики", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        4:{"mast":"Крести", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},}

    koz = randint(1, 4)

    pl_hand = []
    comp_hand = []

    for _ in range(6):
        if deck[1]["values"] or deck[2]["values"] or deck[3]["values"] or deck[4]["values"]:
            mast = randint(1, 4)
            if mast == koz:
                card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)), True)
            else:
                card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)))
            pl_hand.append(card)
            mast = randint(1, 4)
            if mast == koz:
                card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)), True)
            else:
                card = Card(deck[mast]["mast"], deck[mast]["values"].pop(randint(0, len(deck[mast]["values"]) - 1)))
            comp_hand.append(card)

    return (pl_hand, comp_hand)
