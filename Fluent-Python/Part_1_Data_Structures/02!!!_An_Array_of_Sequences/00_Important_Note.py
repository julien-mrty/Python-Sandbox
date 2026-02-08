my_list = list(range(20)) # Explicit constructor
my_list2 = [range(20)] # Creates a range object in a list
my_list3 = [x for x in range(20)] # List comprehension
my_list4 = [*range(20)] # Unpacking operator

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

"""
Range creates a range object, iterable
list(...) consumes the iterable and builds a list of elements
"""