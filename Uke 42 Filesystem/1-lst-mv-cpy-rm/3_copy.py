import os
import shutil

org_name = 'test.log'

# kopierer filer
cpy_name = f'copy_{org_name}'

# sjekk at filen finnes, sjekke at det er en fil, sjekke at copy name ikke finnes
if os.path.exists(org_name) and os.path.isfile(org_name) and not os.path.exists(cpy_name):
    shutil.copy(org_name, cpy_name)
    print(f"Kopierte: {org_name} -> {cpy_name}")
else:
    print(f"Klarte ikke å kopiere filen {org_name}")