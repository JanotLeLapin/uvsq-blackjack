import random

KINDS = {0: "Carreau", 1: "Pic", 2: "Coeur", 3: "Trèfle"}
STACK = [x for x in range(13 * 4)]

random.shuffle(STACK)

def pick_card():
    return STACK.pop()

def deserialize_card(card):
    return (KINDS[card // 13], min(card % 13, 10))

def count_deck(deck):
    return sum(map(lambda card: deserialize_card(card)[1] + 1, deck))

def stringify_card(card):
    (kind, value) = deserialize_card(card)
    return f"{'As' if value == 0 else value + 1} de {kind}"

def stringify_deck(deck):
    return ", ".join(map(stringify_card, joueur)) + f" (valeur totale: {count_deck(deck)})"

joueur = [pick_card() for _ in range(2)]
croupier = [pick_card() for _ in range(2)]

print(stringify_deck(joueur))
while True:
    option = input("> Quel est votre choix?\n").upper()
    if option == "HIT":
        joueur.append(pick_card())
        print(stringify_deck(joueur))
        if count_deck(joueur) > 21:
            print("Degage sale clochard")
            break
    elif option == "STAND":
        break
    elif option == "SURRENDER":
        break
    else:
        print("Option inconnue")
