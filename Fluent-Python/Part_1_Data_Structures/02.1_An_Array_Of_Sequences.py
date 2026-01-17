""""""
"""
The standard library offers a rich selection of sequence types implemented in C:
- Container sequences: 
  Can hold items of different types, including nested containers. Some examples: list, tuple, and collections.deque.
- Flat sequences: 
  Hold items of one simple type. Some examples: str, bytes, and array.array.
  
A container sequence holds references to the objects it contains, which may be of any type, while a flat sequence stores
the value of its contents in its own memory space, not as distinct Python objects.

Thus, flat sequences are more compact, but they are limited to holding primitive
machine values like bytes, integers, and floats.
"""