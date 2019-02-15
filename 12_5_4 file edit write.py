from random import *
from string import *
from pprint import pprint

#There is a name,  an email address,  and a phone number,
#each separated by tabs. Write aprogram that reads through
#the file line-by-line, and for each line, capitalizes
#the first letter of the first and last name and adds
#the area code 301 to the phone number.
#Your programshould write this to a new file called students2.txt.
#Here is what the first line of the newfile should look like:
#    Walter Melon        melon@email.msmary.edu        301-555-3141
    
with open('students.txt', 'r+') as f:
    print('walter melon melon@email.msmary.edu 555-3141', file=f)
    print('volker texas volker@email.msmary.edu 222-3451', file=f)

L = [line.split() for line in open('students.txt')]
f = open('students_edited.txt', 'w')
for i in L:
    print (i[0].capitalize(),' ',i[1].capitalize(),' ', i[2], ' ', '301-'+i[3], file=f)
f.close()
S = [info for info in open('students_edited.txt')]
print(S)

