from random import *
from string import *
from pprint import pprint


#Adding certain numbers to their reversals sometimes produces a palindromic number.
#Forinstance, 241 + 142 = 383.  Sometimes, we have to repeat the process.
#For instance, 84 + 48 =132 and 132 + 231 = 363.
#Write a program that finds both two-digit numbers for which thisprocess must
#be repeated more than 20 times to obtain a palindromic number.

L=[sk for sk in [str(sk) for sk in range(10, 151)] if (str(sk)!= str(sk[::-1]))]

for sk in L:
    k=0
    print('Pirminis sk: ',sk)
    sk =str(sk)
    while sk!=sk[::-1]:
        k+=1
        rsk = sk[::-1]
        rsk =int(rsk)
        sk = int(sk)
        sm = rsk+sk
        sk = str(sm)
    print(sk, '- achieved in ',k,' loops.' )
    
