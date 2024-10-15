import os

# vs-code
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# lage en fil 'numbers.txt'
# skrive 100 tall (1-100) til filen

FILENAME_WRITE = 'numbers.txt'

with open(FILENAME_WRITE, 'a', encoding='utf-8') as f:
    for i in range(10, 20):
        f.write(f'{str(i)}\n' )