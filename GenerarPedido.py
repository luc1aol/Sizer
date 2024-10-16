from FuncionesFechas import generarFecha
from Validar import dniValido

def generarPedido(dicClientes, dicProductos, idPedidoActual):

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
            talles = ", ".join(datos['talles'])
            print(f"{llave}: {datos['nombre_producto']} - {datos['descripcion']} - Marca: {datos['marca']} - Talles: {talles} - Precio: ${datos['precio']} - Stock: {datos['stock']} unidades")
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
            tallesDisp= productosDisp[producto_id]['talles']
            print(f"Talles disponibles para {productosDisp[producto_id]['nombre_producto']}: {', '.join(tallesDisp)}")
            
            while True:
                talle = input("Ingrese el talle deseado: ")
                if talle not in tallesDisp:
                    print("Talle no válido. Por favor, elija un talle disponible.")
                    continue
                break
            
            # Agregar la cantidad pedida
            while True:
                cantidad = int(input(f"Ingrese la cantidad de {productosDisp[producto_id]['nombre_producto']} que desea (0 para cancelar): "))
                
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
                        'nombre_producto': productosDisp[producto_id]['nombre_producto'],
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