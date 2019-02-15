from random import *
from string import *
from pprint import pprint

# Use the following two lists and theformatmethod to create
#a list of card names in the formatcard valueofsuit name
#(for example,'Two of Clubs').

suits = ['Hearts','Diamonds','Clubs','Spades']
values = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

for s in suits:
    for v in values:
        print('{:>8s} of {:8s}'.format(v, s))
