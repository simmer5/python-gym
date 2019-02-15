from random import randint




a = [x for x in range(1, 6)]
l = [x for x in range(1, 6)]

#last first
for x in range(5):
    l.insert(0, l.pop())
    print(l)

print('# '*8)

#first back
for item in a:
    a = a[1:]
    a.append(item)
    print(a)
