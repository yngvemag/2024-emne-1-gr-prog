# Problemløsing
# 1. Forstå problemet
# 2. Lag en plan
# 3. utfør planen
# 4. test om planen fungerer

# 2. Lag en plan
# - Lage 3 spørsmål med alternative svar
# - print spørsmål og alternative svar
# - Les inn svar fra spiller (input)
# - sjekk om svaret er riktig og gi tilbakemelding til spiller (riktig/galt)
# - hvis riktig må vi øke spiller poeng !!

# 3. Gjennomføring !
# starter med å lage en score-variabel
antall_riktige_svar: int = 0

# spørsmål 1
print("Spørsmål 1: Hva er datatypen til verdien 10? (1,2 eller 3)")
print("1. int")
print("2. str")
print("3. bool")

# svar1_nr: int = int(input("Svar (skriv inn nummeret): "))
svar1: str = input("Svar (skriv inn nummeret): ")

# ønsker svaret som nummert -> casting til integer
# svar1_nr = int(svar1)

# sjekk om svaret er riktig og gi tilbakemelding
# øke antall poeng hvis svar er riktig
if svar1 == '1':
    print(f"Riktig: {svar1} er riktig svar!")
    # øke verdien til variabel 'antall_riktige_svar' med 1
    # antall_riktige_svar = antall_riktige_svar + 1
    antall_riktige_svar += 1
else:
    print(f"Feil: {svar1} er feil svar!")

# Gi beskjed til spiller om antall poeng
print(f"Du har nå {antall_riktige_svar}/3 poeng!")

# spørsmål 2:
print("Spørsmål 2: Hva er datatypen til 'Python'? (1,2 eller 3)")
print("1. int")
print("2. str")
print("3. float")

svar2: str = input("Svar (skriv inn nummeret): ")
# sjekk om svaret er riktig og gi tilbakemelding
# øke antall poeng hvis svar er riktig
if svar2 == '2':
    print(f"Riktig: {svar2} er riktig svar!")
    antall_riktige_svar += 1
else:
    print(f"Feil: {svar2} er feil svar!")

# Gi beskjed til spiller om antall poeng
print(f"Du har nå {antall_riktige_svar}/3 poeng!")

# Spørsmål 3
print("Spørsmål 3: Hva er datatypen til 4.12? (1,2 eller 3)")
print("1. int")
print("2. str")
print("3. float")

svar3: str = input("Svar (skriv inn nummeret): ")
# sjekk om svaret er riktig og gi tilbakemelding
# øke antall poeng hvis svar er riktig
if svar3 == '3':
    print(f"Riktig: {svar3} er riktig svar!")
    antall_riktige_svar += 1
else:
    print(f"Feil: {svar3} er feil svar!")

# Gi beskjed til spiller om antall poeng
print(f"Du klarte {antall_riktige_svar}/3 poeng!")
