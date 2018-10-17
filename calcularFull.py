import random

def dame_un_dado():
    return random.randrange(1,7)

def dame_tirada():
    tirada = []
    for dado in range (1,6):
        tirada.append(dame_un_dado())
    return tirada

def dado_esta_repito(numero,tirada):

    return  (numero, tirada.count(numero))

def esFull(tirada):
    repeticiones=[]
    hay_tres_repetido=False
    hay_dos_repetido=False

    #GUARDO EN UNA LISTA EL NUMERO QUE SALIO CON SUS REPETICIONES ASOCIADAS
    for i in range (0,len(tirada)):
        repeticiones.append(dado_esta_repito(tirada[i],tirada))

    #ANALIZO SI EXISTEN 3 REPETIDOS Y OTROS 2 REPETIDOS DENTRO DE LA LA MISMA TIRADA

    for j in range(0,len(repeticiones)):
        if (repeticiones[j][1]==3):
            hay_tres_repetido=True
        else:
            if(repeticiones[j][1]==2):
                hay_dos_repetido=True

    #EN CASO DE QUE HAYA 3 REPETIDOS Y OTROS DOS REPETIDOS TENEMOS FULL, CASO CONTRARIO NO EXISTE FULL
    return hay_tres_repetido and hay_dos_repetido


tirada=dame_tirada()
#tirada=[3,3,3,3,3]
print("Posee FULL?", esFull(tirada))
print("Su tirada fue:",tirada)