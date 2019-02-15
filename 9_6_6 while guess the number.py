from random import *
from string import *
from pprint import pprint

#Modify the higher/lower program so that when
#there is only one guess left, it says1 guess, not 1 guesses.

sk = randint(1, 100)
#print(sk)

k=0
guess = 0
print('Guess the number between 1-100')
print('You have {} guesses.'.format(5-k))
while guess!=sk and k!=5:
    k+=1
    guess = eval(input('Your guess: '))
    
    if guess>sk:
        print('Lower.')
        if k==4:
            print('You have {} guess.'.format(5-k))
        else:
            print('You have {} guesses.'.format(5-k))
    elif guess<sk:
        print('Higher.')
        if k==4:
            print('You have {} guess.'.format(5-k))
        else:
            print('You have {} guesses.'.format(5-k))
    elif k==5:
        print('You have no more guess.')
    else:
        print('Correct!!!')
        break
    
else:
    print('The End.')
