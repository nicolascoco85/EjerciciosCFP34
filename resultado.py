import azar as simulacro
def iniciar_tabla_resultados(cantidad):
    jugadores={}
    juegos_posibles={'1':"4",'2':"8",'3':"6",'4':"",'5':"",'6':"",'E':"",'F':"",'P':"",'G':"",'D':"",'T':""}

    for i in range (0,cantidad):
        jugador=input("Nombre del jugador"+str(i))
        jugadores[jugador]= juegos_posibles

    return jugadores

def iniciar_cabecera(tablero):
    fila=""
    for jugador in tablero:
       fila= fila+"  " + str(jugador)

    return "Juegos " +fila

def obtener_jugadores(tablero):

    return tablero.keys


def mostrar_puntaje(tablero):

    jugadores=obtener_jugadores(tablero)
    for jugador in tablero:
        fila= tablero[jugador]

def dame_puntaje(tablero, jugador, juego):

    return tablero[jugador][juego]

def mostrar_resultados(tablero):
    lista_de_filas=[]
    juegos_posibles = ['1', '2', '3', '4', '5', '6', 'E', 'F', 'P', 'G','D','T']
    print(iniciar_cabecera(tablero))
    tripla=""
    for juego in juegos_posibles:
        for jugador in tablero:
            tripla=tripla+"\t"+dame_puntaje(tablero,str(jugador),juego)
        lista_de_filas.append(str(juego)+"\t" +tripla)
        #limpio la tripla para la proxima categoria
        tripla=""

    for i in range(0,len(lista_de_filas)):
        print("   "+str(lista_de_filas[i]))

#cantidad_de_jugadores = int(input("ingrese canitdad de jugadores"))
#jugadores=iniciar_tabla_resultados(cantidad_de_jugadores)
juegos_posibles1={'1':"4",'2':"8",'3':"6",'4':"20",'5':"5",'6':"18",'E':"25",'F':"30",'P':"40",'G':"50",'D':"0",'T':""}
juegos_posibles2={'1':"2",'2':"6",'3':"6",'4':"16",'5':"20",'6':"6",'E':"20",'F':"35",'P':"40",'G':"0",'D':"0",'T':""}
jugadores={'nico':juegos_posibles1,'javi':juegos_posibles2}
#print(obtener_jugadores(jugadores))
mostrar_resultados(jugadores)

#print(iniciar_cabecera(jugadores))