# ==================================================================
# Variabler:
# - Et sted hvor vi kan lagre informasjon
# - variabel-navn: Vi kan bruke lagret data via dette navnet
#
# variabel_navn = variabel_verdi
# variabel type blir satt automatisk av python når verdien settes.
# ==================================================================

my_name = "Yngve"
age = 51

print(my_name)

# Kan dere lage følgene print: "Jeg heter Yngve og er 51 år"
# version 1
print("Jeg heter", my_name, "og er", age, "år")

# version 2
print(f"Jeg heter {my_name} og er {age} år")