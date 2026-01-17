""""""
"""
By implementing special methods, your objects can behave like the built-in types, enabling the expressive coding style.

A basic requirement for a Python object is to provide usable string representations of itself, one used for debugging 
and logging, another for presentation to end users. That is why the special methods __repr__ and __str__ exist in the 
data model.

Emulating sequences, as shown with the FrenchDeck example, is one of the most common uses of the special methods. For 
example, database libraries often return query results wrapped in sequence-like collections.

Thanks to operator overloading, Python offers a rich selection of numeric types, from the built-ins to decimal.Decimal 
and fractions.Fraction, all supporting infix arithmetic operators. The NumPy data science libraries support infix 
operators with matrices and tensors.

More concretely: Infix operators are operators written between operands (like a + b), and Python lets many numeric types 
(built-in, Decimal, Fraction, NumPy arrays) overload these operators so the same syntax works for scalars, rationals, 
and tensors.
"""