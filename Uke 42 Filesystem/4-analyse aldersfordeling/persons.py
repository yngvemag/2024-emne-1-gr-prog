import os
import sys

# Lage en funksjon som returnerer en liste med personer
# [
#   ('Ole', 'Johansen', 44, 'Mann'),
#   ('Marte', 'Knutsen', 29, 'Kvinne'),
#   ()
# ]
def read_persons(filename: str, has_header: bool = True) -> list[tuple[str, str, int, str]] | None:
    # sjekk om filen finnes !!
    if not os.path.exists(filename):
        print(f"Finner ikke filen '{filename}'")
        return

    # vi leser inn data fra fil
    person_list: list[tuple[str, str, int, str]] = []
    with open(filename, 'r', encoding='utf-8') as fread:
        for idx, line in enumerate(fread):

            # Hopper over første linje hvis filen har en header
            if idx == 0 and has_header:
                continue

            # line = 'Ole,Johansen,44,Mann\n' -> \n = betyr "new line"
            # line = "Ole,Johansen,44,Mann" split-> ['Ole', 'Johansen', '44', 'Mann']
            person_arr = line.rstrip('\n').split(',')

            # 1. Validering, sjekke at vi har 4 felter
            if not len(person_arr) == 4:
                print(f'Feil format på filen: linenr: {idx} -> {line}')
                continue

            # pakker ut array i variabler
            # first_name, last_name, age, gender =  ['Ole', 'Johansen', '44', 'Mann']
            first_name, last_name, age, gender = person_arr

            # 2. Validering, sjekker om vi har data i alle felt
            if not all([first_name, last_name, age, gender]):
                print(f'Feil i data, mangler data i felt(er): linjenr: {idx} -> {line}')
                continue

            # 3. Validering, sjekker at age er en int (heltall)
            if not age.isdigit():
                print(f'Feil i data, age er ikke et tall: linjenr: {idx} -> {line}')
                continue

            # 4. Validering, sjekker at kjønn er 'kvinne' eller 'mann'
            if not gender.lower() in ['kvinne', 'mann']:
                print(f'Feil i data, stemmer ikke med forventet data i fil: linjenr: {idx} -> {line}')
                continue

            try:
            # Nå har vi gyldig data på denne linjen
                person_list.append((first_name, last_name, int(age), gender))
            except ValueError as valErr:
                print(valErr)
                continue

    return person_list

def sum_age_by_gender(person_list: list[tuple[str, str, int, str]], gender: str) -> int:
    tot_age = 0

    # vi lager en løkke som går gjennom alle personer
    # person = ('Ole', 'Johansen', 44, 'Mann')
    for p in person_list:
        fname, lname, age, g = p

        # sjekker om kjønn stemmer med argument gitt i funksjonen
        if g.lower() == gender.lower():
            tot_age += age

    return tot_age

def get_gender_count(person_list: list[tuple[str, str, int, str]], gender: str) -> int:
    count = 0
    for p in person_list:
        fname, lname, age, g = p
        if g.lower() == gender.lower():
            count += 1

    return count


if __name__ == '__main__':
    # leser personer fra filen 'persons.csv'
    # liste med personer (tuples)
    persons:list[tuple[str,str,int,str]] = read_persons('persons.csv')

    # ('Ole', 'Johansen', 44, 'Mann')
    # [0, 1, 2, 3]
    # 1. Beregn den totale alderen for alle menn i datasettet
    print(f'Den totale alderen for alle menn i datasettet er: {sum_age_by_gender(persons ,'mann')}')

    # alterativt bruke list comprehension
    # p[2] -> age, p[3] -> gender
    tot_age_men = sum([p[2] for p in persons if p[3].lower() == 'mann'])
    print(f'Den totale alderen for alle menn i datasettet er: {tot_age_men}')

    # 2. Beregn den totale alderen for alle kvinner i datasettet
    print(f'Den totale alderen for alle kvinner i datasettet er: {sum_age_by_gender(persons, 'kvinne')}')

    # 3. Hvor mange menn er det i datasettet?
    print(f'Antall menn i datasettet er: {get_gender_count(persons, 'mann')}')

    # 4. Hvor mange kvinner er det i datasettet?
    print(f'Antall kvinner i datasettet er: {get_gender_count(persons, 'kvinne')}')

    # print ut listen med personer
    for person in persons:
        print(person)


