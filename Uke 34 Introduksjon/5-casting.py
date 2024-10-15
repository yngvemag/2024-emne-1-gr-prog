# ================================================
# Casting:
# Vi kan endre datatypen på variabler/data
# ================================================

nr: int = 34
nr_str: str = str(nr)

print(f"'nr' er av typen {type(nr)}, 'nr_str' er av typen {type(nr_str)}")

# casting: STR -> INT
nr_str: str = '33'
nr: int = int(nr_str)
print(nr * 100)