
s=''        
with open('test-failas.txt', 'a+') as f:
    counter =0
    for i in range(10):
        if s != 'stop':
            s = input('String eilute: ')
            if s != 'stop':
                f.write(str(counter+1)+'. '+s+'\n')
                counter=counter+1
                continue
            else:
                print ('Tiek eiluciu irasyta: {}'.format(counter))
        
if find in ss:
    print('Zodis {} yra sitam tekste! Vieta - {}'.format(find.upper(), ss.index(find)))
    
else:
    print('Zodzio <<{}>> nera sitam tekste'.format(find))
    
