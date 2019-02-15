from random import randint

s =input('Enter a string:')
sk = [ls for ls in s]
encrypted =''

# encrypting

print('Encrypted string:')
for i in range(len(s)):
    if i%2 == 0:
        encrypted = encrypted+s[i]
for j in range(len(s)):
    if j%2!=0:
        encrypted = encrypted+s[j]
print(encrypted)

# decrypting

encrypted_s = input('Paste in encrypted string for decryption: ') 
print('Decrypted string: ')

if len(encrypted_s)%2==0:
    for i in range(int(len(encrypted_s)/2)):
        print(encrypted_s[0+i]+encrypted_s[int(len(encrypted_s)/2)+i],end="")
    
else:
    for i in range(int(len(encrypted_s)/2)):
        print(encrypted_s[0+i]+encrypted_s[int(len(encrypted_s)/2)+1+i],end="")
    print(encrypted_s[int(len(encrypted_s)/2)])
