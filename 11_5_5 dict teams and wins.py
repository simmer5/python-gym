from random import *
from string import *
from pprint import pprint

#Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost.
#Store this information in a dictionary where the keys are the
#team names and the values are lists of the form[wins,losses].
#(a)  Using the dictionary created above, allow the user to enter a team name
#   and print outthe team’s winning percentage.
#(b)  Using the dictionary, create a list whose entries are the number of wins of each team.
#(c)  Using the dictionary, create a list of all those teams that have winning records.

teams={}

for t in range(2):
    t = input('Enter team name, wins and loses: ').split()
    teams[t[0]]=[int(t[1]),int(t[2])]

win = input('Enter team to get wins percentage: ')
total = sum(teams[win])
prc = (teams[win][0]*100/total)
print('Wins: {:.2f}%'.format(prc))

print ('Wins: ')
wins=[]
for t in teams:
    wins.append([t, teams[t][0]])
print(wins)
    

    
