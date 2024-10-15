import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("../../Uke 35 Betingelser, Løkker")

# Lister ut alle filer på nåværende path
dir_content = os.listdir()
for content in dir_content:
    print(f'{content} Er en mappe: {os.path.isdir(content)}, '
          f'Er en fil: {os.path.isfile(content)}')