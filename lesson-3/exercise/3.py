
NUM_PLAYER = 4
import random


def createDeck():
    global deck
    seeds = ['coppe','denari','spade','bastoni']
    values = ['asso','due','tre','quattro','cinque','sei','sette','jack','donna','re']
    deck = []
    for seed in seeds:
        for value in values:
            deck.append((seed,value))
    return deck

def shuffleDeck():
     random.shuffle(deck)
     return deck

def getCard(deck):
    card_info = random.choice(deck)
    deck.remove(card_info)
    print(f"Card extracted -> {card_info}")
    return card_info

def getWinner(p1=0,p2=0):
     if(p1>p2):
        print('you win 🎉')
     else:
        print('you lose 😱')

def distribute_card(deck):
    game_table = []
    for player in range(0,NUM_PLAYER):
        card = getCard(deck)
        game_table.append(card)
    return game_table
    
def print_game_table(game_table):
    for player in game_table:
        print(f"{player}",sep="--")

if __name__ == "__main__":

    print('-----SND HAND-----')
    deck = createDeck()
    game_table = distribute_card(deck)
    print_game_table(game_table)
