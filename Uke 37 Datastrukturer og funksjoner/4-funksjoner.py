# Hva er en funksjon
# En funksjon i Python er en gjenbrukbar blokk med kode som
# utfører en spesifikk oppgave.
# Funksjoner hjelper med å gjøre koden mer organisert,
# modulær og lett å vedlikeholde.
# Du kan bruke en funksjon flere ganger uten å
# skrive samme kode om igjen.

# Hvordan lager vi en funksjon
# For å definere en funksjon i Python bruker man nøkkelordet 'def',
# etterfulgt av funksjonsnavnet, parenteser og et kolon.
# # Kodeblokken inne i funksjonen må være innrykket.
# Her er et enkelt eksempel:

#%%
def say_hello() -> None:
    print("Hello")


say_hello()


#%%
# Hva er parametere og argumenter?
# * Parametere er variabler som funksjonen
#   forventer når den blir definert.
# * Argumenter er de faktiske verdiene som blir gitt til
#   funksjonen når den blir kalt.

# 'name' -> er nå parameter for funksjonen
def greet(name: str) -> None:  # skal ha string inn, ingenting ut!
    print(f'Hello, {name}')


# bruker funksjonen med ulike argumenter.
greet('Anna')
greet('Bob')


#%%
# Hva er returverdi
# En returverdi er verdien som en funksjon sender tilbake til der den ble kalt.
# Da må vi bruke 'return' statement

def add(a: int, b: int) -> int:
    return a + b


x: int = add(1, 2)
y: int = add(14, 67)
print(x, y)
