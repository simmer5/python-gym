from random import *
from string import *
from pprint import pprint

s = input('Enter a string: ')
L = s.split()
print(L)

#removes first letter and makes new list
l = [i[1:] for i in L]
#length of the strings in L
le = [len(item) for item in L]
#strings longe then 3 from L
tr = [item for item in L if len(item)>3]


  
    

