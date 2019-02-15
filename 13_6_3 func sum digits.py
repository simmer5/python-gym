from random import *
from string import *
from pprint import pprint

#Write a function called sum_digits that is given an integer num and
#returns the sum of the digits of num.

def suma(num):
    s=0
    for i in str(num):
        i = int(i)
        s = s+i
    return s
    
print(suma(4657))
