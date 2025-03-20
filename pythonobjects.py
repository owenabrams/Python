'''
x = int(input('Enter an integer:'))
if x%2 == 0:
    print('')
    print(x, 'Is an Even number')
else:
    print('')
    print(x, 'Is an Odd number')

print('Done with conditional')
''' 

'''

i%j  - the remainder when i is divided by j
i**j - i to the power of j
i//j - int division - result is int, quotient without remainder
i/j  - division - result is a float

--- 'If both are floats result is float, if both are ints, result is int' ---
i*j  - the product 
i-j  - the difference
i+j  - the sum

--- 'Operator precedence without parenthesis' executed left to right, as appear in expression ---
**
*
/
+ and -

--- 'Operator precedence with parenthesis' executed left to right, as appear in expression ---
3*5+1 = 16
3*(5+1) = 18

'''

'''
A list in python is actually created by an array!
LINKED LISTS VS ARRAY
'''

# LINKED LIST is a linear data structure that stores data in a data object called a node that allows for efficient insertion and deletion!

# --- LINKED LIST --- is a node object that has an element and a pointer 
# --- ARRAY --- has a fixed set of items

# object7 -> object5 -> object3 -> object13 -> object4 -> object30 -> none
# 7 -> 5 -> 3 -> 13 -> 4 -> 30 (arrays are usually hiden below the datastructures because, a list in python is actually created by an array)

# With Arrays, you have to move everything upfront or backwards if you are inserting at the begining or inserting at the end
#Look-Ups are not effective in Linked Lists

# NOW LET'S TURN DRAWINGS INTO CODE!

class Node:
    def __init__(self, element = None, next_node = None):
        self.element = element
        self.next_node = next_node
    
    #def __init__(self):
    #    self.element = None
    #    self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert_first(self, element):
        n = Node(element) # create the element first
        n.next_node = self.head
        self.head = n
        
    def insert_last(self, element):
        n = Node(element) # create the element first
        m = self.head
        while m.next_node is not None:
            m = m.next_node
        m.next_node = n
    
    def print_list(self):
        n = self.head
        print("[", end='') # Eye Candy - also - NO New Line (end='')
        while n is not None:
            print(n.element, '', end='')
            n = n.next_node
        print("]") # print a new line

def linked_list():
    ll = LinkedList()
    ll.insert_first(30)
    ll.insert_first(4)
    ll.insert_first(13)
    ll.insert_first(3)
    ll.insert_first(5)
    ll.print_list()
    ll.insert_first(7)
    
    ll.print_list()
    ll.insert_last(9)
    
    ll.print_list()

'''
def print_list(n):
    while n is not None: 
        print(n.element, '', end='')
        n = n.next_node
    print() # print a new line
'''

def linked_list_3():
    ll = Node(5, Node(3, Node(13, Node(4, Node(30)))))
    # [Old print statement before the print function above] print(ll.element, ll.next_node.element, ll.next_node.next_node.element, ll.next_node.next_node.next_node.element, ll.next_node.next_node.next_node.next_node.element)
    ll = Node(7, ll)
    print_list(ll)

def linked_list_2():
    ll = Node()
    ll.element = 5
    ll.next_node = Node()
    ll.next_node.element = 3
    ll.next_node.next_node = Node()
    ll.next_node.next_node.element = 13
    ll.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.element = 4
    ll.next_node.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.next_node.element = 30
    # print(ll.element, ll.next_node.element, ll.next_node.next_node.element, ll.next_node.next_node.next_node.element, ll.next_node.next_node.next_node.next_node.element)


def linked_list_1():
    n1 = Node()
    n1.element = 5 # (we could have pointed to n2 but we have to create the n2 node first)
    n2 = Node()
    n1.next_node = n2
    n2.element = 3
    n3 = Node()
    n2.next_node = n3
    n3.element = 13
    n4 = Node()
    n3.next_node = n4
    n4.element = 4
    n5 = Node()
    n4.next_node = n5
    n5.element = 30


if __name__ == "__main__":
    linked_list()





































    
    