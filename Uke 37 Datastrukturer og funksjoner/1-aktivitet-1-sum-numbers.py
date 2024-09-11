# Plan
# 1. Lag en variabel av typen 'list'
my_numbers: list[int] = []

# 2. Vi må ha en while-løkke og lese inn tall som vi
#    kan legge i listen. Avslutter løkken med å ikke
#    skrive inn noe.
while True:
    input_text: str = input('Skriv inn et tall: (avslutt med "")')

    # kan være tall, tekst eller ingenting
    if input_text == '':
        print("Avslutter innlesing av tall")
        break

    # Må vi gjøre om tekst til tall før vi legger i listen
    if not input_text.isdigit():
        print("Du må skrive inn tall!")
        continue

    # Nå kan vi legge i tall i listen
    my_nr: int = int(input_text)
    my_numbers.append(my_nr)


# 3. Lag en for-løkke som går gjennom alle tallene i
#    listen og summerer de sammen.
sum_numbers_1: int = sum(my_numbers)
sum_numbers: int = 0
for nr in my_numbers:
    # legge 'nr' sammen med sum_numbers
    sum_numbers += nr

# 4. Print ut denne summen.
print(f'Summen av tallene i listen er: {sum_numbers}')