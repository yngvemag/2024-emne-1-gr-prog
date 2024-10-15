import os

rm_name = 'copy_test.log'


# slette fil
# sjekke at filen finnes, sjekk at det er en fil (ikke directory)
if os.path.exists(rm_name) and os.path.isfile(rm_name):
    os.remove(rm_name)
    print(f"Slettet fil: {rm_name}")
else:
    print(f"Finner ikke filen ({rm_name}) du ønsker å slette")

