from random import *
from string import *
from pprint import pprint

#Write a program that takes a list of ten prices and ten products,
#applies an 11% discount toeach of the prices displays the output like
#below, right-justified and nicely formatted

K = [23, 45, 23, 155, 12]
P = ['Kava', 'Ledas', 'Alus', 'Pienas', 'Suris']

for k in range(len(P)):
    print('{:>10s} : {:>6.2f} Eur'.format(P[k],(K[k]-(K[k]*.11))))
