from random import *
from string import *
from pprint import pprint
from string import punctuation

#Write a class called Product. The class should have fields called name,amount,
#and price,holding the product’s name, the number of items of that product in stock, and the regular price
#of the product. There  should  be a method get_price that receives the
#number of items to be bought and returns the cost of buying that many items,
#where the regular price is charged for orders of less than 10 items,
#a 10% discount is applied for orders of between 10 and 99 items,
#and a 20% discount is applied for orders of 100 or more items.
#There should also be a method called make_purchase that receives the number
#of items to be bought and decreases amount by that much.

class Product:
    def __init__(self, name, amount, price):
        self.name=name
        self.amount=amount
        self.price=price

    def get_price(self, k):
        self.k=k
        
        if k>10:
            price = self.price*0.9
        elif k>99:
            price = self.price*0.8
        else:
            price = self.price

        self.cost = self.k*price
        
        return self.cost

    def make_purchase(self):
        self.amount = self.amount-self.k
        return 'Order: %s - %d: total %d Eur' %(self.name, self.cost, self.cost)

kava = Product('Paulig', 212, 3)




