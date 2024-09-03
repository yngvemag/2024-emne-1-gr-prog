#%%
# print alle tallene fra 1-10 med en while løkke
i: int = 1
while True:
    print(f'{i}', end=' ')

    # hvordan stopper vi løkken på 10!!
    if i >= 10:
        # stoppe løkken/avslutte løkken
        break  # avslutter løkken vi er i !!

    # sikrer 'step' i løkken
    i += 1

#%%
# print alle tallene fra 1-10 med en while-løkke unntatt tallet 6
i: int = 1
while True:
    if i == 6:
        i += 1 # VIKITG å oppdatere teller i løkken !!
        continue  # Vi hopper over resten av løkken og starter ny runde!

    print(f'{i}', end=' ')

    # VIKTIG: Må ha exit mulighet - stoppe evig løkke !! BREAK!!
    if i >= 10:
        break

    # STEP (unngå evig løkke med å øke med 1)
    i += 1
