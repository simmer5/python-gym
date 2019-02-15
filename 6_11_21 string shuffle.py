from random import randint

s =input('Enter a string:')
sk = [ls for ls in s]
sn =''
print(sk)

for i in range(len(s)):
    rsk = randint(0, len(s)-1)
    temp = sk[i]
    sk[i]=sk[rsk]
    sk[rsk]=temp

for i in sk:
    sn = sn+i
print('After shuffle: {}'.format(sn))
