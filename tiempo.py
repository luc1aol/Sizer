# Acá van a ir las funciones y todo lo relacionado con el apartado pedidos.
import random
import time
# Inicializamos el primer pedido con un valor de id=10
#idPedidoActual=10


# Acá va una función para hallar la fecha actual y asignarla al pedido
#   Las fechas que necesitamos en el pedido son la fecha en que se confirmó el pedido y la de entrega 
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
    fechaEntrega = None  #¿Cómo calcular el plazo de entrega de cada producto?


# Esta función recibe id del cliente y un diccionario de diccionarios
# {{{producto1},{cantidad}},{producto2},{cantidad}}
#def nuevoPedido(cliente, producto_cantidad):

    id_pedido = idPedidoActual

    # Lo hacemos autoincremenetal
    idPedidoActual +=1
    
    # Bloque para anclar la fecha actual al pedido
    # 
    # 
    
    # Bloque para extraer los datos del diccionario producto_cantidad que pedimos por parametro
    # 
    # 

    # Bloque para contabilizar el total del pedido en base a la cantidad y el costo de cada producto
    # 
    # 

    # Vamos a tener que retornar un diccionario que contenga toda la info junta
    return
