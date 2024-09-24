# lambda funksjoner er små definert med key-word 'lambda'
# Brukes når du trenger små og simple funksjoner uten å måtte definere en funksjon med 'def'

# Syntax: lambda arguments: expression

#%%
# lage en lambda som dobler tallet ditt
def double_my_number_def(nr: int) -> int:
    return nr * 2


# samme funksjon, bare nå med lambda
double_my_number_lambda = lambda nr: nr * 2

#
print(double_my_number_def(10))
print(double_my_number_lambda(10))


#%%
# lage en lambda som multipliserer to tall

def multiply_def(x: int, y: int) -> int:
    return x * y


multiply_lambda = lambda x, y: x * y

# test
print(multiply_def(4, 5))
print(multiply_lambda(4, 5))

#%%
list_number: list[int] = [1, 3, 4, 5, 6, 7, 8, 9, 13, 44, 55, 66]

# bruke filter() lage en ny lyste med par-tall
even_numbers = list(filter(lambda x: x % 2 == 0, list_number))
print(even_numbers)

#%%
# map()
numbers = [1, 2, 3, 4]
# [1, 4, 9, 16]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#%%
# Sorting
# Tuple = ('Yngve', 1, 2, 4, 6)
# Index = (   0   , 1, 2, 3, 4 ) -> posisjon tuple[0] -> 'Yngve', tuple[3] -> 4

students = [('Yngve', 50), ('Ole', 34), ('Kari', 44)]
sorted_students = sorted(students, key=lambda tpl: tpl[0], reverse=True)
print(sorted_students)