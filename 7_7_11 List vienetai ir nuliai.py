from random import randint

#Using a for loop, create the list below,
#which consists of ones separated by increasingly
#many zeroes. The last two ones in the list
#should be separated by ten zeroes.
#[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

l = [1]
n = [0, 0, 0, 0]
N=[]
LN=[]
ls =[]

for i in range(10):
    n=n[:i+1]
    N.append(n)
    l=l+N[i]
    LN.append(l)
    ls = ls+LN[i] 
print(ls)
#---------------
print('-'*20)

t = []
for i in range(10+1):
    t += [1]+[0]*i
t.append(1)
print(t)


