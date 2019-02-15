from random import *
from string import *
from pprint import pprint

#  For this problem, use the dictionary from the beginning of
#this chapter whose keys are monthnames and whose values are
#the number of days in the corresponding months.
#(a)  Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
#(b)  Print out all of the keys in alphabetical order.
#(c)  Print out all of the months with 31 days.
#(d)  Print out the (key-value) pairs sorted by the number of days in each month 
#(e)  Modify the program from part (a) and the dictionary so that the user
#     does not have to know how to spell the month name exactly.
#     That is, all they have to do is spell the first three letters of the month name correctly.      

days = {'January':31,
        'February':28,
        'March':31,
        'April':30,
        'May':31,
        'June':30,
        'July':31,
        'August':31,
        'September':30,
        'October':31,
        'November':30,
        'December':31}

mon = input('Enter the name of the month: ')
print ('{} has {} days'.format(mon, days[mon]))

print('- '*30)
#################################################

list_mon = list(days.items())
list_mon.sort()

for m in list_mon:
    
    print (m[0])
print('- '*30)
###################################

print('All month with 31 days: ')

for m in days:
    if days[m]==31:
        print(m)
print('- '*30)
######################################################

print('Month sorted by days:')

d = list(days.items())
d = [(i[1], i[0]) for i in d]
d.sort()
d.reverse()
for i in d:
    print(i)

################################
    
find = input('Show the month: ')

for m in list(days):
    if find in m:
        print(m)
        break
    else:
        print('Somthing is wrong.')
        break
