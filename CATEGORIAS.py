#jugada: representa a los cinco dados
#valor: el valor del dado que estoy buscando en mi jugada
#retorno, cantidad de veces que aparece

def alNumero(jugada,valor):
    cantidad_de_repeticiones=0

    for dado in jugada:
        if dado==valor:
            cantidad_de_repeticiones=cantidad_de_repeticiones+1
    return cantidad_de_repeticiones

def numeros_por_dado(jugada):
    lista_de_apariciones=[]
    for i in range(1,7):
        lista_de_apariciones.append(alNumero(jugada,i))
    return lista_de_apariciones

def esPoker (apariciones_por_dado):
    return 4 in apariciones_por_dado

def esGenerala (apariciones_por_dado):
    return 5 in apariciones_por_dado

def esFull (apariciones_por_dado):
    return 3 and 2 in apariciones_por_dado
