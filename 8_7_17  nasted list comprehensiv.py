from random import *
from string import *
from pprint import pprint

# Write a program that finds the average of all of the entries
#in a 4×4 list of integers.

L=[[randint(1, 10) for r in range(4)] for col in range(4)]
print(L)

# 1

sm_items =[b for a in L for b in a]#suma visu elementu
print ('Average of 4x4: {}'.format(sum(sm_items)/16) )

# 2

sm_row = [sum(row) for row in L ]#suma kiekvienos eilutes elementu
avg = [item/4 for item in sm_row]
print ('Average of row: {}'.format(avg) )
