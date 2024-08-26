#%%
my_input = input('venter på input fra tastatur: ')

print(f'Input fra tastatur: {my_input}')

#%%
# Oppgave
# 1. Les inn to tall og legge disse i variabler
# 2. Skriv ut summen av disse tallene ved å legge sammen variabler med +

a = input("Tall a: ") # 5
b = input("Tall b: ") # 6

# Casting -> Vi prøver å omforme tekst til et tall som vi kan regne med !
tall_a = int(a)
tall_b = int(b)

print(f'Summen er {tall_a + tall_b}')

