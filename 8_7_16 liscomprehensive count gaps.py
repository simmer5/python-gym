from random import *
from string import *
from pprint import pprint

# Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47].
#Use a list comprehension to produce a list of the gaps
#between consecutive entries in L. Then find the maximum
#gap size and the percentage of gaps that have size 2

L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

gap=[L[i+1]-L[i] for i in range(len(L)-1)]
max_gap = max(gap)

proc = (gap.count(2)/(len(L)-1))*100 
print (round(proc, 2))
