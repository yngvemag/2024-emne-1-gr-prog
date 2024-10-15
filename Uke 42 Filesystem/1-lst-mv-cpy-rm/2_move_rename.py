import os

org_name = 'test.txt'
new_name = 'test.log'

# sjekker at dette faktisk er en fil
# sjekker at filen finnes
# sjekker at nytt navn ikke finnes
if os.path.exists(org_name) and os.path.isfile(org_name) and not os.path.exists(new_name):
    os.rename(org_name, new_name)
    print(f'Laget nytt navn på file: {org_name} -> {new_name}')
else:
    print(f'kan ikke bytte navn på {org_name}')

