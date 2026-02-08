""""""
"""
To initialize tuples, arrays, and other types of sequences, you could also start from a listcomp, but a genexp 
(generator expression) saves memory because it yields items one by one using the iterator protocol instead of building 
a whole list just to feed another constructor.
"""
symbols = '$¢£¥€¤'

# Initialize tuple from generator expression
my_tuple = tuple(ord(symbol) for symbol in symbols)
print(my_tuple)

# Initialize array from generator expression
import array
my_array= array.array("I", (ord(symbol) for symbol in symbols))
print(my_array)

"""
Usage of a generator expression to print the roster. In contrast with the list comprehension method, a list is never
built in memory, the list comprehension technique creates the list that will be printed, this add overhead. 
The generator expression feeds the loop producing one item at a time which doesn't consume extra memory.
"""
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)