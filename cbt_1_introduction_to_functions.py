# The 'DRY' principle - Don't Repeat Yourself
# Functions will always return something - 'None' by default

''' ~~~~~~~~~~~~~~~~~~~~~~~~ EXPLORING BUILT-IN FUNCTIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '''
# www.docs.python.org/3/Functions.html
''' 
help(print)
    print(value, ..., sep='', end='\n', file=stdout, flush=False)
    
    '''

def print_function(names):
    
    print(names)
    return names

names = input("Types names separated by a space: ").split(" ")

# test numbers in a list using in-built function 'isinstance'
def check_for_number_in_list(my_list):
    
    for num in my_list:
        if isinstance(num, list):
            for n in num:
                if num == 15:
                    print("15 exists")
        else:
            if num == 2:
                    print("2 exists")

my_list = [1,2,3,[2,2, 15, 5], 6, 45, 78]

if __name__ == "__main__":
    print_function(names)
    check_for_number_in_list(my_list)