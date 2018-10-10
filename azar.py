import random

def dame_un_dado():
    return random.randrange(1,7)

def dame_tirada():
    tirada = []
    for dado in range (1,6):
        tirada.append(dame_un_dado())
    return tirada


tirada=dame_tirada()
print(tirada)