# WHAT IS  Recursion - "Mise en abyme" OR the "Droste effect" - a picture within a picture
# The process of repeating items in a self-similar way
'''
French "put in the abyss", [miːz ɒn əˈbɪːm]) is a transgeneric and transmedial technique that can 
occur in any literary genre, in comics, film, painting or other media. It is a form of similarity and/or repetition, and hence a variant of self-reference
'''

# SOLUTION:
# How many twists does it take to screw in a light bulb? 
# Is it already screwed in? Then zero. If not, then twist it once, ask me again, and add 1 to my answer....


# WHAT is RECURSION? ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Algorithmycally: ~~~~~~~~ a way to design solutions to problems by 'dividing-and-conquer' or 'decrease-and-conquer'
# - in other words, to reduce a problem to a simpler version of the same problem

# Semantically: ~~~~~~~~ a programming technique where 'a function calls itself'
# - in programming, the goal is NOT to have an infinite recursion
# - must have 1 or more base cases that are easy to solve
#- must solve the same problem on some other input with the goal of simplifying the larger problem input
#

# EXAMPLE:  ~~~~~~~~ ITERATIVE ALGORITHMS
# looping constructs (while and for loops) lead to iterative algorithms, they can capture computation in a set of 'state variables' that can update on each iteration through loop

# MULTIPLICATION (ITERATIVE)
# multiply 'a * b' is equivalent to "add a to itself b times"
# capture state by 
# - an iteration number (i) starts at b
#       i <- i-1 and stop when 0
# - a current value of computation (result)
#       result <- result + a

def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# NOTE: We have two things here.
# 1: Recursive Step:
#   think of how to reduce the problem into a simpler / smaller version of the same problem
#   a + a*(b-1)
#
# 2: Base Case:
#   Keep reducing until you reach a simple case that can be solved directly
#   When b = 1, a*b = a
#
#

def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

a = 5
b = 4
answer = mult(a,b)
print(answer)

#  Another problem - FACTORIAL (RECUSRSIVE)
# n! = n*(n-1)*(n-2)*(n-3)* ... * 1
# For what 'n' do we know the factorial?
'''
n = 1 therefore if n == 1:
                    return 1
'''
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
n = 4
print(fact(7))

#Compare above with FACTORIAL ITERATIVE - 
# you will find that recursion is much simpler, more intuitive, maybe efficient for programmer and computer 

def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *=1
    return prod

# MATHEMATICAL INDUCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Some mathematical statement that runs over integers
# If I want to prove some statement that runs over integers (indexed on integers), if I want to prove that it is true
# for all values of those integers, MATHEMATICALLY, I only have to prove that it is true for the smallest value of n
# typically n == 0 or n == 1, THEN I do an interesting thing, I say that if it is true for an arbitrary value of n, then 
# am just gonna prove that it is also true for n+1 - IF I can do these two things, I can then conclude that for any 
# infinite number of values of n, it is always true!

# EXAMPLE of INDUCTION - 
#  . . . . 0 + 1 + 2 + 3 + ... + n = (n(n+1))/2 
# Proof:
# - If n = 0, then LHS is 0 and RHS is 0*1/2 = 0, so true
# Assume true for some k, then need to show that
#       0 + 1 + 2 + ... + k + (k+1) = ((k+1)(k+2))/2
#
# - . . . continued explanation

 # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~  This above is how RECURSION IN PROGRAMMING WORKS! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 


# # # # # # #    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TOWERS OF HANOI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ## # # # # # 

'''
# 
'''

def printMove(fr, to):
    print("move from " + str(fr) + " to " + str(to))

def Towers(n, fr, to, spare):
    if n==1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
fr = "A"
to = "B"
spare = "C"
n = 4

#print(Towers(n, fr, to, spare))

# Example 2: TOWERS OF HANOI
# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
        
# Driver code
n = 4
#TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods

'''
RECURSION WITH MULTIPLE BASE CASES
'''
# Fibonacci Numbers
# Leonardo of Pisa (aka Fibonnaci) modeled the following challenge
'''
    ~ Newborn pair of rabbits (one female, one male) are put in a pen.
    ~ Rabbits mate at age of one month.
    ~ Rabbits have a one month gestation period.
    ~ Assume rabbits never die, that female always produces one new pair (one male, one female) every month from its second month on.
    ~ How many female rabbits are there at the end of one year?
    ~
    Month Females
    0     1 
    1     1
    2     2
    3     3
    4     5
    5     8
    
    Two recursive calls with different sizes of arguments, compared to Towers of Hanoi, which also had two recursive calls but with the same size of call
    '''
# Now we need two base cases (to return the fibonacci of x in the example below)

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# RECURSION ON NONE NUMERICS
'''
How to check if a string of characters is a palindrome, i.e reads the same forwards and backwards
 # "Able was I, ere I sa Elba" ~ attributed to Napoleon
 # "SATOR AREPO TENET OPERA ROTAS"  ~ the SATOR SQUARE
 # "Are we not drawn onward, we few, drawn onward to new era?" # attributed to Anne Michaels
 Individual words
The words are in Latin, and the following translations are known by scholars:[2][6]

SATOR
(nominative noun; from serere, "to sow") sower, planter, founder, progenitor (usually divine); originator; literally 'seeder';[2][6]
AREPO
unknown word, perhaps a proper name, either invented to complete the palindrome or of a non-Latin origin (see § Arepo interpretations);[2][6]
TENET
(verb; from tenere, 'to hold') he/she/it holds, keeps, comprehends, possesses, masters, preserves, sustains;[2][6]
OPERA
(ablative [see opera] singular noun) service, pains, labor; care, effort, attention;[2][6]
ROTAS
(rotās, accusative plural of rota) wheels. [2][6]
Sentence construction

Sator form of the square on a door in Grenoble, France
The most direct sentence translation is: "The sower (or, farmer) Arepo holds the wheels with care (or, with care the wheels)".[1][10][14][4][17] 
Similar translations include: "The farmer Arepo works his wheels",[18] or "Arepo the sower (sator) guides (tenet) the wheel (rotas) with skill (opera)".[19]
'''
# Solving Recursively?
 # - First, convert the string to just characters, by stripping out the punctuation, then convert uppercase to lower case
 # - Then:
    # ~ Base case: a string of length 0 or 1 is a palindrome
    # ~ Recursive case:
        # - If the first character matches the last character, then is a palindrome if the middle section is a palindrome

'''
'Able was I, ere I saw Elba' -> 'ablewasiereisawelba'
isPAlindrome ('ablewasiereisawleba')
 is same as:
    'a' == 'a' and isPalindrome('blewasiereisawelb')
'''

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s [0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

s = "SATOR AREPO TENET OPERA ROTAS"
print(isPalindrome(s))

#NExt: Dictionaries

if __name__ == "__main__":
    mult(a,b)
    fact(n)
    #Towers(n, fr, to, spare)
    isPalindrome(s)

 