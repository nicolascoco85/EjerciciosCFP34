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




sePlanta=False
print("comencemos a jugar")
tirada_elegida=[]
intentos=0
while (sePlanta==False and intentos<3):
    tirada_elegida=juego.dame_tirada()
    intentos=intentos+1
    print(tirada_elegida)
    if(intentos!=3):
        sePlanta = sePlanto()



print("La tirada final fue: ", tirada_elegida)
print("JUEGOS CANDIDATOS")
print("Escalera", esc.esEscalera(tirada_elegida))
print("Full", je.esFull(tirada_elegida))
print("Poker", je.esPoker(tirada_elegida))
print("Generala", je.esGenerala(tirada_elegida))