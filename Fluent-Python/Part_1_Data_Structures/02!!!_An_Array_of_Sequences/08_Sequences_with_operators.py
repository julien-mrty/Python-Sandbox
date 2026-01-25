"""
/!\
Both + and * always create a new object, and never change their operands
"""
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

"""
Beware of expressions like a * n when a is a sequence containing mutable items. For example, trying to initialize a list
of lists as my_list = [[]] * 3 will result in a list with three references to the same inner list.
"""
my_list = [[]] * 3 # The three outer lists contain a reference to the same inner list
my_list[0].append(1)
print(my_list)