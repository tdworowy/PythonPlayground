def f(ham:str,eggs:str = 'eggs') -> str:
    pass

print(f.__annotations__)
f(1,2) # annotations is just information