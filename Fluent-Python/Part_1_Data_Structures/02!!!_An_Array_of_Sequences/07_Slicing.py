my_list = [*range(10)]

print(my_list)
print(my_list[:])
print(my_list[::])
print(my_list[5:])
print(my_list[:5])
print(my_list[::2])
print(my_list[::-1])

"""
The notation a:b:c is only valid within [] when used as the indexing or subscript operator, and it produces a 
slice object: slice(a, b, c). To evaluate the expression seq[start:stop:step], Python calls 
seq.__getitem__(slice(start, stop, step)).
"""

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                 $4.95    2     $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
"""

DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

my_list[2:8] = [10, 20]
print(my_list)
del my_list[0:3]
print(my_list)
# my_list[1:3] = 30
# Creates an error: TypeError: can only assign an iterable
# When the target of the assignment is a slice, the rhs must be an iterable object, even if it has just one item.
my_list[1:3] = [30]
print(my_list)