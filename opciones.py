import azar as juego
import JuegosEspeciales as je
import juegosalternativos_TFL as esc
def sePlanto():

    decision= input("Desea plantarse?Y/N")
    if (decision.upper()=="Y"):
        return True
    else:
        return False

def mensajes_por_intentos(intentos):

    if(intentos==2):
        print("Mucha suerte, este es tu ultimo intento")
    if (intentos != 3):
        print("No te desanimes :)")
    else:
        print("No te quedan más intentos.")

def mostrar_juegos_especiales_candidatos(tirada):

    if esc.esEscalera(tirada) :
        print("ESCALERA")
    else:
        if je.esFull(tirada):
            print("FULL")
        else:
            if je.esPoker(tirada):
                print("POKER")
            else:
                if je.esGenerala(tirada):
                    print("GENERALA")
                else:
                    print("NO TIENE JUEGOS ESPECIALES")


#Estado incial del Juego
sePlanta=False
print("comencemos a jugar")
tirada_elegida=[]
intentos=0
##########

while (sePlanta==False and intentos<3):
    tirada_elegida=juego.dame_tirada()
    ## SelecionarDados###


    #######
    intentos=intentos+1
    mensajes_por_intentos(intentos)
    print(tirada_elegida)
    if(intentos!=3):
        sePlanta = sePlanto()



print("La tirada final fue: ", tirada_elegida)

print("JUEGOS CANDIDATOS")
mostrar_juegos_especiales_candidatos(tirada_elegida)