# Acá van a ir las funciones y todo lo relacionado con el apartado pedidos.
import random
import time
import funcionesFechas

# Inicializamos el primer pedido con un valor de id=10
idPedidoActual=10

def fechas():
    fechaActual,fechaEntrega = funcionesFechas.fecha()
    #La función obtiene la fecha actual y la fecha de entrega del producto
    
# Esta función recibe id del cliente y un diccionario de diccionarios
# {{{producto1},{cantidad}},{p idad}}
def nuevoPedido(cliente, producto_cantidad):

    id_pedido = idPedidoActual

    # Lo hacemos autoincremenetal
    idPedidoActual +=1


    
    # Bloque para extraer los datos del diccionario producto_cantidad que pedimos por parametro
    # 
    # 

    # Bloque para contabilizar el total del pedido en base a la cantidad y el costo de cada producto
    # 
    # 

    # Vamos a tener que retornar un diccionario que contenga toda la info junta
    return

fechas()