L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 # L3 is [2,1,3,4,5,6] while L1 and L2 are unchanged

L1.append(5) # L1 is now [2,1,3,5] "object_name.do_something()"

L1.extend([0,6]) # Mutates L1 to [2,1,3,0,6]




L - [2,1,3,6,3,7,0]
L.remove(2) # L = [1,3,6,3,7,0]
L.remove(3) # L = [1,6,3,7,0] will remove the first 3 ONLY
del(l[1]) # L = [1,3,7,0]
L.pop() # returns 0 and mutates L by removing the last element in the list - L = [1,3,7]
# the above 'dot operatio' "L.pop()", returns the removed element after removing it from the list

#Converting and back
list(s) # returns a list with every character from s as an element in L
    s.split() # split a string on a character parameter, will split on spaces if called without a parameter s.plit(" "), s.split(",")
    .join(L) # to turn a list of characters into a string, can give a character in quotes to add char between every element


#NOTE: 'join() and split() are opposites

s ="Iv3 cs" # here s is a string - "Iv3 cs"
list(s)  # returns ['I','<','3',' ','c','s']
s.split('<')  # returns ['I', '3 cs']
L = ['a','b','c']  # L is a list
''.join(L)  # returns "abc"
'_'.join(L)  # returns "a_b_c"

# OTHER List operations
# sort(), sorted(), reverse()

L = [9,6,0,3]
sorted(L)   # returns sorted list, does not mutate L []
L.sort()     # mutates L = [0,3,6,9]
L.reverse()  # mutates L = [9,6,3,0]

# ~~~~~~~~~~~~~~~~~~~~~~ LISTS and ALIASES ~~~~~~~~~~~~~~~~~~~~~~
# Lists are mutable so they are affected by 'ALIASING'
# hot is an alias for warm - changing one, changes the other
# append() - has a side effect

a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']  # warm is - ['red', 'yellow', 'orange']
hot = warm                          # hot is warm, which is - ['red', 'yellow', 'orange']
hot.append('pink')  # hot = warm + 'pink'
print(hot)    # ['red', 'yellow', 'orange', 'pink']
print(warm)   # ['red', 'yellow', 'orange', 'pink']

# ~~~~~~~~~~~~~~~~~~~~~~ If you want to create an entire copy of the list, you have to CLONE it ~~~~~~~~~~~~~~~~~~~~~~
# Use this '[:]'next to the list you want to clone - basically this is similar to slicing i.e 
# [:] - 0 : len()

cool = ['blue', 'green', 'grey'] 
chill = cool[:]
chill.append('black')   # Only alters the copy to - ['blue', 'green', 'grey', 'black']
print(chill)            # Chill has changed to - ['blue', 'green', 'grey', 'black']
print(cool)             # Cool stay original - ['blue', 'green', 'grey']



# ~~~~~~~~~~~~~~~~~~~~~~   SORTING LISTS  ~~~~~~~~~~~~~~~~~~~~~~ 

# calling sort(),   mutates the list, returns nothing
# calling sorted()  does not mutate the list, must assign to a variable 

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)


# ~~~~~~~~~~~~~~~~~~~~~~   APPENDING LISTS of LISTS is affected by Aliasing  ~~~~~~~~~~~~~~~~~~~~~~ 
# can have nested lists
# side effect still possible after mutation

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)


# ~~~~~~~~~~~~~~~~~~~~~~   MUTATION & ITERATION in lists ~~~~~~~~~~~~~~~~~~~~~~ 
# avoid mutating a list as you are iterating over it

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1,L2)

# L1 is [2,3,4] not [3,4] Why?
'''
Because:
 - Python uses an internal counter to keep track of index it is in the loop
 - mutating changes the length of the list but python doesn't update the counter
 - loop never sees element 2
'''
# Solution here to to copy the list, iterate over the list copied, then modify the original list

def remove_dups(l1,L2):
    L1_copy = L1 [:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
            
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1,L2)













