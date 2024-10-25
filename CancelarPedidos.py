from Validar import dniValido

def cancelarPedido(dicClientes):
    '''
    - Cancela un pedido de un cliente seleccionado.
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno:
        Se elimina el pedido seleccionado del dicClientes.
    '''
    print("-----------------------------------\n CANCELAR PEDIDO\n-----------------------------------")
    while True:
        dni = dniValido("cancelar sus pedidos")

        if dni == 0:
            print("Finalizando...")
            break

        if dni not in dicClientes:
            print(f"No se encontró un cliente con el DNI {dni}. Intente de nuevo.")
            continue

        pedidos = dicClientes[dni].get('pedidos', {})

        if not pedidos:
            print(f"Este cliente no tiene pedidos activos.")
            continue

        print(f"Pedidos del cliente con DNI {dni}:")
        for idPedido, detalles in pedidos.items():
            print(f"  Pedido ID: {idPedido} - Fecha de pedido: {detalles['fecha']} - Fecha de entrega: {detalles['fecha_entrega']}")

        idPedidoCancelar = int(input("Ingrese el ID del pedido que desea cancelar (0 para salir): "))

        if idPedidoCancelar == 0:
            print("Finalizando cancelación de pedidos...")
            break

        if idPedidoCancelar not in pedidos:
            print(f"No se encontró un pedido con ID {idPedidoCancelar}. Intente nuevamente.")
            continue

        del dicClientes[dni]['pedidos'][idPedidoCancelar]
        print(f"Pedido {idPedidoCancelar} cancelado exitosamente.")
    
    return dicClientes