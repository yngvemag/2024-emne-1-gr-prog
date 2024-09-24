# List comprehension er en elegant og effektiv måte å lage lister på i Python.
# Det er en syntaks som gjør det mulig å lage lister basert på eksisterende lister eller itererbare objekter,
# alt på én linje.
# Dette kan ofte gjøre koden kortere og mer lesbar.

# Syntax: [uttrykk for element i itererbart_objekt hvis betingelse]

from math import sqrt

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ved list-comprehension:
list2 = [i for i in range(1, 11)]
print(list2)

list_squared = [i**2 for i in range(1, 11)]
print(list_squared)

list_root = [sqrt(i) for i in range(1, 11)]
print(list_root)


list_names = ['Yngve', 'Ola', 'Kari', 'Per']
list_names_upper_case = [name.upper() for name in list_names]
print(list_names_upper_case)

# lage gangetabellen
multiplication_table = [f'{a}*{b}={a*b}'  for a in range(1, 11) for b in range(1, 11) ]
print(multiplication_table)