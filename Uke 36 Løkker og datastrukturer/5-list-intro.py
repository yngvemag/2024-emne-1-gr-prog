#%%
names_group_one: list[str] = ['Yngve', 'Ola', 'Kari']
age_group_one: list[int] = [51, 40, 20]
list_mixed: list = [1, 2, "Yngve", True, 4.67]

# skrive ut hvert element i listen
for name in names_group_one:
    print(name)

# skrive ut hvert tall i listen age_group_one
for age in age_group_one:
    print(age)

#%%
# legge til nye elementer i en liste !!
my_list: list = []
print(my_list)

my_list.append("Yngve")
print(my_list)

my_list.append(73)
print(my_list)

#%%
# Indexing !! Hvert element i listen har en posisjon og starter på posisjon 0.
my_list_numbers: list[int] = list(range(20, 30))
print(my_list_numbers)

# indexing -> printe ut index=3, index=4
# List  = [20, 21, 22, 23,24, 25, 26, 27, 28,29] ?
# index = [0 , 1 , 2 , 3 , 4, 5 , 6 , 7 , 8 , 9] ?
print(my_list_numbers[0])
print(my_list_numbers[3])
print(my_list_numbers[4])
print(my_list_numbers[10])  # IndexError: list index out of range

#%%
# Legge til i listen på en gitt posisjon
names: list[str] = ['Magnussen']
print(names)

# legger til 'Yngve' først i listen
names.insert(0, 'Yngve')
print(names)

# legger til 'Et eller annet' først i listen
names.insert(1, 'Et eller annet')
print(names)

# print ut alle elementer som tekst string
print(str.join(', ', names))

#%%
# Fjerne elementer
list_numbers: list[int] = list(range(10, 20))
print(list_numbers)

# ønsker å fjerne tallet 16 fra listen
list_numbers.remove(16)
print(list_numbers)

# fjerner på index
list_numbers.pop(0)
print(list_numbers)

# slette hele listen (del list_number)
del list_numbers[5]
print(list_numbers)
del list_numbers

#%%
# Sortering av liste
list_animals: list[str] = ['Dog', 'Cat', 'Mouse']
print(list_animals)

list_animals.sort()
print(list_animals)

list_animals.sort(reverse=True)
print(list_animals)

#%%
# innebygde funksjoner
list_number: list[int] = list(range(10, 20))
print(list_number)
length: int = len(list_number)  # finner lengden på listen
maximum: int = max(list_number)
minimum: int = min(list_number)
total: int = sum(list_number)

print(f'Length={length}, Minimum={minimum}, Maximum={maximum}, total={total}')
