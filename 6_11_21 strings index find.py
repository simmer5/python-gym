s, l =input('Enter the string: '), input('Enter letter to find: ')


# checks for letter in string without using "in"
if s.index(l)!=-1 :
    print('Letter exist in the string.')
else:
    print ('No letter like this.')

#letter occurrences in the string without using count()

counter = 0
for i in s:
    if i==l:
        counter = counter+1
print('Amount of letter {} - {}'.format(l, counter))        

#index of the first occurrence of the letter in the string without using index()

for i in range(len(s)):
    if s[i]==l:
        print ('Index of the first letter {} is: {}'.format(l, i))
        break
