from random import *
from string import *
from pprint import pprint

#(a)  Write a program that asks the user to enter a
#sentence and then randomly rearranges thewords of the
#sentence. Don’t worry about getting punctuation or
#capitalization correct.
#(b)  Do the above problem, but now make sure that the sentence
#starts with a capital, thatthe original first word is not capitalized if
#it comes in the middle of the sentence, andthat the period is in
#the right place.

S=[]
SS=[]
tt=[]
s = input('Enter a sentence: ')
s = s.lower()
s = s.split('.')
for i in range (len(s)):
    S.append(s[i].split())
    shuffle(S[i])
    SS.append(' '.join(S[i]))
    tt.append(SS[i].capitalize())
    t = '. '.join(tt)
print(t)

  
    
    

