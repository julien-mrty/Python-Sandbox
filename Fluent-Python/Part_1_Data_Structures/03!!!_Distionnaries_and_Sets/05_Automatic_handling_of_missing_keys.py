"""
A collections.defaultdict instance creates items with a default value on demand whenever a missing key is searched using
d[k] syntax.
"""
import collections

index = collections.defaultdict(list)
index["a"].append(1)
index["a"].append(2)
index["b"].append(3)
print(index)
# IMPORTANT:
print(index.get("c"))
print(index["c"])
"""
Still returns None and not a dict because: The default_factory of a defaultdict is only invoked to provide default 
values for __getitem__ calls, and not for the other  methods. For example, if dd is a defaultdict, and k is a missing
key, dd[k] will call the  default_factory to create a default value, but dd.get(k) still returns None, and k in dd is 
False.
"""


"""
The __missing__ Method

A better way to create a user-defined mapping type is to subclass collections.UserDict instead of dict. Here we subclass
dict just to show that __missing__ is supported by the built-in dict.__getitem__ method.
"""
class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str): # If key is a string and is missing, raise a KeyError, otherwise infinite recursion
            raise KeyError(key)
        return self[str(key)] # Otherwise build a str from the key and look it up

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    # Essential because the method inherited from dict doesn't fall back to str(key)
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
""" 
There is a subtle detail in our implementation of __contains__: we do not check for the key in the usual Pythonic 
way k in my_dict because str(key) in self would recursively call __contains__. 
A search like k in my_dict.keys() is efficient in Python 3 even for very large mappings because dict.keys() returns a 
view, which is similar to a set. However, remember that k in my_dict does the same job, and is faster because it avoids  
the attribute lookup to find the .keys method.
"""

my_dict = StrKeyDict()
# print(my_dict[1]) KeyError: '1'
print("Example key 1:")
print(my_dict.get("1"))
my_dict["1"] = [1, 2, 3]
print(my_dict.get("1"))
print(my_dict.get(1)) # Works too !

# BUT, it's a custom str dict so:
print(f"\nExample key 2:")
print(my_dict.get(2))
my_dict[2] = [4, 5, 6]
print(my_dict.get(2))
print(my_dict.get("2")) # No fall back because the initially created key is an int

"""
When subclassing dict and implementing __missing__:
- d[k] calls dict.__getitem__
- if the key is missing calls dict.__missing (overloaded by you)
BUT:
dict.get(k) doesn't call __getitem__
The built-in dict.get() is implemented in C and:
- Looks up the key directly
- If missing → returns None (or the default). It does not trigger __missing__

When subclassing collections.UserDict and implementing __missing__:
UserDict is written in pure Python, not C.
- d[key] calls __getitem__
- d.get(key) calls __getitem__
- __getitem__ triggers __missing__ if the key is missing

Key differences:
dict is a built-in C type, UserDict is a Python wrapper class
"""