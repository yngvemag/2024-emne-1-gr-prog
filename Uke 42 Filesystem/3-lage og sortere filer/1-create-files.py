import os
import random as rnd
import time

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# 1. Lage subfolder 'files'
sub_folder = os.path.join(os.getcwd(), 'files')
if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
    print(f"Laget sub-folder '{sub_folder}'")
else:
    print(f"folder '{sub_folder}' finnes")

# 2. lage 100 tilfeldige filer med følgende struktur i subfolder 'files'
# YYYY-MM.txt -> eks 2015-02.txt
files_created_count = 0
while files_created_count < 100:
    year = rnd.randint(2013, 2024)
    mnd = rnd.randint(1, 12)
    filename = f'{year}-{mnd:0>2}.txt'

    if os.path.exists(os.path.join(sub_folder, filename)):
        continue

    with open(os.path.join(sub_folder, filename), 'w') as f:
        print(f'laget fil: {filename}', files_created_count)
        files_created_count += 1




