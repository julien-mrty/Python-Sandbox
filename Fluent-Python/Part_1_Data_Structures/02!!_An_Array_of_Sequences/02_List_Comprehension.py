""""""
"""
Remember that: Listcomps build lists
To generate data for other sequence types, a genexp is the way to go
"""
sequence = "ABCD"

# Classic way of building a list
my_list = []
for element in sequence:
    my_list.append(ord(element))

print(my_list)

# Python specific way: list comprehension
my_list_2 = [ord(element) for element in sequence]
print(my_list_2)

# Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
shirts =  [(color, size) for color in colors for size in sizes]
print(shirts)