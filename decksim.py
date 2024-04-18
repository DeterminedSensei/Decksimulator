import os
import argparse
from pathlib import Path
import random




if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Decksim', 
                                    description='Simulate playing with a deck in a card game', )
    parser.add_argument('-d', '--deck', dest='deck', default='nonegiven', help='first argument')

    decks = parser.parse_args().deck
    print(decks)

    if decks == 'nonegiven' or not os.path.isfile(decks):
        
        decks = os.path.join(os.getcwd(), 'deck.txt')
    
    decklist = open(decks, "r")
    cards = [line.rstrip('\n') for line in decklist]
    print(cards)
    random.shuffle(cards)
    handcards = []
    Userinput = ""
    while(not (Userinput == "quit")):
        Userinput = input()
        if len(Userinput.split()) == 1:
            if Userinput == "draw":
                handcards.append(cards.pop())
            elif Userinput == "hand":
                print(handcards)
            elif Userinput == "decklist":
                print(cards)
            else:
                print("Den Command gibt es gar nicht du Idiot")
        else:
            command = Userinput.split()
            if command[0] == "add":
                handcards.append(" ".join(command[1:]))
            elif command[0] == "use":
                try:
                    handcards.remove(" ".join(command[1:]))
                except:
                    print("Du hast die Karte gar nicht auf der Hand du Idiot")
            elif command[0] == "draw":
                try:
                    handcards.append(cards.pop(cards.index(" ".join(command[1:]))))
                except:
                    print("Eine solche Karte gibt es nicht in deinem Deck")
            elif command[0] == "deck":
                cards.append(" ".join(command[1:]))
                random.shuffle(cards)
            else:
                print("Der Command existiert gar nicht")
    exit()



        