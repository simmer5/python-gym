from random import *
from string import *
from pprint import pprint

#The following is useful in implementing computer
#players in a number of different games. Write a program
#that creates a5×5 list consisting of zeroes and ones.
#Your program should then pick a random location in the
#list that contains a zero and change it to a one.
#If all the entries are one, the program should say so.
#[Hint: one way to do this is to create a new list whose
#items are the coordinates of all the ones in the list and
#use the choice method to randomly select one.
#Use a two-element list to represent a set of coordinates.]

L = [[randint(0, 1) for row in range(5)] for col in range(5)]
pprint(L)
print()

#location list with 0
print('0 location list:')
loc_0 =[(r, c) for r in range(len(L)) for c in range(len(L)) if L[r][c]!=1]
print(loc_0)
#------------
lo = choice(loc_0)
print('Random location for canging from 0 to 1: ', lo)
print()
loc_0.remove(lo)    

#Changing value from 0 to 1
L[lo[0]][lo[1]]=1

#full line checker
for i in L:
    if sum(i)==5:
        print('{} line if full!'.format(L[i]))

print('You still have {} free places:'.format(len(loc_0)))
pprint(L)
        
    



        

