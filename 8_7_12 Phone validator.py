from random import *
from string import *
from pprint import pprint
# Write a program that gets a string from the user containing a potential
#telephone number. The program should print Valid if it decides the phone
#number is a real phone number, and Invalid otherwise.  A phone number is
#considered valid as long as it is written in the form
#abc-def-hijk or 1-abc-def-hijk.
#The dashes must be included, the phone number should containonly
#numbers and dashes, and the number of digits in each group must be correct.


tel = input ('Enter the phone number: ')
d_sk = tel.count('-')
spl_tel = tel.split('-')
no_letters = True
sk = len(tel)

for i in spl_tel:
    if i.isdigit():
        continue
    else:
        no_letters = False
    
if sk == 14 and d_sk==3 and spl_tel[0]=='1' and no_letters == True:

    print ('Number is valid.')
elif sk == 12 and d_sk==2 and no_letters == True:
    print ('Number is correct.')
else:
    print('Bad number.')
    
    

