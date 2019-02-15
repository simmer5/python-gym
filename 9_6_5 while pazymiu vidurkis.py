from random import *
from string import *
from pprint import pprint

# Write a program that allows the user to enter any number
#of test scores. The user indicatesthey are done by
#entering in a negative number.
#Print how many of the scores are A’s (90 orabove).
#Also print out the average

s=[]        
p=1
a=0
while p>0:
    p = eval(input('Enter score: '))
    s.append(p)
    if p>=90:
        a+=1
else:
    print('Baigta!')
    print('A -',a)
    print('{} proc.'.format(a/(len(s)-1)*100))


