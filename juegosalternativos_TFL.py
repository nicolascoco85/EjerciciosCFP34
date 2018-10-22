tirada=[3,3,3,3,1]

def ordenar_tirada(tirada):
    #Comentario:
    tirada_ordenada=sorted(tirada)
    return tirada_ordenada

def esEscalera(tirada_ordenada):
    if(tirada_ordenada==[1,2,3,4,5] or tirada_ordenada==[2,3,4,5,6]):
       return True
    else:
        return False


def esFull(tirada_ordenada):
    #Comentario:
   if(tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[3]==tirada_ordenada[4] or tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[2]==tirada_ordenada[3] and tirada_ordenada[3]==tirada_ordenada[4]):
       return print("Full")

def esPoker(tirada_ordenada):
    if(tirada_ordenada[0]==tirada_ordenada[1] and tirada_ordenada[1]==tirada_ordenada[2]and tirada_ordenada[2]==tirada_ordenada[3] or tirada_ordenada[1]==tirada_ordenada[2] and tirada_ordenada[2]==tirada_ordenada[3]and tirada_ordenada[3]==tirada_ordenada[4]):
        return print("Poker")

mostrar_tirada=ordenar_tirada(tirada)
print(mostrar_tirada)
resultado=esEscalera(mostrar_tirada)
resulatao2=esFull(mostrar_tirada)
resultado3=esPoker(mostrar_tirada)