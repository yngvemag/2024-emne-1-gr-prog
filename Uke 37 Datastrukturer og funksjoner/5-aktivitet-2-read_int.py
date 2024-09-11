# Denne er utrygg da det smeller om de skriver 'ajl3'
# my_number: int = int(input("Hvilke tall skal pc gjette: "))


def read_int(promt: str, min_number: int, max_number: int) -> int:
    # innlesing av tall !!
    while True:
        safe_str_nr = input(f"{promt}")
        if not safe_str_nr.isdigit():
            print("Du må taste inn et gyldig tall!")
            continue

        # det er trykt å gjøre om string til int !!
        my_number = int(safe_str_nr)

        # må vi sjekk max_nr og min_nr !!! Sikre at input er innefor max/min range
        if min_number <= my_number <= max_number:
            return my_number

        print(f"Du må taste inn et tall innenfor gitt område {min_number}-{max_number}")


# utenfor funksjonen
my_int = read_int("Skriv inn et tall", 50, 100)
print(f'my int is: {my_int}')
