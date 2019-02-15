from random import *
from string import *
from pprint import pprint

#Use thechoicemethod to create a random anagram of a string.

zodis = input ('Enter the word: ')
list = list(zodis)
for i in range(len(zodis)):
    r = choice(list)
    print(r, end='')
    list.remove(r)
     


  
    
    

