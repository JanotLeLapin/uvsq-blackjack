import random
import time

KINDS = {0: "Carreau", 1: "Pic", 2: "Coeur", 3: "Trèfle"}

# Génération de la pile
STACK = [x for x in range(13 * 4)]
random.shuffle(STACK)


def pick_card():
    
    #Retire la dernière carte de la pile et la renvoie
    
    return STACK.pop()

def deserialize_card(card):
    
    #Renvoie un tuple contenant le type de la carte et sa valeur
    
    return (KINDS[card // 13], min(card % 13, 10))

def count_deck(deck):
    
    #Renvoie la valeur totale du deck, ou -1 si la valeur excède 21
    
    value = sum(map(lambda card: deserialize_card(card)[1] + 1, deck))
    return -1 if value > 21 else value

def stringify_card(card):
  
    #Renvoie une représentation lisible d'une carte
   
    (kind, value) = deserialize_card(card)
    return f"{'As' if value == 0 else value + 1} de {kind}"

def stringify_deck(deck):
    
    #Renvoie une représentation lisible d'un deck
    
    return (", ".join(map(stringify_card, joueur)) + f" (valeur totale: {count_deck(deck)})")

# Génération des decks
joueur = [pick_card() for _ in range(2)]
croupier = [pick_card() for _ in range(2)]
bot1=[pick_card() for _ in range(2)]
bot2=[pick_card() for _ in range(2)]
bot3=[pick_card() for _ in range(2)]



#bots commencent à piocher carte random

botoption=["hit","stand"]
choixbot1=random.randint(0,2)
choixbot2=random.randint(0,2)
choixbot3=random.randint(0,2)

 
game=input("commencer? Y/N").upper()
if game=="Y":
    if botoption[choixbot1]=="hit":

        bot1.append(pick_card())
        print(stringify_deck(bot1))
        if count_deck(bot1) == -1:
                print("bot1 a depassé 21: élimination du jeu")
                
    elif botoption[choixbot1]=="stand":
        print("bot 1 ne force pas il a donc"+ stringify_card(bot1))
    


    if botoption[choixbot2]=="hit":
        bot2.append(pick_card())
        print(stringify_deck(bot2))
        if count_deck(bot2) == -1:
                print("bot2 a depassé 21: élimination du jeu")
                
    elif botoption[choixbot2]=="stand":
        print("bot 2 ne force pas il a donc"+ stringify_card(bot2))
        


    if botoption[choixbot3]=="hit":
        bot3.append(pick_card())
        print(stringify_deck(bot3))
        if count_deck(bot3) == -1:
                print("bot3 a depassé 21: élimination du jeu")
                
    elif botoption[choixbot3]=="stand":
        print("bot 3 ne force pas il a donc"+ stringify_card(bot3))
        

    bot2.append(pick_card())
    print(stringify_deck(bot2))

    bot3.append(pick_card())
    print(stringify_deck(bot3))

    # Boucle principale
    x=True
    if x==True:
        print(stringify_deck(joueur))
        option = input("> Quel est votre choix?\n").upper()
        if option == "HIT":
            joueur.append(pick_card())
            print(stringify_deck(joueur))
            if count_deck(joueur) == -1:
                print("Degage sale clochard")
                x=False
        elif option == "STAND":
            count_croupier = count_deck(croupier)
            res = count_deck(joueur) - count_croupier  
            if res > 0:
                print("Joueur a gagné , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
                x=False
            elif res == 0:
                print("Égalité , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
                x=False
            else:
                print("Joueur a perdu , la valeur des cartes du croupier faisait au total "+ str(count_croupier))
                x=False
        elif option == "SURRENDER":
            print("fin partie")
            x=False
        else:
            print("Option inconnue")

count_croupier = count_deck(croupier)
res = count_deck(joueur) - count_croupier
bot1res=count_deck(bot1) - count_croupier
bot2res=count_deck(bot2) - count_croupier
bot3res=count_deck(bot3) - count_croupier

print(f"Deck croupier: {count_croupier}")

def resultat():
    if res > 0:
        print("Joueur a gagné")
    elif res == 0:
        print("Égalité")
    else:
        print("Joueur a perdu")


if bot1res>0:
    print("Bot1 a gagné avec une valeur de " + count_deck(bot1))
elif bot1res == 0:
    print("Égalité avec une valeur de " + count_deck(bot1))
else:
    print("Bot1 a perdu avec une valeur de " + count_deck(bot1))


if bot2res>0:
    print("Bot1 a gagné avec une valeur de " + count_deck(bot2))
elif bot2res == 0:
    print("Égalité avec une valeur de " + count_deck(bot2))
else:
    print("Bot1 a perdu avec une valeur de " + count_deck(bot2))


if bot3res>0:
    print("Bot1 a gagné avec une valeur de " + count_deck(bot3))
elif bot3res == 0:
    print("Égalité avec une valeur de " + count_deck(bot3))
else:
    print("Bot1 a perdu avec une valeur de " + count_deck(bot3))

