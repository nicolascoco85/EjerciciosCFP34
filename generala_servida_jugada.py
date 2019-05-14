def definirGeneralaServida(tirada, intento):
    if (intento>3) or (intento<1):
        return KeyError
    if (tirada.count(max(tirada)) == 5) and (intento==1):
        puntaje = True
    else:
        puntaje = False
    return puntaje

