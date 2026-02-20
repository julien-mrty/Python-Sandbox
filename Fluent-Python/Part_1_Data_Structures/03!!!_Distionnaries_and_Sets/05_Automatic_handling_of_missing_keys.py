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
"""
class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str): # If key is a string and is missing, raise a KeyError
            raise KeyError(key)
        return self[str(key)] # Otherwise build a str from the key and look it up