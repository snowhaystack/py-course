"""
- creating the deck 
- get a card from the deck 
- comparing two cards and returning the winning one (the one with the highest value) 
"""
NUM_PLAYER = 4
import random
def createDeck():
    global deck
    seeds = ('coppe','denari','spade','bastoni')
    values = ('asso','due','tre','quattro','cinque','sei','sette','jack','donna','re')
    deck = []
    for seed in seeds:
        for value in values:
            deck.append((seed,value))
    return deck
def shuffleDeck():
     random.shuffle(deck)
     return deck
def getCard():
    card_info = {'index':random.randint(1,len(deck)),'card':deck[random.randint(1,len(deck))]}
    deck.remove(card_info['card'])
    return card_info
def getWinner(p1=0,p2=0):
     if(p1>p2):
        print('you win 🎉')
     else:
        print('you lose 😱')

if __name__ == "__main__":

    deck = createDeck()
    deck = shuffleDeck()
    print(f'complete deck => {createDeck()}')
    print('---------------------------------')
    print(f'random ordered deck => {shuffleDeck()}')
    print('---------------------------------')
    my_card = getCard()
    my_card_value = my_card['card']
    my_card_indexes = my_card['index']
    opponent_card = getCard()
    opponent_card_value = opponent_card['card']
    opponent_card_indexes = opponent_card['index']
    print(f'my card => {my_card_value}')
    print('---------------------------------')
    print(f'opponent card => {opponent_card_value}')
    print('--------------WINNER IS-------------------')
    for i in range(1,10):
        print('DRUM ROLL')
    getWinner(my_card_indexes,opponent_card_indexes)
