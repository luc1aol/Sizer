def listarPedidos(dicClientes):
    for dni, detalles in dicClientes.items():
            print(f"\nDNI del cliente: {dni}")
            
            # Acceder al diccionario de pedidos del cliente actual
            pedidos = detalles.get('pedidos', {})
            
            # Recorred cada pedido de por cada cliente
            for idPedido, detalles in pedidos.items():
                print(f"  ID del pedido: {idPedido}")
                print(f"    Fecha de pedido: {detalles['fecha']}")
                print(f"    Fecha de entrega: {detalles['fecha_entrega']}")
                print(f"    Productos:")
                
                # Iterar sobre los productos en el pedido
                for producto_id, producto_info in detalles['productos'].items():
                    print(f"      - {producto_info['nombre_producto']}:")
                    print(f"        Cantidad: {producto_info['cantidad']} unidades")
                    print(f"        Precio unitario: ${producto_info['precio']}")
                    print(f"        Subtotal: ${producto_info['cantidad'] * producto_info['precio']}")    