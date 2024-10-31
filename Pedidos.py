from funcionesFechas import generarFecha
from Validar import dniValido

def generarPedido(dicClientes, dicProductos, idPedidoActual):
    '''
    - Ingresa un nuevo pedido al sistema.
    - Parámetros: 
        Diccionario "dicClientes", diccionario "dicProductos" y variable "idPedidoActual" (autoincremental)
    -Retorno:
        Se asigna el pedido al ciente, con su fecha de pedido, fecha de entrega y los productos pedidos.
    '''

    print("-----------------------------------\n GENERAR PEDIDO\n-----------------------------------")

    while True:
        dni = dniValido("generar un pedido")

        # Validamos
        if dni == 0:
            print("Finalizando...")
            break
        
        # Verificar que el cliente existe
        if dni not in dicClientes: 
            print(f"No se encontró un cliente con el DNI {dni}.")
            continue

        # Filtrar los productos con stock disponible
        productosDisp = {}
        for llave, datos in dicProductos.items():
            if datos.get('stock') > 0:
                productosDisp[llave] = datos


        if not productosDisp:
            print("No hay productos disponibles en stock para generar un pedido.")
            return

        # Mostrar productos disponibles
        print("Productos disponibles:\n--------------------------")
        for llave, datos in productosDisp.items():
            talles = ", ".join(datos['talle'])
            print(f"{llave}: {datos['Producto']} - {datos['descripcion']} - Marca: {datos['marca']} - Talles: {talles} - Precio: ${datos['precio']} - Stock: {datos['stock']} unidades")
        print("--------------------------")

        # Recibir selección de productos
        pedido = {}
        while True:
            producto_id = int(input("Ingrese el ID del producto que desea agregar (0 para finalizar pedido): "))
            
            # Validación del id
            if producto_id == 0:
                print("Finalizando generación de pedidos...")
                break

            if producto_id not in productosDisp:
                print("Producto no válido o sin stock. Intente nuevamente.")
                continue

            # Mostrar y seleccionar el talle
            tallesDisp= productosDisp[producto_id]['talle']
            print(f"Talles disponibles para {productosDisp[producto_id]['Producto']}: {', '.join(tallesDisp)}")
            
            while True:
                talle = input("Ingrese el talle deseado: ")
                if talle not in tallesDisp:
                    print("Talle no válido. Por favor, elija un talle disponible.")
                    continue
                break
            
            # Agregar la cantidad pedida
            while True:
                cantidad = int(input(f"Ingrese la cantidad de {productosDisp[producto_id]['Producto']} que desea (0 para cancelar): "))
                
                # Salir del bucle de cantidad para seleccionar otro producto
                if cantidad == 0:
                    print("Carga de cantidad cancelada...")
                    break  

                if cantidad > productosDisp[producto_id]['stock']:
                    print("No hay suficiente stock. Intente con una cantidad menor.")
                    continue
                else:
                    # Actualizar stock y agregar al pedido
                    productosDisp[producto_id]['stock'] -= cantidad
                    pedido[producto_id] = {
                        'Producto': productosDisp[producto_id]['Producto'],
                        'cantidad': cantidad,
                        'precio': productosDisp[producto_id]['precio']
                    }
                    break 

            # Asociar el pedido con el cliente
            if pedido:
                fechaPedido, fechaEntrega = generarFecha()
                dicClientes[dni]['pedidos'][idPedidoActual] = {
                    'fecha': fechaPedido,
                    'fecha_entrega': fechaEntrega,
                    'productos': pedido
                }
                print(f"Pedido generado exitosamente con el ID: {idPedidoActual}")
                idPedidoActual += 1  # Incrementa el ID para el próximo pedido
            else:
                print("No se agregó ningún producto al pedido.")
    return 
# Definimos la función listarPedidos que toma como parámetro el diccionario de clientes
# Recorremos el diccionario de clientes, donde 'dni' es la clave y 'detalles' es el valor
# Accedemos al diccionario de pedidos del cliente actual usando el método 'get'
# Si no tiene pedidos, devolvemos un diccionario vacío por defecto
# Si el diccionario de pedidos está vacío, informamos que no hay pedidos
# Si el cliente tiene pedidos, recorremos cada pedido en el diccionario 'pedidos'
# Iteramos sobre los productos en el pedido. 'productos' es un diccionario dentro de 'detalles'
def listarPedidos(dicClientes):
    print("-----------------------------------\n LISTAR PEDIDOS\n-----------------------------------")
    for dni, detalles in dicClientes.items():
            print(f"\nDNI del cliente: {dni}")
            
            # Acceder al diccionario de pedidos del cliente actual
            pedidos = detalles.get('pedidos', {})

            if pedidos == {}:
                print("    -No hay pedidos")
            
            for idPedido, detalles in pedidos.items():
                print(f"  ID del pedido: {idPedido}")
                print(f"    Fecha de pedido: {detalles['fecha']}")
                print(f"    Fecha de entrega: {detalles['fecha_entrega']}")
                print(f"    Productos:")
                
                for producto_id, producto_info in detalles['productos'].items():
                    print(f"      - {producto_info['nombre_producto']}:")
                    print(f"        Cantidad: {producto_info['cantidad']} unidades")
                    print(f"        Precio unitario: ${producto_info['precio']}")
                    print(f"        Subtotal: ${producto_info['cantidad'] * producto_info['precio']}")    
    return 
def cancelarPedido(dicClientes):
    '''
    - Cancela un pedido de un cliente seleccionado.
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno:
        Se elimina el pedido seleccionado del dicClientes anclado a un cliente.
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
        
        # .get(key, valor por default)
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