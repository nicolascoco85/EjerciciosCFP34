def mostrarTablero(tablero):
    for i in range (1,len(tablero)+1):
        separador=" "

        if (i % 3 != 0):
            separador ="-"

        print(tablero[str(i)], end=separador)

        if (i%3==0):#Permite el interlineado
            print("")

def iniciarlizarTablero():
    return {'1':"1",'2':"2",'3':"3"
        ,'4':"4",'5':"5",'6':"6"
        ,'7':"7",'8':"8",'9':"9"}

def isTableroCompleto(tablero):
    for i in range(1, len(tablero) + 1):
        if (tablero[str(i)]==" "):
            return False
    return True

def hayGanador(tablero):
    return ((tablero["1"]==tablero["2"]) and (tablero["2"]==tablero["3"])) \
           or ((tablero["4"]==tablero["5"]) and (tablero["5"]==tablero["6"]))\
           or ((tablero["7"]==tablero["8"]) and (tablero["8"]==tablero["9"]))\
            or ((tablero["1"]==tablero["5"]) and (tablero["5"]==tablero["9"]))\
            or ((tablero["3"]==tablero["5"]) and (tablero["5"]==tablero["7"])) \
           or ((tablero["1"] == tablero["4"]) and (tablero["4"] == tablero["7"]))\
           or ((tablero["2"] == tablero["5"]) and (tablero["5"] == tablero["8"]))\
            or ((tablero["3"]==tablero["6"]) and (tablero["6"]==tablero["9"]))

def mostrarGanador(i):
    if (i % 2 != 0):
        print("gano la X")
    else:
        print("gano la O")
    input()

def estaOcupado(tablero,opcion):
    return tablero[str(opcion)]=="X" or tablero[str(opcion)]=="O"


def pedirOpcion(jugador):
    return input("Ingrese el Numero donde quiere poner la "+jugador)[0]

def determinarJugador(i):
    if (i%2==0):
        return "X"
    else:
        return "O"

#mostrarTablero(tablero)
tablero=iniciarlizarTablero()
mostrarTablero(tablero)
opcion=input("Ingrese el Numero donde quiere poner la X")[0]
i=0

while (hayGanador(tablero)!=True and i<len(tablero)):
    while estaOcupado(tablero,opcion):
        opcion= pedirOpcion(determinarJugador(i))
    tablero[str(opcion)]=determinarJugador(i)
    i=i+1#Paso de turno
    mostrarTablero(tablero)

mostrarGanador(i)




