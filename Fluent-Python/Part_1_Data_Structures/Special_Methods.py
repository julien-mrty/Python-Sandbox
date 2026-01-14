""""""
"""
Special methods: meant to be called by python interpreter

Python variable-sized collections has a "size" field holding the number of item in the collection.
If my_object is an instance of those built-ins, len(my_object) retrieves the "size" field -> much faster than calling a method
"""

"""
String representation:

__repr__ goal is to be unambiguous
__str__ goal is to be readable

If __str__ is not implemented, the implementation of __repr__ will be used
Must implement: __repr___
Implementing __str__ is optional
"""

"""
Boolean Value of a Custom Type

Any object can be used in a Boolean context.
"""

"""
Collection API

Example of Abstract Base Classes (ABCs):
Sized, Iterable, Collection, Mapping, Sequence

Every collection should implement:
• Iterable to support for, unpacking, and other forms of iteration
• Sized to support the len built-in function
• Container to support the in operator

Python does not require concrete classes to inherit from any of these ABCs.
Any class that implements __len__ satisfies the Sized interface.

Three very important specializations of Collection are:
• Sequence, formalizing the interface of built-ins like list and str
• Mapping, implemented by dict, collections.defaultdict, etc.
• Set, the interface of the set and frozenset built-in types
"""