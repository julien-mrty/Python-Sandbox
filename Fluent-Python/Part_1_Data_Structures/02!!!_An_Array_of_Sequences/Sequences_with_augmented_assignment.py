""""""
import dis

"""
The special method that makes += work is __iadd__ (for “in-place addition”). However, if __iadd__ is not implemented, 
Python falls back to calling __add__. Consider this simple expression:
a += b
If a implements __iadd__, that will be called. In the case of mutable sequences (e.g., list, bytearray, array.array), a 
will be changed in place (i.e., the effect will be similar to a.extend(b)). However, when a does not implement __iadd__,
the expression a += b has the same effect as a = a + b: the expression a + b is evaluated first, producing a new object, 
which is then bound to a. In other words, the identity of the object bound to a may or may not change, depending on the 
availability of __iadd__.

*= and __imul__ works with the same idea.
"""

l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))
t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))

"""
Repeated concatenation of immutable sequences is inefficient, because instead of just appending new items, the 
interpreter has to copy the whole target sequence to create a new one with the new items concatenated.
str is an exception to this description. Because string building with += in loops is so common in real codebases, 
CPython is optimized for this use case. Instances of str are allocated in memory with extra room, so that concatenation 
does not require copying the whole string every time.
"""

# Get the bytecode of an expression
dis.dis("l.append(4)")