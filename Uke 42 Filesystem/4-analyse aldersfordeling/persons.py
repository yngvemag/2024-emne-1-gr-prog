import os

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


if __name__ == '__main__':
    pass


