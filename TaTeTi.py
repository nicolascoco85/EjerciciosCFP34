tablero={'1':"X",'2':"X",'3':"O"
        ,'4':"O",'5':"X",'6':"O"
        ,'7':"X",'8':"O",'9':"X"}
def mostrarTablero(tablero):
    for i in range (1,len(tablero)+1):
        print(tablero[str(i)], end="-")
        if (i%3==0):
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


#mostrarTablero(tablero)
tablero=iniciarlizarTablero()
mostrarTablero(tablero)
opcion=input("Ingrese el Numero donde quiere poner la X")[0]
i=0
while (hayGanador(tablero)!=True and i<len(tablero)):
    if (i%2==0):
        while(tablero[str(opcion)]=="X" or tablero[str(opcion)]=="O" ):
            opcion=input("Ingrese el Numero donde quiere poner la X")[0]
        tablero[str(opcion)]="X"
    else:
        while (tablero[str(opcion)]=="X" or tablero[str(opcion)]=="O" ):
            opcion = input("Ingrese el Numero donde quiere poner la O")[0]
        tablero[str(opcion)] = "O"
    i=i+1
    mostrarTablero(tablero)

mostrarGanador(i)




