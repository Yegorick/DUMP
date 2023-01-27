from card import Card
from random import randint

deck = {
        1:{"mast":"Черви", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        2:{"mast":"Буби", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        3:{"mast":"Пики", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]},
        4:{"mast":"Крести", "values":[6, 7, 8, 9, 10, 11, 12, 13, 14]}
        }

main_deck = []

koz = randint(1, 4)

for i in deck:
    if i == koz:
        for j in deck[i]["values"]:
            main_deck.append(Card(deck[i]["mast"], j, True))
    else:
        for j in deck[i]["values"]:
            main_deck.append(Card(deck[i]["mast"], j))

print(main_deck)
