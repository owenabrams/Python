#Debugging is a component of defensive programming - to make your life a bit easier.
# Test cases : Pairs of inputs and outputs
'''
Unit Testing: Test that each unit / function runs according to the specifications. If you find a bug, then you do regression testing
    ~ validate each piece of program
    ~ testing each function

Regression Testing:
    ~ add test for bugs as you find them
    ~ catch reintroduced errors that were previously fixed

Integration Testing:
    ~ does the overal program work?
    ~ tend to rush to do this

It is a cycle of tests as you go back and forth to eliminate them and prevent them from happening at all.

'''

# TESTING APPROACHES: 
'''
~~~~~ intuition ~~~~~ about natural boundaries to the problem
def is_bigger(x,y):
    "returns True if y is less than x, else False"

if no natural partitions, might do ~~~~~ random testing ~~~~~ 
    ~ probability that code is correct increases with more tests
    ~ better options below
'''
#   ~ Black Box Testing
    #   ~ explore paths through spefication of the function, such as the specifications in the 'DOC String'
    #   ~ you look at the doc string and come up with some test cases based on that
#   ~ Glass  Box Testing
    #   ~ You have the code itself and you try to come up with some test cases that hit up on all the possible paths through the code
    
# BLACK BOX TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sqrt(x, eps):
    '''Assumes x, eps floats, x >= 0, eps > 0" Returns res such that x-eps <= res*res <= x+eps 
"""
'''
#   ~ designed without looking at the code
#   ~ can be done by someone other than the implementer to avoid some implementer biases
#   ~ testing can be resused if the implementation changes
#   ~ paths through specification
#       ~ build test cases in different natural space partitions
#       ~also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)

'''
FOR THIS PARTICULAR FUNCTION ABOVE, here is a sample set of what we check for based on the 'doc string description'
def sqrt(x, eps):
    """Assumes x, eps floats, x >= 0, eps > 0"""
    
CASE                      x                   eps
____________________________________________________________________________________________________________
boundary                  0                   0.0001
perfect square            25                  0.0001
less than 1               0.05                0.0001
irrational square root    2                   0.0001
extremes                  2                   1.0/2.0**64.0
extremes                  1.0/2.0**64.0       1.0/2.0**64.0
extremes                  2.0**64.0           1.0/2.0**64.0
extremes                  1.0/2.0**64.0       2.0**64.0 
extremes                  2.0**64.0           2.0**64.0 

'''

# GLASS BOX TESTING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#   ~ you are using the code itself to guide the design of the test cases
#   ~ called path-complete if every potential path through code is tested at least once

#   ~ What are some drawbacks of this type of testing?

#       ~ can go through loops arbitrarily many times
#       ~ missing paths

#   ~ Guidelines
#       ~ branches
#           ~ exercise all parts of a conditional
#       ~ for loops
#           ~ loop not entered
#           ~ body of loop executed exactly once
#           ~ body of loop executed more than once
#       ~ while loops
#           ~ same as for loops, cases that catch all ways to exit loop

def abs(x):
    """ Assumes x is an int
    Returns x if x>=0 and -x otherwise """
    
    if x < -1:
        return -x
    else:
        return x
# ~ a path complete test suite could miss a bug
# ~ path-complete test suite: 2 and -2
# ~ but abs(-1) incorrectly returns -1
# ~ should still test boundary cases

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    HISTORY OF DEBBUGING     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
# September 9, 1947
# Mark II Aiken Relay Computer - 'addition in 0.1 secs, multiplication 0.7 secs, log - in 5 secs
# A group of engineers were working on a running a program that was supposed to find the trigonometric function but they found that the function was not operating correctly
# One of them was 'Grace Hopper' , so they went through all the panels and relays and isolated a program in PANEL F, RELAY 70, and they found a moth
# They made a note in their log book that said ' first actual case of bug being found.

######### TOOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python Tutor
# Debuggers within programs
# Print statements
# ~ inserted within loops

#BI-SECTION METHOD
#   ~ find the middle part of the code and put a print statement, then put another print statement 3 quarters etc

# DEBUGGING STEPS
#   ~Study program code
#       ~ don't ask what is wrong
#       ~ ask how did I get the unexpected result
#       ~ is it part of a family?
#
#   ~Scientific Method
#       ~ study available data
#       ~ form hypothesis
#       ~ repeatable experiments
#       ~ pick simplest input to test with
#
# As you debug, you will encounter error messages

'''

ERROR MESSAGES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
trying to access beyond the limits of a list                 ~~~~~~ IndexError
test = [1,2,3] then test[4]

trying to convert an inappropriate type                      ~~~~~~ TypeError
int(test)

refrencing a non-existent variable                           ~~~~~~ NameError
a

mixing data types without appropriate coercion               ~~~~~~ TypeError
'3'/4

forgetting to close parenthensis, quotation, etc.            ~~~~~~ SyntaxError
a = len([1,2,3]
print(a)

'''
                    # LOGIC ERRORS ARE HARD ---------------------

# RUBBER DUCKY DEBUGGING
# ~ When a programmer explains their code to a 'Rubber Ducky'!
#   ~ think before writing new code
#   ~ draw pictures, take a break
#   ~ explain the code to someone else, a rubber ducky

