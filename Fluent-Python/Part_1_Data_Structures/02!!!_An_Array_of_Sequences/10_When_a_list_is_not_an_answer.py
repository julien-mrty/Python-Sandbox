"""
The list type is flexible and easy to use, but depending on specific requirements, there are better options. For
example, an array saves a lot of memory when you need to handle millions of floating-point values. On the other hand, if
you are constantly adding and removing items from opposite ends of a list, it’s good to know that a deque
(double-ended queue) is a more efficient FIFO data structure.
"""

"""
Arrays

If a list only contains numbers, an array.array is a more efficient replacement. Arrays support all mutable sequence
operations (including .pop, .insert, and .extend), as well as additional methods for fast loading and saving, such as 
.frombytes and .tofile.
.tofile save as binary which makes data way faster to read, write and creates smaller files.

A Python array is as lean as a C array.

When creating an array, you provide a typecode, a letter to determine the underlying C type used to store each item in 
the array.
"""


"""
Memory View

The built-in memoryview class is a shared-memory sequence type that lets you handle slices of arrays without copying 
bytes.
A memoryview is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to 
share memory between data-structures (things like PIL images, SQLite databases, NumPy arrays, etc.) without first 
copying. This is very important for large data sets.
"""

from array import array
octets = array("B", range(6))
m1 = memoryview(octets)
print(m1.tolist())
m2 = m1.cast("B", [2, 3])
print(m2.tolist())
m3 = m1.cast("B", [3, 2])
print(m3.tolist())
m2[1, 2] = 50
m3[1, 1] = 30
print(octets.tolist())

"""
Deques and other Queues

The .append and .pop methods make a list usable as a stack or a queue (if you use .append and .pop(0), you get FIFO 
behavior). But inserting and removing from the head of a list (the 0-index end) is costly because the entire list must 
be shifted in memory.
The class collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends. 
It is also the way to go if you need to keep a list of “last seen items” or something of that nature, because a deque 
can be bounded, created with a fixed maximum length. If a bounded deque is full, when you add a new item, it discards an 
item from the opposite end.
There is a hidden cost: removing items from the middle of a deque is not as fast. It is really optimized for appending
and popping from the ends.
The append and popleft operations are atomic, so deque is safe to use as a FIFO queue in multithreaded applications 
without the need for locks.
"""