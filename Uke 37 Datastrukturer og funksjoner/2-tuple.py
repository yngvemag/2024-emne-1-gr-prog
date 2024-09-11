#%%
my_tuple: tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#%%
# index og slicing
#(1, 2, 3, 4, 5)
#(0, 1, 2, 3, 4) Index!
element = my_tuple[2]
print(element)

sub_tuple: tuple = my_tuple[1:4] # slicing (start, stop)
print(sub_tuple)
#%%
print(len(my_tuple))
#%%
# slå sammen tuples !! Her får vi ny tuple
new_tuple = my_tuple + (6, 7)
print(new_tuple)
#%%
print(sum(my_tuple))

#%%
# Unpacking
person = ('Yngve','Magnussen', 51)

# vi pakker ut tuple i variabler - her må det være like mange
# variabler som elementer i tuple !!
first_name, last_name, age = person
print(first_name, last_name, age)

