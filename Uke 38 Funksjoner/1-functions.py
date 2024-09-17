# Skriv en funksjon som tar tre tall som parametere og returnerer det største tallet.
# Plan
# - navn: get_biggest_number()
# - 3 parametere: a, b og c av type 'int'
# - skal finne den største og returnere denne -> return statement
# - hint: bruke max() funksjonen som er innebygd i python
def get_biggest_number(a: int, b: int, c: int) -> int:
    return max(a, b, c)


# test.
biggest_number = get_biggest_number(10, 20, 30)
print(biggest_number)


# Skriv en funksjon som tar inn et tall og returnerer
# 'True' hvis det er et parttall, og 'False' ellers.
# Plan:
# 1. Navn: 'is_even()'
# 2. Parameter: 1 parameter av typen 'int'
# 3. Return 'True' hvis det f.eks er 2, 4, 6, 8 ...Ellers return 'False'
def is_even(n: int) -> bool:
    return n % 2 == 0
    #if n % 2 == 0:
    #    return True
    #return False


# test:
print(f'Er tallet 5 et partall? {is_even(5)}')
print(f'Er tallet 10 et partall? {is_even(10)}')


# Lag en funksjon som tar inn en liste med tall og returnerer
# summen av alle tallene i listen.
# Plan:
#   1. Navn: 'sum_numbers'
#   2. Parameter: liste med tall av typen 'int' eller 'float'
#   3. Returnerer: summen av tallene i listen av typen 'int' eller 'float'
#   4. Hint: bruk sum() funksjonen i python
def sum_numbers(numberlist: list[int | float]) -> int | float:
    return sum(numberlist)


# test:
numbers = [1, 2, 3, 4, 5, 6.35, 7.65, 8.8, 9]
print(sum_numbers(numbers))


# Skriv en funksjon som tar to strenger som parametere og returnerer True hvis de er like, og
# False hvis de er forskjellige.
# Plan:
#   1. Navn: 'str_compare'
#   2. Parametere: 2 tekst strenger (type 'str')
#   3. Return: hvis de er like return 'True' else 'False'
def str_compare(str1: str, str2: str) -> bool:
    return str1 == str2
    #if str1 == str2:
    #    return True
    #return False
