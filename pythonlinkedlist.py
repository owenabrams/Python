class Node:
    def __init__(self):
        self.element = None
        self.next_node = None

def linked_list():
    ''' This requires that we simply know the first one ( ll=Node() ) then replicate it'''
    ll = Node()
    ll.element = 5
    ll.next_node = Node ()
    ll.next_node.element = 3
    ll.next_node.next_node = Node ()
    ll.next_node.next_node.element = 13
    ll.next_node.next_node.next_node = Node ()
    ll.next_node.next_node.next_node.element = 4
    ll.next_node.next_node.next_node.next_node = Node ()
    ll.next_node.next_node.next_node.next_node.element = 30
    
    print(ll.element, ll.next_node.element, ll.next_node.next_node.element, ll.next_node.next_node.next_node.element, ll.next_node.next_node.next_node.next_node.element)


def linked_list_1():
    ''' This method requires that you type every node etc therefore if they are many . . .'''
    n1 = Node() # create an object of type node - remember it has two things in it - the element and the next node
    n1.element = 5
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
    n5.next_node = 30
    


if __name__ == "__main__":
    linked_list()