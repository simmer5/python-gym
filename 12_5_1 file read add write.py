from random import *
from string import *
from pprint import pprint

# You are given a file calledclass_scores.txt, where each line of the file 
#contains a one-word username and a test score separated by spaces, like below.
#Write code that scans through the file, adds 5 points to each test score, and outputs the user-names and new 
#test scores to a new file,scores2.txt
with open('write.txt', 'w') as f:
    print('GWashington 83', file=f)
    print('JAdams 86', file=f)

L = [line.split() for line in open('write.txt')]
nf = open('naujas.txt','w')
for i in L:
    print(i[0], int(i[1])+5, file=nf)
nf.close()
