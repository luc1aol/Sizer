import time

def diaSiguiente(dia, mes, anio):
    # Último día de los meses largos
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        ultimoDiaDelMes = 31
    # Último día de los meses cortos
    elif mes in [4, 6, 9, 11]:
        ultimoDiaDelMes = 30
    # Último día de febrero según el año sea bisiesto o no
    elif mes == 2:
        if ((anio % 4 == 0) and not(anio % 100 == 0)) or (anio % 400 == 0):
            ultimoDiaDelMes = 29
        else:
            ultimoDiaDelMes = 28

    # Cálculo final del día seguiente
    if dia < ultimoDiaDelMes:
        dia = dia + 1
    else:
        dia = 1
        if mes < 12:
            mes = mes + 1
        else:
            mes = 1
            anio = anio + 1

    return dia, mes, anio


# Se itera la función dia siguiente n veces hasta llegar a la cantidad de días que necesitamos y
#   nos retorne un valor de día, mes y año válidos
def sumarDias(dia, mes, anio, n):
    for _ in range(n):
        dia, mes, anio = diaSiguiente(dia, mes, anio)
    return [dia, mes, anio]


def generarFecha():
    seconds = time.time()
    result = time.localtime(seconds)

    anio = result.tm_year
    mes = result.tm_mon
    dia = result.tm_mday
    hora = result.tm_hour
    minuto = result.tm_min
    seg = result.tm_sec

    fechaPedido = [anio, mes, dia, hora, minuto, seg]
    # Para la fecha de entrega, sabemos que son 15 días más por defecto
    fechaEntrega = sumarDias(dia, mes, anio, 15)
    
    return fechaPedido, fechaEntrega




