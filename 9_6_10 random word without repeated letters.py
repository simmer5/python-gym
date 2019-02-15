from random import *
from string import *
from pprint import pprint

#Write a program that has a list of ten words, some
#of which have repeated letters and somewhich don’t.
#Write a program that picks a random word from the list
#that does not have anyrepeated letters.

L= ['player', 'correctly', 'guessed', 'filled', 'letters', 'represented', 'dashes', 'game', 'several', 'program']
ll =[]

#1
print(L)
for zodis in L:
    for letters in range(len(zodis)-1):
        #print(zodis[letters], end="")
        if zodis[letters] == (zodis[letters+1]):
            ll.append(zodis)
print('Random word with repeated letters: ', choice(ll))
      
#2
aa =[zodis for zodis in L for letters in range(len(zodis)-1) if zodis[letters] == zodis[letters+1]]

print('Random word with repeated letters: {}.'.format(choice(aa).upper()))


