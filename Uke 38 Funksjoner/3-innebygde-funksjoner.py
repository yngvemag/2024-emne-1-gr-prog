# max(), min(), sum(), len()

#%%
# zip()
# Kombinerer flere iterables (som lister eller tuples) til en
# iterator med tupler der hver tuple inneholder elementer fra hver
# iterable på samme indeks
animals: list[str] = ['dog', 'cat', 'horse']
animal_names: list[str] = ['Diaz', 'Pusur', 'Silver']

animal_with_names = list(zip(animals, animal_names))
print(animal_with_names)
# [
#   ('dog','Diaz'),
#   ('cat', 'Pusur'),
#   ('horse', 'Silver')
#  ]

# test: Vi lager en for-løkke som itererer gjennom alle elementene
for animal, animal_name in animal_with_names:
    print(f'Dyr: {animal} - {animal_name}')

#%%
# reversed()
my_tuple = ('dog', 'cat', 'horse')
my_reversed_tuple = reversed(my_tuple)

print(*my_tuple)
print(*my_reversed_tuple)

# print reversed
print(my_reversed_tuple[::-1])

#%%
# sorted / sortering
names: list[str] = ['Diaz', 'Pusur', 'Silver', 'Anne', 'Ba']

# sorterer alfabetis
sorted_names: list[str] = sorted(names)  # return ny liste !!
print(sorted_names)
print(names)

# mulig å sortere på den orginale listen ved å bruke innebygd 'sort'
names.sort()
print(names)

names_sorted_length = sorted(names, key=len, reverse=True)
print(names_sorted_length)

#%%
# filter
my_list = [1, 2, 3, 'dog', 'cat', 'horse', 6, 7, 8, 9]


# vi ønsker nå å bare se på tallene og overse alt annet !!
# vi må lage en funksjon som sjekker om parameter er en 'int' !!
# Plan:
#   1. Name: 'is_digit'
#   2. parameter: 1 parameter -> type: any
#   3. return : True hvis det er et tall (int), False for alt annet !!
def is_digit(var: any) -> bool:
    if isinstance(var, int):
        return True
    return False


# filtrer bort tekst
res = filter(is_digit, my_list)
print(*res)

#%%
# map()

from math import sqrt

# 2 * 2 -> 2^2
my_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# Vi må lage en funksjon som utfører exponent x^2 (square)
# Plan
#   1. Navn: 'square_number'
#   2. Parameter: vi må ha et tall, type -> int, float
#   3. Return: param * param, input**2
def square_number(number: int | float) -> int | float:
    return number ** 2  # number * number


result = map(square_number, my_numbers)
result_root = map(sqrt, my_numbers)

print(*result)
print([round(x, 2) for x in result_root])

x = 2.546347437437
print(round(x, 4))