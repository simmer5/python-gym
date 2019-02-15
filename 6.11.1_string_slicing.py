s = input('Enter a string: ')

print('Raidziu skaicius zodyje yra: {}.'.format(len(s)))

print('Three firs letters : '+s[:3])
print('Three las letters: '+s[-3:])
print('Last letter: '+s[-1:])
print('Revers:')
for i in range(len(s)):
    print(s[(-1)-i], end='' )
print()




