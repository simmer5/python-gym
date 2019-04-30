def factorial(x):
	if x==1: # base case stops function. without it runs infinite
		return 1
	else:
		return x*factorial(x-1)

print(factorial(5))


def sum_to(y):
	if y == 0:
		return y
	else:
		return y + sum_to(y-1)

print (sum_to(5))

#==============================
#Recursion can also be indirect. One function can call a second, 
#which calls the first, which calls the second, and so on. 
#This can occur with any number of functions.
#==============================

def is_even(z):
    if z == 0:
        return True
    else:
        return is_odd(z-1)

def is_odd(z):
    return not is_even(z)



print(is_even(0))
print(is_odd(0))

def fib(x):
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)
		
print(fib(4))