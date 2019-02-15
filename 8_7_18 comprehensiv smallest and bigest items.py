from random import *
from string import *
from pprint import pprint

L = [[randint(1, 100) for row in range(10)] for col in range(10)]
pprint(L)


#Find the largest value in the third row.
li3r = max(L[2])
#Find the smallest value in the sixth column.
si6c =min([L[i][5] for i in range(len(L))])
print()
print('Largest value in the third row: ', li3r)
print('Smallest value in the sixth column: ', si6c)
