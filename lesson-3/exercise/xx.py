import random

NUM_PLAYER = 4

def createDeck():
    seeds = ['bastoni', 'coppe', 'spade', 'denari']
    values = ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Fante', 'Cavallo', 'Re']
    deck = []
    for seed in seeds:
        for value in values:
            deck.append((seed,value))
    return deck

def getCard(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def compare_cards(game_table):
    deck_value = createDeck()
    winning_card = game_table[0]
    for card in game_table:
        winning_card_points = deck_value.index(winning_card)
        card_points = deck_value.index(card)
        if card_points>winning_card_points:
            winning_card = card
    return winning_card

def distribute_card(deck):
    game_table = []
    for player in range(0, NUM_PLAYER):
        card = getCard(deck)
        game_table.append(card)
    return game_table

def print_game_table(game_table):
    for player in game_table:
        print(f"{player}",sep="--")

def print_card(card):
    print("*"*10)
    print(f"Card -> {card}")
    print("*"*10)

if __name__ == "__main__":
    deck = createDeck()
    game_table = distribute_card(deck)
    print_game_table(game_table)
    winning_card = compare_cards(game_table)
    print_card(winning_card)
