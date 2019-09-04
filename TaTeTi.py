tablero={'1':"X",'2':"X",'3':"O"
        ,'4':"O",'5':"X",'6':"O"
        ,'7':"X",'8':"O",'9':"X"}
def mostrarTablero(tablero):
    for i in range (1,len(tablero)+1):
        print(tablero[str(i)], end="-")
        if (i%3==0):
            print("")

def iniciarlizarTablero():
    return {'1':" ",'2':" ",'3':" "
        ,'4':" ",'5':" ",'6':" "
        ,'7':" ",'8':" ",'9':" "}

def isTableroCompleto(tablero):
    for i in range(1, len(tablero) + 1):
        if (tablero[str(i)]==" "):
            return False
    return True


mostrarTablero(tablero)
tablero=iniciarlizarTablero()




