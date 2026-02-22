"""""""""
collections.OrderedDict

Now that the built-in dict also keeps the keys ordered since Python  3.6, the  most common reason to use OrderedDict is 
writing code that is backward compatible with earlier Python versions. Having said that, Python’s documentation lists 
some remaining differences between dict and OrderedDict, which I quote here—only reordering the items for relevance in
daily use:
• The equality operation for OrderedDict checks for matching order.
• The  popitem() method of OrderedDict has a different signature. It accepts an optional argument to specify which item 
  is popped.
• OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.
• The regular dict was designed to be very good at mapping operations. Tracking insertion order was secondary.
• OrderedDict was designed to be good at reordering operations. Space efficiency, iteration speed, and the performance 
of update operations were secondary.
• Algorithmically, OrderedDict can handle frequent reordering operations better than dict. This makes it suitable for 
tracking recent accesses (for example, in an LRU cache).
"""

"""
collections.ChainMap

A ChainMap instance holds a list of mappings that can be searched as one. The lookup is performed on each input mapping
in the order it appears in the constructor call, and succeeds as soon as the key is found in one of those mappings. 
For example:
"""
d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap
chain = ChainMap(d1, d2)
print(chain['a'])
print(chain['c'])
"""
The ChainMap instance does not copy the input mappings, but holds references to them. Updates or insertions to a 
ChainMap only affect the first input mapping. Continuing from the previous example:
"""
chain['c'] = -1
print(d1)
print(d2)

"""
collections.Counter

A mapping that holds an integer count for each key. Updating an existing key adds to its count. This can be used to 
count instances of hashable objects or as a multiset. Counter implements the + and - operators to combine tallies, and
other useful methods such as most_common([n]), which returns an ordered list of tuples with the n most common items and 
their counts. Here is Counter used to count letters in words:
"""
from collections import Counter
ct = Counter('abracadabra')
print(ct)
ct.update('aaaaazzz')
print(ct)
print(ct.most_common(3))


"""
shelve.Shelf

The shelve module in the standard library provides persistent storage for a mapping of string keys to Python objects
serialized in the pickle binary format. The curious name of shelve makes sense when you realize that pickle jars are 
stored on shelves.
The shelve.open module-level function returns a shelve. Shelf instance, a simple key-value DBM database backed by the 
dbm module, with these characteristics:
• shelve.Shelf subclasses abc.MutableMapping, so it provides the essential methods we expect of a mapping type.
• In addition, shelve.Shelf provides a few other I/O management methods, like sync and close.
• A Shelf instance is a context manager, so you can use a with block to make sure it is closed after use.
• Keys and values are saved whenever a new value is assigned to a key.
• The keys must be strings.
• The values must be objects that the pickle module can serialize.
"""