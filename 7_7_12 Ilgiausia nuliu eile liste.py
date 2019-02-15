from random import randint

#Write a program that generates  100 random integers
#that  are  either  0  or  1.   Then  find  the longest run
#of zeros, the largest number of zeros in a row.
#For instance, the longest run ofzeros
#in [1,0,1,1,0,0,0,0,1,0,0]is 4.

l = [randint(0,1) for i in range (100)]
blokai=[]
print(l)
vienetai = l.count(1)
for i in range(vienetai):
    v = l.index(1)
    blokai.append(v)
    #print (l.index(1))
    del l[:v+1]
    #print(l)
    
print('The longest run of zeros: {}'.format(max(blokai)))    
