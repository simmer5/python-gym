from random import *
from string import *
from pprint import pprint

# Write a program that uses a dictionary that contains ten user names and passwords.
# The program should ask the user to enter their username and password.
# If the username is not in the dictionary, the program should indicate that
# the person is not a valid user of the system. If the username is in the dictionary,
# but the user does not enter the right password, the program should say
# that the password is invalid. If the password is correct, then the program
# should tell the user that they are now logged in to the system.


users = {'mynde':'pynde',
        'kava':'kakava'}

u = input('Enter User Name: ')
p = input('Enter Password: ')

if u in users:
    if p==users[u]:
        print('You are logged in, {}!'.format(u))
    else:
        print('Wrong password!')
else:
    print('NO user like this.')



