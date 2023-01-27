from random import randint, choice

from card import *

deck = {
        1:{"mast":"Черви", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        2:{"mast":"Буби", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        3:{"mast":"Пики", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        4:{"mast":"Крести", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]}
        }

main_deck = []

koz = randint(1, 4)
trump = deck[koz]["mast"]

for i in deck:
    if i == koz:
        for j in deck[i]["values"]:
            main_deck.append(Card(deck[i]["mast"], j, True))
    else:
        for j in deck[i]["values"]:
            main_deck.append(Card(deck[i]["mast"], j))

def new_game():
    global deck, koz

    pl_hand = []
    comp_hand = []

    for _ in range(6):
        pl_hand.append(main_deck.pop(main_deck.index(choice(main_deck))))
        comp_hand.append(main_deck.pop(main_deck.index(choice(main_deck))))
    return (pl_hand, comp_hand)
