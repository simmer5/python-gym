s = input('Enter a string: ')
s = s.lower()

for c in ',.;:-?!()\'"':
    s=s.replace(c, '')
print (s)

