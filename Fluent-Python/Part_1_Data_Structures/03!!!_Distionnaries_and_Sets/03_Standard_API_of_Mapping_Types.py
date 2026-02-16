import collections.abc as abc

"""
The main value of the ABCs is documenting and formalizing the standard interfaces for mappings, and serving as criteria 
for isinstance tests in code that needs to support mappings in a broad sense:
"""
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))
print(isinstance(my_dict, abc.MappingView))

""" Hashable"""
tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
"""
print(hash(tl))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))