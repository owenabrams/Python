# ~DICTIONARIES:
# Imagine you want to store information lists ( Remember LISTS = [] ) that are separate

'''

names = ['Ana', 'John', 'Denise', 'Katy']
grades = ['B', 'A+', 'A', 'A']
course = [2.00, 6.0001, 20.002, 9.01]

# Note that info is stored at the same index in each list in order to match other lists

'''  
# Dictionary uses key and value pairs ~

my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

grades['grades'] # 'A+'
grades['Sylvan'] # gives a KeyError

grades['Sylvan'] = 'A'

'John' in grades # returns True
'Daniel' in grades # returns False

del(grades['Ana'])

grades.keys() # returns ['Denise', 'Katy', 'John', 'Ana'] NOTE: In NO GUARANTEED ORDER
grades.values()  # returns ['A', 'A', 'A+', 'B'] NOTE: In NO GUARANTEED ORDER

# The values can be anything - lists, integers, other data structures, mutable, immutable, etc
# The keys have to be unique, immutable

'''
LISTS                                                DICTIONARIES
-------------------------------------                ----------------------------------------------
ordered sequence of elements                         matches 'keys' to 'values'
look up elements by an integer index                 looks up one item by another item
indices have an order                                no order is guaranteed
index is an integer                                  key can be any immutable type

'''

# EXAMPLE: Frequency of words in a song's lyrics

def lyrics_to_frequency(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# But its not ordered so how do I figure out the most common words

def most_common_words(freqs): # freqs is a dictionary
    values = freqs.values()
    best = max(values)
    words = []
    
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

#Leveraging DICTIONARY Properties

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

beatles = [] # ?
print (words_often(beatles, 5))

# FIBONACCI WITH A DICTIONARY

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6,d))

# This above will basically first:
#   Do a lookup first in case already calculated the value
#   Modify dictionary as progress through function calls
# Memoization helps with this

# Dictionaries are vaaluable on procedure calls when those intermediate values are not going to change.










 


