import os

# lage en ny mappe der vi står i filsystemet
ny_mappe = os.path.join(os.path.dirname(__file__), 'ny_mappe')
if not os.path.exists(ny_mappe):
    os.mkdir(ny_mappe)  # mk -> make directory
    print(f"laget ny mappe: {ny_mappe}")
else:
    print(f"Kan ikke lage mappen '{ny_mappe}', den finnes fra før.")