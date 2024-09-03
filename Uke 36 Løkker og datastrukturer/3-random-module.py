import random as rnd

# tilfeldig tall mellom 1-100
tilfeldig_tall: int = rnd.randint(1, 100)
print(tilfeldig_tall)

# tilfeldig partall/oddetall mellom 0-100
partall: int = rnd.randrange(0, 101, 2)
oddetall: int = rnd.randrange(1, 100, 2)

print(f'random partall: {partall}, random oddetall: {oddetall}')

# tilfeldig desimal tall 1-10
number_a: float = rnd.uniform(1, 10)
number_b: float = rnd.random() * 10 # 0 - 1 (3.5, 4.4 osv)

print(f'random number a: {number_a:.2f}, random number b: {number_b:.3f}')
