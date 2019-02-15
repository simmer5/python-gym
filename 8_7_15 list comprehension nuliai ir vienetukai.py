from random import *
from string import *
from pprint import pprint

# Use a list comprehension to create the list below, which consists
#of ones separated by increas-ingly many zeroes.
#The last two ones in the list should be separated by ten zeroes.
#[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

L = [[1]+[0]*i for i in range(0, 10+1)]
l = [x for xs in L for x in xs]  


#for i in range(len(L)):
#    l=l+L[i]

LL=[x for xs in [([1] + [0] * i + [1]) for i in range(0, 10 + 1)] for x in xs]

listas = [[3, 4, 6], [9, 8, 1]]
li =[item for i in listas for item in i]

L=[f"{a}-{b}-{c}" for a in range(5) for b in "abc" for c in range(6)]


