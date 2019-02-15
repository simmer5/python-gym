s='abcdefghijklmnopqrstuvwxyz'

#firs letter to the end

for i in range(27):
    print(s[i:len(s)]+s[0:i])
