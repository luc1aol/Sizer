import time

def esBisiesto(año):
    """
    Funcion para verificar si un año es bisiesto.
    PARAMETROS:
        año el cual se quiere controlar.
    SALIDA:
        True si el año es biesiesto o False si el año no es bisiesto.
    """
    bisiesto = False
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        bisiesto = True
    return bisiesto

def fecha():
    #Detectar que el pedido esta confirmado 
    aux = time.localtime()
    año = aux.tm_year
    mes = aux.tm_mon
    dia = aux.tm_mday
    hora = aux.tm_hour
    minuto = aux.tm_min
    seg = aux.tm_sec
    fechaPedido = str(dia)+ "/" + str(mes) + "/" + str(año) + " " + str(hora) + ":" + str(minuto) + ":" + str(seg)
    entrega = fechaEntrega(dia,mes,año)
    return fechaPedido, entrega


def fechaEntrega(dia,mes,año):
    bisiesto = esBisiesto(año)
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10:
        if dia + 15 > 31:
            mes += 1
            dia = dia + 15 - 31
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
        else:
            dia += 15
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    elif mes == 12:
        if dia + 15 > 31:
            mes = 1
            año += 1
            dia = dia + 15 -31
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
        else:
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia + 15 > 30:
            mes += 1
            dia = dia + 15 - 30
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
        else:
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    elif mes == 2 and bisiesto == True:
        if dia + 15 > 29:
            mes += 1
            dia = dia + 15 - 29
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
        else:
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    elif mes == 2 and bisiesto == False:
        if dia + 15 > 28:
            mes += 1
            dia = dia + 15 - 28
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
        else:
            fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    fechaDeEntrega = str(dia) + "/" + str(mes) + "/" + str(año)
    return fechaDeEntrega

