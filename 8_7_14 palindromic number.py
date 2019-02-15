from random import *
from string import *
from pprint import pprint

#Use a list comprehension to produce a list that
#consists of all palindromic numbers
#between100 and 1000.

L = [i for i in range(100, 1000)if int(i/100)==int(i%10)]

print(L)  
    

