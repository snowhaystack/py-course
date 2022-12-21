#OUTPUT => DECK ORDERED WITH PRIORITY BASED ON
#SEED AND VALUES

#VARIABLE INIT
import random
seeds = ('coppe','denari','spade','bastoni')
values = ('asso','due','tre','quattro','cinque','sei','sette','jack','donna','re')
deck = []

for seed in seeds:
    for value in values:
        deck.append([seed,value])


print(f'complete deck => {deck}')
print(f'lower card value => {deck[0]}')
print(f'major card => {deck[-1]}')
random.shuffle(deck)
print('')
print(f'random ordered deck => {deck}')