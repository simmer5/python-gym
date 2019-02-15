abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'

message = input('Your message: ')
message = message.lower()
print('Your secret mesage')

for letter in message:
    if letter.isalpha():
        print(key[abc.index(letter)], end='')
    else:
        print(letter, end='')
print('\n'+('-'*40))

#converter

secret_message = input('Paste your secret message here: ')
print('Converted message: ')
for letter in secret_message:
    if letter.isalpha():
        print(abc[key.index(letter)], end='')
    else:
        print(letter, end='')
