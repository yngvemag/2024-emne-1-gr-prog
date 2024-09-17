# Definere 'add' funksjonen
def add(*args) -> int:
    # args = (2, 4, 6, 8, 9) -> tuple !!!
    print(f'*args = {args}, type(args) = {type(args)}')
    return sum(args)


# test:
print(f'sum= {add(2, 4, 6, 8, 9)}')
print(f'sum= {add(2, 4, 6, 8, 9, 18, 14, 37)}')


# *args

# **kwargs -> key word argumenter
def kwargs_demo(**kwargs):
    print(f'**kwargs = {kwargs}, type(kwargs) = {type(kwargs)}')
    # **kwargs = {'age': 50, 'name': 'Yngve'}, type(kwargs) = <class 'dict'>


# test: key-word=value, key-word=value
kwargs_demo(age=50, name='Yngve')
