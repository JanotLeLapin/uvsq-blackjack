import random

KINDS = {0: "Carreau", 1: "Pic", 2: "Coeur", 3: "Trèfle"}
STACK = [x for x in range(13 * 4)]

random.shuffle(STACK)

def pick_card():
    return STACK.pop()

def deserialize_card(card):
    return (KINDS[card // 13], card % 13)
