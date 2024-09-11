# En dictionary i Python er en datastruktur som lagrer verdier i nøkkel-verdi-par.
# Det betyr at hver verdi (value) i en dictionary er assosiert med en unik nøkkel (key).
# Du kan bruke nøkkelen til å hente eller endre verdien i dictionaryen.

#%%
# En dictionary er omsluttet av {}  ({} 'set' har også denne)
my_dict = {
    # key: value
    "name": "Yngve Magnussen",
    "age": 25,
    "city": "Horten"
}
print(my_dict)

#%%
# Hente ut verdier fra en dictionary
name = my_dict["name"]
print(name)

# hente ut ved hjelp av .get("")
age = my_dict.get("age", 50)
print(age)

#%%
# Oppdatere verdier i dictionary
my_dict["age"] = 44
my_dict.update({"name": "Yngve"})
print(my_dict)

#%%
# Slette elementer fra en dictionary
del my_dict["age"]
print(my_dict)

name = my_dict.pop("name")
print(name)
print(my_dict)

#%%
# vi kan sjekke om noe finnes i dictionary
has_name = "name" in my_dict
print(has_name)

#%%
# Liste av 'keys' og 'values'
keys = my_dict.keys()
for key in keys:
    print(key)

values = my_dict.values()
for value in values:
    print(value)

items = my_dict.items()
for key, value in items:
    print(key, value)

#%%
# kopiere en dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)

#%%
# legge til nye elementer til dictionary
my_dict["height"] = 180
print(my_dict)
