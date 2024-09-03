# import statement
# Instruksjon som brukes for å inkludere en modul (kode) eller pakke (kode)
# i ditt nåværende program

#%%
# Importere en hel modul og deretter aksessere funksjone ved å bruke modulene
# https://docs.python.org/3/library/math.html
import math

# kvadratrot, eks på tallet 5
print(math.sqrt(5))

# 6! = 1*2*3*4*5*6 (factorial)
print(f'1 * 2 * 3 * 4 * 5 * 6 = {math.factorial(6)}')

#%%
# Importere spesifikke funksjoner eller objekter fra en modul
from math import sqrt, factorial

print(sqrt(5))

#%%
# Gi modulen et alias
import math as m

# 5 opphøyd i andre -> 5**2
print(m.pow(5,2))

#%%
# importere alle funksjoner og objekter fra en modul
from math import *

print(sqrt(5))
