a = [1, 2, 3]
b = a
a += [4, 5, 6] # Mutate the object
print("b: ", b)
a.append(7) # Mutate the object
print("b: ", b)
a[6] = 8 # Mutate the object
print("b: ", b)
a = [9, 10] # Rebind a, b still points to the original object
print("b: ", b)

c = [1, 2, 3]
d = c
c = c + [4, 5, 6] # Creates a new object, b still points to the original object
print("d: ", d)


tuple = (1, "azer", 15.9)
for x in tuple:
    print(x)

for i in range(len(tuple)):
    print(tuple[i])

x = {2, 4, 6}
y = {2, 4}
print(y < x) # Subset

x = 3
y = 2
result = y and x / y
print(result)

def f(x=None):
    if not x:
        return False
    return True

print(f())
print(f([])) # Both None and empty list are considered "not"
print(f([1]))

#Stared variable
list = [1, 2, 3, 4, 5]
a, b, *extra = list
print(extra)
a, *extra, b  = list
print(extra)
*extra, a, b = list
print(extra)

a = [0, *list, 6]
print(a)