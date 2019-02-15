from random import *
from string import *
from pprint import pprint

#Create a 5×5 list of numbers. Then write a program that creates
#a dictionary whose keys are the numbers and whose values are the how
#many times the number occurs.  Then print the three most common numbers.

L=[[randint(1, 25) for row in range(5)] for col in range(5)]
pprint(L)
d = {}

for row in L:
    for col in row:
        if col in d:
            d[col] = d[col]+1
        else:
            d[col] = 1
pprint(d)
ds = list(d.items())
ds = [(i[1], i[0]) for i in ds]
ds.sort()
print('Three most common values: ')
for i in range(3):
    print(ds.pop())
