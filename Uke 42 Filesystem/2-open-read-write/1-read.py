import os
import sys

# vs-code
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# 'r' : Åpne filen for lesing (standard). Hvis filen ikke finnes, vil det oppstå en feil.
# 'w' : Åpne filen for skriving. Hvis filen eksisterer, overskrives den. Hvis den ikke eksisterer, lages en ny fil.
# 'a' : Åpne filen for å legge til innhold. Hvis filen ikke eksisterer, lages en ny fil.
# 'x' : Åpne filen eksklusivt for opprettelse. Hvis filen eksisterer, vil det oppstå en feil.
# 'b' : Åpne filen i binær modus (kan kombineres med andre moduser, som 'rb' eller 'wb').
# 't' : Åpne filen i tekstmodus (standard og kan kombineres med andre moduser, som 'rt' eller 'wt').
# '+' : Åpne filen for oppdatering (lesing og skriving).

FILENAME = 'persons.csv'

# Hvis filen ikke finnes så avslutter vi scriptet!
if not os.path.exists(FILENAME) and not os.path.isfile(FILENAME):
    print(f'Finner ikke filen {FILENAME} - Avslutter')
    sys.exit()

with open(FILENAME, 'r', encoding='utf-8') as fread:
    for line in fread:
        line = line.strip('\n')

        # lager liste av linjen som er komma separert (csv)
        person: list = line.split(',')
        print(person)


