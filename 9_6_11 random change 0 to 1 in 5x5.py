from random import *
from string import *
from pprint import pprint

#Write a program that starts with an 5×5 list of zeroes
#and randomly changes exactly five of those zeroes to ones.

L=[[0 for x in range(5)] for j in range(5)]
C = [(x, y) for x in range(5) for y in range(5)]
pprint(L)
print('-'*20)

k = 0
while k!=5:
    c = choice(C)
    if L[c[0]][c[1]] !=1:
        L[c[0]][c[1]] = 1
    k+=1
pprint(L)
