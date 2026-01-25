lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # unpacking
print(latitude)
print(longitude)

# Swapping values without temporary variables
a = 1
b = 0
a, b = b, a
print(a, b)

# Unpacking with *
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

# Grab excess items
a, b, *rest = range(5)
print(rest)
a, b, *rest = range(2)
print(rest)

print(range(4), 4)
print(*range(4), 4)
