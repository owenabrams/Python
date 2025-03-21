# Compound data structures
'''
TUPLE - Immutable like strings - can contain anything

'''
te = () # empty tuple
t = (2, "mit", 3)

t[0] # evaluates to 2
(2,"mit", 3) + (5,6) # evaluates to (2, "mit", 3, 5, 6)

# ~ SLICING

t[1:2] # evaluates to ("mit",) - comma indicates it is a tuple string, otherwise, python may think that this is a string
t[1:3] # evaluates to ("mit", 3)
len(t) # evaluates to 3
t[1] = 4 # gives error, can't modify object

# USES of TUPLES
# ~ Conveniently used to swap variable values

x = y
y = x

# The code above won't work, because you overwrite the first variable, Therefore, to swap, 
temp = x
x = y
y = temp

# Where as if we were using a tuple, it would be simple as below

(x,y) = (y,x)

# Tuples can be used to return more than one value from a function
# NOTE - FUNCTIONS allow you to return only one value, but you can use a tuple if you want to return more values
# For example returning a remainder

def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    
    return (q,r)

(quot,rem) = quotient_and_remainder(4,5)

# EXAMPLE WITH A TUPLE OF TUPLES ~ can iterate over tuples
# aTuple:((int,string), (int,string), (int,string))
# continued under 'lists.py'