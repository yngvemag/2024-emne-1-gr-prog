#%%
import random as rnd

# Plan
# 1. Vi må bestemme et tall som pc-gjetter.
my_number: int = 73

# 2. Vi må la pc-gjette på tallet vårt helt til den får riktig
#   - Det innebærer en løkke (while-løkke)
#   - pc gjetter ved help av random funksjonen.
number_of_tries: int = 1
while True:
    pc_guess_number: int = rnd.randint(1, 100)

    # 3. Så må vi sjekke om pc har gjettet riktig. (if -statement)
    # 4. Hvis pc har riktig -> avslutt
    if pc_guess_number == my_number:
        break
    ...
    # 5. Hvis pc har feil -> øk antall forsøk og gjett igjen!
    number_of_tries += 1

# 6. Avslutt med å printe ut resultat.
print(f'Riktig tall gjettet. Pc brukte {number_of_tries} forsøk!')

#%%
import random as rnd

# Plan
# 1. Vi må bestemme et tall som pc-gjetter.
min_nr: int = 1
max_nr: int = 100
my_number: int = int(input("Hvilke tall skal pc gjette: "))

# while True:
    # safe_str_nr = input("Skal pc gjette: ")
    # safe_str_nr.isdigit() -> True/False
    # hvis det bare er tall -> Trykt å caste til int -> avslutt
    # hvis ikke prøv igjen !!!

# 2. Vi må la pc-gjette på tallet vårt helt til den får riktig
#   - Det innebærer en løkke (while-løkke)
#   - pc gjetter ved help av random funksjonen.
number_of_tries: int = 1
while True:
    pc_guess_number: int = rnd.randint(min_nr, max_nr)

    # 3. Så må vi sjekke om pc har gjettet riktig. (if -statement)
    # 4. Hvis pc har riktig -> avslutt
    if pc_guess_number == my_number:
        break

    # 5. Hvis pc har feil -> øk antall forsøk og gjett igjen!
    number_of_tries += 1

# 6. Avslutt med å printe ut resultat.
print(f'Riktig tall gjettet. Pc brukte {number_of_tries} forsøk!')