'''

DON'T                                                 DO
______________________________________________________________________________________________________
Write entire program                                  Write a function
Test entire program                                   Test the function, debug the function
Debug entire program                                  Write a function
                                                      Test the function, debug the function
                                                      *** Do integration testing ***
                                                      
IF YOU ARE CHANGING CODE?
______________________________________________________________________________________________________
- Remember to back up your code. Save the most recent version that worked.
- Document what worked and what didn't

Then:
. Change code
. Remember where bug was
. Test code
. Forget where bug was or what change you made
. Panic



'''

# NEXT, EXCEPTIONS! - - - - - - -
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     DEALING WITH EXCEPTIONS       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In python, we can actually write handlers to deal with exceptions 
'''
# For example below: Dealing with inputs from users
# Python code can provide handlers for exceptions

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print (a/b)
except:
    print("Bug in user input.") # users are really unpredictable, because you tell them to give you a number and they might give you a name
    # So it says, an error came up but I know how to handle it.
    

# Exceptions raised by any statement in body of try are handled by the except statement and execution continues with the body of the except statement

# ~~~~~~~~~~~~~~~~~~ HANDLING SPECIFIC TYPES OF ERRORS  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# have specific except clauses to deal with a particular type of exception

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError:
    print("Could not convert to a number. ")
except ZeroDivisionError:
    print("Can't divide by zero. ")
except:
    print("Something went wrong. ")
    
# OTHER EXCEPTIONS: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''' ELSE BLOCK '''
# else:
#   ~ body of this is executed when execution of associated 'try' body completes with no exceptions

''' FINALLY BLOCK '''
# finally:
#   ~ body of this is always executed after 'try, else and except' clauses, even if they raised another error or executed a break, continue or return
#   ~ useful for clean-up code that should be run no matter what else happened (eg. close a file)

''' WHAT TO DO WITH EXCEPTIONS?'''
# What to do when encounter an error?

#   ~ fail silently:
#       ~ substitute default values or just continue
#       ~ bad idea! user gets no warning

#   ~ return an "error" value:
#       ~ what value to choose?
#       ~ complicates code having to check for a special value

#   ~ stop execution, signal error condition:
#       ~ in Python: raise an exception
#       ~ raise Exception ("descriptive string")

''' ~~~~~~~~~~~~~~~~~~~~  EXCEPTIONS AS CONTROL FLOW  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
# don't return special values when an error occurred and then check whether 'error value' was returned
# instead, raise an exception when unable to produce a result consistent with function's specification

raise <exceptionName> (arguments)
raise ValueError ("Something is wrong") # here you have a [ keyword, name of error you want to raise, 'optional' but typically a string with a message]

# EXAMPLE OF RAISING AN EXCEPTION

def get_ratios(L1,L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    
    for index in range(len(l1)):
        
        try:
            
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))  # nan = not a number
        except:                 # manage flow of program by raising own error
            raise ValueError('get_ratios called with bad arg')
    return ratios

# ANOTHER EXAMPLE OF EXCEPTIONS
"""
Asume we are given a class list for a subject: each entry is a list of two parts
    ~ a list of first and last name for a student
    ~ a list of grades on assignments
"""

test_grades[[['peter', 'parker'], [80.0, 70.0, 85.0]],[['bruce', 'wayne'],[100.0, 80.0, 74.0]]]

# create a new class list, with name, grades, and an average

[[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333], [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.666667]]

# if class_list = [[['peter', 'parker'], [80.0, 70.0, 85.0]],[['bruce', 'wayne'],[100.0, 80.0, 74.0]]]

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades)

# ERRROR IF NO GRADE FOR A STUDENT
# if one or more students don't have any grades, get an error

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'Wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['deadpool'], []]]

# if you run the function above with this data, you get ZeroDivisionError: float division by zero becasue try to
# return sum(grades) / len(grades)

#~~~~~~~~~~~~~~~# Option 1: FLAG THE ERROR BY PRINTING A MESSAGE
                # decide to notify that something went wrong with a msg

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print ('Warning: no grades data')

                # running on the test data above gives,
'''

                warning: no grades data
                [[['peter', 'parker'], [10.0, 5.0, 85.0], 15.41666666],
                [['bruce', 'Wayne'], [10.0, 8.0, 74.0], 13.83333334],
                [['captain', 'america'], [8.0, 10.0, 96.0], 17.5],
                [['deadpool'], [], None]]

                '''
                
#~~~~~~~~~~~~~~~# Option 2: CHANGE THE POLICY
                # decide that a student with no grades gets a zero

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print ('Warning: no grades data')
        return 0.0

                # running on the test data above gives,
'''

                warning: no grades data
                [[['peter', 'parker'], [10.0, 5.0, 85.0], 15.41666666],
                [['bruce', 'Wayne'], [10.0, 8.0, 74.0], 13.83333334],
                [['captain', 'america'], [8.0, 10.0, 96.0], 17.5],
                [['deadpool'], [], 0.0]]

                '''
                
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ASSERTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Is a Good example of defensive programming, to have assert statements at the beginning of a function (typically) or at the end.

# Example
def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades) / len(grades)

# raises an AssertionError if it is given an emptry list for grades
# if the assertion is false, the function will immeadiately stop and terminate
# otherwise runs ok

'''
WHERE TO USE ASSERTIONS?
# goal is to spot bugs as soon as they are introduced and make clear where they happened
# use as a supplement to testing
# raise exceptions if users supplies bad data input
# use assertions to
    ~ check types or arguments or values
    ~ check that invariants on data structures are met
    ~ check constraints on return values
    ~ check for violations of constraints on procedure (e.g. no duplicates in a list)
    ~
'''



