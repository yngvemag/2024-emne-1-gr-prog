# lese inn et tall
# lese med input -> str -> skrive ut som tall

str_number = input("Skriv inn et tall: ")
try:
    nr = int(str_number)
    print(f"Du skrev inn tallet: {nr}")
except ValueError as valErr:
    print(f"Klarte ikke å tolke input som tall: {valErr}")
else:
    print("Avslutter skriptet! Alt gikk bra!")


try:
    with open('test.txt', 'r', encoding='utf8') as f:
        for line in f:
            print(line)
except FileNotFoundError as fnErr:
    print(fnErr)