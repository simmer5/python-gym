s1 = input('Enter a string 1: ')
s2 = input('Enter a string 2: ')

if len(s1)!=len(s2):
    print ('The length of the strings are diferent.')
else:
    for l in range(len(s1)):
        print(s1[l].upper()+s2[l], end='')
