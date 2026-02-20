index = {"a":[1], "b":[2], "c":[3]}
index.setdefault("a", []).append(4)
print(index)

# The actions performed are equivalent to:
if "a" not in index:
    index["a"] = []
index["a"].append(4)
print(index)
# In the latter case, you perform 2 or 3 searches of the key in the dict
# The first example does it all in one lookup
