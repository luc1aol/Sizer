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
            
            pedidos = detalles.get('pedidos', {})

            if pedidos == {}:
                print("    -No hay pedidos")
            
            for idPedido, detalles in pedidos.items():
                print(f"  ID del pedido: {idPedido}")
                print(f"    Fecha de pedido: {detalles['fecha']}")
                print(f"    Fecha de entrega: {detalles['fecha_entrega']}")
                print(f"    Productos:")
                
                for producto_id, producto_info in detalles['productos'].items():
                    print(f"      - {producto_info['Producto']}:")
                    print(f"        Cantidad: {producto_info['cantidad']} unidades")
                    print(f"        Precio unitario: ${producto_info['precio']}")
                    print(f"        Subtotal: ${producto_info['cantidad'] * producto_info['precio']}")