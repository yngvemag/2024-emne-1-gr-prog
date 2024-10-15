import os
import sys


os.chdir(os.path.dirname(os.path.realpath(__file__)))

# vi skal sortere filene i denne folderen
sub_folder = os.path.join(os.getcwd(), 'files')

# sjekk om folder finnes
if not os.path.exists(sub_folder):
    sys.exit(f"Folder {sub_folder} finnes ikke!")

# Vi navigerer oss inn i 'sub_folder'
os.chdir(sub_folder)

# lister ut alle filene i folder
files = os.listdir('.')

# Eksempel fil: 2013-02.txt
for file in files:
    year = file[0:4]  # 2013
    month = file[5:7] # 02

    if not year.isdigit() or not month.isdigit():
        print(f"Noe er galt i fil-navnet: {file}")
        continue

    # lager sub foldere for filen
    sub_directories = os.path.join(sub_folder, year, month)
    if not os.path.exists(sub_directories):
        os.makedirs(sub_directories)

    # Flytter filen -> rename filen inn i subfolder
    if not os.path.exists(os.path.join(sub_directories, file)):
        os.rename(file, os.path.join(sub_directories, file))