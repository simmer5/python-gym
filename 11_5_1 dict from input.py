from random import *
from string import *
from pprint import pprint

#Write a gram that repeatedly asks the user to enter product names and prices.
#Store all of these in a dictionary whose keys are the product
#names and whose values are the prices. When the user is done entering
#products and prices, allow them to repeatedly
#enter a productname and print the corresponding
#price or a message if the product is not in the dictionary.
        
products ={}                     
for i in range(3):        
    product = input('Enter product name and price: ').split()
    products [product[0]]=int(product[1])     
print(products)

find = input('Finde a product: ')
if find in products:
    print('Price: ', products[find])
else:
    print('No product like this.')

suma = sum([products[i] for i in products])

print('Total: ', suma)

        
