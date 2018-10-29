def dado_esta_repetido(numero,tirada):

    return  (numero, tirada.count(numero))

def esFull(tirada):
    repeticiones=[]
    hay_tres_repetido=False
    hay_dos_repetido=False

    #GUARDO EN UNA LISTA EL NUMERO QUE SALIO CON SUS REPETICIONES ASOCIADAS
    for i in range (0,len(tirada)):
        repeticiones.append(dado_esta_repetido(tirada[i],tirada))

    #ANALIZO SI EXISTEN 3 REPETIDOS Y OTROS 2 REPETIDOS DENTRO DE LA LA MISMA TIRADA

    for j in range(0,len(repeticiones)):
        if (repeticiones[j][1]==3):
            hay_tres_repetido=True
        else:
            if(repeticiones[j][1]==2):
                hay_dos_repetido=True

    #EN CASO DE QUE HAYA 3 REPETIDOS Y OTROS DOS REPETIDOS TENEMOS FULL, CASO CONTRARIO NO EXISTE FULL
    return hay_tres_repetido and hay_dos_repetido

def esGenerala(tirada):
        for k in range(0,len(tirada)-1):
            if(tirada[k]!=tirada[k+1]):
                 return False
        return True

def esGeneralAlternativa(tirada):
    #Si la tupla que me devuelve tiene un 5 en
    #su cantidad de veces repetida, la tirada es una generala
    return dado_esta_repetido(tirada[0],tirada)[1]==5

def esPoker(tirada):
    return dado_esta_repetido(tirada[0],tirada)==4 or dado_esta_repetido(tirada[1],tirada)==4