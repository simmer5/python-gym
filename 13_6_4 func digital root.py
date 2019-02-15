from random import *
from string import *
from pprint import pprint

#The digital root of a number n is obtained as follows:
#Add up the digits n to get a new number. Add up
#the digits of that to get another new number.
#Keep doing this until you get a number that has
#only one digit.
#That number is the digital root.

def root (n):
    """ Function returns digital root of the number """
    while n>9:
        n=str(n)
        n=[int(n) for n in n]
        s = sum(n)
        n=s
    return n

print(root(4325))
