# range(stop)
# range(start, stop)
# range(start, stop, step )

# Skriv ut tallene 0-9
# vi skal gjenta print funksjonen 10 ganger!! samtidig endre vår variabel
#print(0)
#print(1)
#print(2)

# [0 1 2 3 4 5 6 7 8 9] = range(10)
for my_number in range(10):  # start=0, stop=10 (ikke med), step=1
    print(my_number, end=' ')
print('')

# Kan dere skrive tallene 2 til og med 8 ved bruk av for-løkke.
for my_number in range(2, 9):
    print(my_number, end=' ')
print("")

# Kan dere skrive ut tallene 2,4,6,8,10 ved bruk av for-løkke
for i in range(2, 11, 2):
    print(i, end=' ')
print("")

# Kan dere skrive ut tallene 15, 11, 7, 3
for i in range(15, 2, -4):
    print(i, end=' ')
print('')

# Slicing
my_name = 'Yngve Magnussen'
print(my_name[2]) # stop
print(my_name[2:5]) # start, stop
print(my_name[2:10:2]) # start, stop, step !!




