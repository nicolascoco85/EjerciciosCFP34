import random
cantidad_limite_jugadores=21
cantidad_jugadores=int(input('Ingrese el numero de jugadores: '))
adivinar_numero= random.randrange(0,cantidad_limite_jugadores)
nombre= input('ingrese el nombre de jugador: ')
numero_elegido= int(input('Ingrese un numero: '))
lista=[]
turnos_jugados=1
while (numero_elegido!=adivinar_numero)and (cantidad_jugadores!=turnos_jugados):
    lista.append((nombre,abs(adivinar_numero-numero_elegido)))
    nombre = input('ingrese el nombre de jugador: ')
    numero_elegido = int(input('Ingrese un numero: '))
    turnos_jugados+=1
print('El numero misterioso es: ',adivinar_numero)
for jugador in lista:
    print(jugador)