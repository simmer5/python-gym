from random import *
from string import *
from pprint import pprint

# Write a program to play the following game. There is a list of several country names
#and the program randomly picks one. The player then has to guess letters in the word
#one at a time.Before each guess the country name is displayed with correctly guessed
#letters filled in andthe rest of the letters represented with dashes. For instance,
#if the country is Canada and the player has correctly guessed a,d, and n, the program
#would display -ana-da. The program should continue until the player either guesses
#all of the letters of the word or gets five letterswrong.

L=['vilnius', 'riga', 'londonas', 'oslas', 'talinas']
c = choice(L)
c = list(c)
#print(c)
b = ['-' for i in range(len(c))]
print(''.join(b))


k=0
s=len(c)
print('Guess the capital.')
while s!=0 and k<5:
    letter = input('Enter the letter to guess: ')
    if letter in c:
        print('Correct letter.')
        location=c.index(letter)
        del c[location]
        c.insert(location, '-')
        b[location] = letter
        print(''.join(b))
        s-=1
    else:
        print('No letter like this.')
        k+=1
        print ('You have {} guesses.'.format(5-k))
        
    
print('The End!')

