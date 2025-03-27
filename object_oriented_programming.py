# In Python , everything is an object, it has a type, and it has some way we can interact with it.
"""
EVERYTHING IN PYTHON IS AN OBJECT (and has a type)
    # Can create new objects of some type
    # Can manipulate objects
    # Can destroy objects
        ~ explicitly using 'del' or just "forget" about them
        ~ python system will reclaim destroyed or innacessible objects - called "garbage collection"

Objects require abstraction of data for: 
    Representation (car's number of wheels, number of doors, length, height)
    Interaction (interface - you can paint a car, drive it, make it make some noise)
        
"""

# EXAMPLE of a ~ LIST as a Python Object
    # internal representation
        # has a value at an index location
        # has a pointer to the next index location
    # how to manipulate lists
    #   L[i], L[i:j], +
    #   len(), min(), max(), del(L[i])
    #   L.append(), L.extend(), L.count(), L.index(), L.insert(), L.pop(), L.remove(), L.reverse(), L.sort()
    
    # internal representation should be private
    # correct behaviour may be compromised if you manipulate internal representation directly

"""

This (Using 'CLASSES' for OOP) allows for:
# DECOMPOSITION
# ABSTRACTION
# REUSABILITY

"""

""" CREATING AND USING YOUR OWN TYPES WITH CLASSES"""
# make a distinction between creating a class and using an instance of the class
# creating the class object involves:
#   ~ defining the class name
#   ~ defining class attributes
#   ~ for example, someone wrote code to implement a list class

# using the class involves:
#   ~ creating new instances of objects
#   ~ doing operations on the instances
#   ~ for example, L = [1,2] and len(L)

'''
DEFINNING OUR OWN TYPES USING CLASSES
# 'A COORDINATE OBJECT' ~~~~~~~~~~~~~~~~ Defining a point in an x,y 2D plane
'''

class Coordinate (object):
    #define attributes here

# Similar to 'def', indent code to indicate which statements are part of the class definition
# the word object means that Coordinate is a Python object and inherits all its attributes (inheritance is in next lecture)
#   ~ 'Coordinate' is a subclass of 'object'
#   ~ 'object' is a superclass of 'Coordinate'

# Attrubutes    ~ are the 'data' and 'procedures' that belong to the object
    '''
    What Are Attributes?
~ data and precedures that belong to the class

# Data attributes
    ~ think of data as other objects that make up the class
    ~ for example, a coordinate is made up of two numbers

# methods (procedural attributes)
    ~ think of methods as functions that only work with this class
    ~ how to interact with the object
    ~ for example you can define a distance between two coordniate objects but there is no meaning to a distance between two list object
    
'''

    '''
    
    Defining how to create an instance of a CLASS
    ~ first have to define how to create an instance of an object
    ~ use a special method called '__init__' to initialize some data attributes
    
    class Coordinates(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
    ~ 
    
    c = Coordinate(3,4)  # You willnotice that we have two parameters here but the third one 'self', by default will be the 'c'
    
'''

class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = Coordinate (3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(origin.x)

# data attributes of an instance are called instance variables
# don't 