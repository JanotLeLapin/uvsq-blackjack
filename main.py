import random


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
joueur = [pick_card() for _ in range(2)]
croupier = [pick_card() for _ in range(2)]
bot1 = [pick_card() for _ in range(2)]
bot2 = [pick_card() for _ in range(2)]
bot3 = [pick_card() for _ in range(2)]

print(bot1)
print(bot2)
print(bot3)

# bots choisissent ce qu'ils veulent faire

botoption = ["hit","stand"]
choixbot1 = random.randint(0,1)
choixbot2 = random.randint(0,1)
choixbot3 = random.randint(0,1)

# Choix du bot1
if botoption[choixbot1]=="hit":

    bot1.append(pick_card())
    print(stringify_deck(bot1))
    if count_deck(bot1) == -1:
            print("bot1 a depassé 21: élimination du jeu")
            
elif botoption[choixbot1]=="stand":
    print("bot 1 ne force pas il a donc "+ stringify_deck(bot1))


# Choix du bot2
if botoption[choixbot2]=="hit":
    bot2.append(pick_card())
    print(stringify_deck(bot2))
    if count_deck(bot2) == -1:
            print("bot2 a depassé 21: élimination du jeu")
            
elif botoption[choixbot2]=="stand":
    print("bot 2 ne force pas il a donc "+ stringify_deck(bot2))
    

# Choix du bot3
if botoption[choixbot3]=="hit":
    bot3.append(pick_card())
    print(stringify_deck(bot3))
    if count_deck(bot3) == -1:
            print("bot3 a depassé 21: élimination du jeu")
            
elif botoption[choixbot3]=="stand":
    print("bot 3 ne force pas il a donc "+ stringify_deck(bot3))
    
# Boucle principale
 
while True:
    print(stringify_deck(joueur))
    option = input("> Quel est votre choix?\n").upper()
    if option == "HIT":
        joueur.append(pick_card())
        print(stringify_deck(joueur))
        if count_deck(joueur) == -1:
            print("Degage sale clochard")
            break
    elif option == "STAND":
        count_croupier = count_deck(croupier)
        res = count_deck(joueur) - count_croupier  
        if res > 0:
            print("Joueur a gagné , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
            break
        elif res == 0:
            print("Égalité , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
            break
        else:
            print("Joueur a perdu , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
            break
    elif option == "SURRENDER":
        print("fin partie")
        break
    else:
        print("Option inconnue")
        break

count_croupier = count_deck(croupier)
res = count_deck(joueur) - count_croupier
bot1res=count_deck(bot1) - count_croupier
bot2res=count_deck(bot2) - count_croupier
bot3res=count_deck(bot3) - count_croupier

print(f"Deck croupier: {count_croupier}")

