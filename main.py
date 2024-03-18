import random
import sys

KINDS = {0: "Carreau", 1: "Pic", 2: "Coeur", 3: "Trèfle"}

# Génération de la pile
STACK = [x for x in range(13 * 4)]
random.shuffle(STACK)


def pick_card():
    # Retire la dernière carte de la pile et la renvoie
    return STACK.pop()


def deserialize_card(card):
    # Renvoie un tuple contenant le type de la carte et sa valeur
    return (KINDS[card // 13], min(card % 13, 10))


def count_deck(deck):
    # Renvoie la valeur totale du deck, ou -1 si la valeur excède 21
    value = sum(map(lambda card: deserialize_card(card)[1] + 1, deck))
    return -1 if value > 21 else value


def stringify_card(card):
    # Renvoie une représentation lisible d'une carte
    (kind, value) = deserialize_card(card)
    return f"{'As' if value == 0 else value + 1} de {kind}"


def stringify_deck(deck):
    # Renvoie une représentation lisible d'un deck
    return (", ".join(map(stringify_card, deck)) + f" (valeur totale: {count_deck(deck)})")


# Génération des decks
croupier = [pick_card() for _ in range(2)]
players = [[pick_card() for _ in range(2)] for _ in range(4)]

# Boucle principale
while True:
    print(stringify_deck(players[0]))
    for i in range(4):
        # TODO: Ajouter des options pour les bots
        option = input("> Quel est votre choix?\n").upper() if i == 0 else random.choice(["HIT"])
        if option == "HIT":
            players[i].append(pick_card())
            print(stringify_deck(players[i]))
            if count_deck(players[i]) == -1:
                print("Degage sale clochard")
                sys.exit(0)
                break
        elif option == "STAND":
            winner = 0
            for i in range(4):
                if count_deck(players[i]) > count_deck(players[winner]):
                    winner = i
            count_croupier = count_deck(croupier)

            # TODO: Égalité
            if count_deck(players[winner]) > count_croupier:
                print(f"Joueur {winner} a gagné ({stringify_deck(players[winner])}).")
                sys.exit(0)
            else:
                print(f"Croupier a gagné ({stringify_deck(croupier)})")
                sys.exit(0)

        elif option == "SURRENDER":
            print("fin partie")
            break
        else:
            print("Option inconnue")
            break
