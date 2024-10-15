import os

ny_mappe = os.path.join(os.path.dirname(__file__), 'ny_mappe')

# slette en mappe
if os.path.exists(ny_mappe):
    os.rmdir(ny_mappe) # rm -> remove directory
    print(f"Slettet mappen {ny_mappe}")
else:
    print(f"Kan ikke slette mappen {ny_mappe}, finnes ikke")