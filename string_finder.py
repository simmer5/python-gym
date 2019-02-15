ss = 'The + operator can be used to build up a string, piece by piece, analogously to the waywe built up counts and sums in Sections 5.1 and 5.2.'
find = input('Ieskomas zodis: ')

for i in range(len(ss)):
    if find in ss:
        print('Zodis {} yra sitam tekste! Vieta - {}'.format(find.upper(), ss.index(find)))
        break
    else:
        print('Zodzio <<{}>> nera sitam tekste'.format(find))
        break

if find in ss:
    print('Zodis {} yra sitam tekste! Vieta - {}'.format(find.upper(), ss.index(find)))
    
else:
    print('Zodzio <<{}>> nera sitam tekste'.format(find))

    
