from random import *
from string import *
from pprint import pprint
from string import punctuation

#Write a class called Investment with fields called principal and interest.
#The constructor should set the values of those fields.
#There should be a method called value_after that returns the value of the
#investment after n years. The formula for this is p(1+i)n,
#where p is the principal, and i is the interest rate.
#It should also use the special method __str__ so that printing the object will
#result in something like below:
#Principal - $1000.00, Interest rate - 5.12%


class Investment:
    def __init__(self, principal, interest):
        self.principal=principal
        self.interest=interest

    def value_after(self, year):
        self.year=year
        self.val =  self.principal*(1+((self.interest*self.year)/100))
        return  'Value after %d yers: %d'%(self.year, self.val)

    def __str__(self):
        return 'Principal: %d Eur. Interest rate %d pct.' % (self.principal, self.interest)


s = Investment(1000, 8)

    
