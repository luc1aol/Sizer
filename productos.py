def listarProductos(productos):
    '''
    - Imprime una lista de los productos con su precio y stock.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Impresión por pantalla del listado resultante.
    '''
    if productos:
        print("\nListado de productos:")
        print("-----------------------------")
        for nombre, detalles in productos.items():
            print(f"Producto: {nombre}")
            print(f"  Precio: ${detalles['precio']}")
            print(f"  Stock: {detalles['stock']} unidades")
            print("-----------------------------")
    else:
        print("No hay productos disponibles.")
    return
def agregarProducto(productos):
    '''
    - Agrega un nuevo producto a vender.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con el o los nuevos productos agregados.
    '''

    while True:
        nombreProducto = input("Ingrese el nombre del producto a añadir o '0' para volver: ")
        
        if nombreProducto == '0':
            print("Volviendo al menu")
            break
        
        if nombreProducto in productos:
            print(f"El producto '{nombreProducto}' ya existe")
        else:
            # solicita precio y stock
            precio = float(input(f"Ingrese el precio para {nombreProducto}: "))
            stock = int(input(f"Ingrese la cantidad de stock para {nombreProducto}: "))

            # agrega el nuevo producto al diccionario
            productos[nombreProducto] = {"precio": precio, "stock": stock}
            print(f"Producto '{nombreProducto}' añadido")
    return 
def actualizarProducto(productos):
    '''
    - Actualiza el precio y/o el stock de los productos.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con los parámetros actualizados.
    '''
    while True:
        idProducto = input("Ingrese el ID del producto a actualizar (o 0 para volver): ")
        
        if idProducto == '0':
            print("Volviendo al menú anterior.")
            break
        
        if idProducto in productos:
            print(f"Producto seleccionado: {idProducto}")
            
            # Preguntar qué desea actualizar
            print("¿Qué desea actualizar?")
            print("[1] Precio")
            print("[2] Stock")
            print("[3] Ambos")
            print("[0] Cancelar")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {idProducto} (actual: ${productos[idProducto]['precio']}): "))
                productos[idProducto]['precio'] = nuevo_precio
                print(f"Precio actualizado a ${nuevo_precio} para {idProducto}.")
                
            elif opcion == "2":
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {nombre_producto} (actual: {productos[nombre_producto]['stock']} unidades): "))
                productos[nombre_producto]['stock'] = nuevo_stock
                print(f"Stock actualizado a {nuevo_stock} unidades para {nombre_producto}.")
                
            elif opcion == "3":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombre_producto} (actual: ${productos[nombre_producto]['precio']}): "))
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {nombre_producto} (actual: {productos[nombre_producto]['stock']} unidades): "))
                
                productos[nombre_producto]['precio'] = nuevo_precio
                productos[nombre_producto]['stock'] = nuevo_stock
                
                print(f"Precio actualizado a ${nuevo_precio} y stock a {nuevo_stock} unidades para {nombre_producto}.")
                
            elif opcion == "0":
                print("Actualización cancelada.")
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró un producto llamado '{nombre_producto}'.")
    return 
def eliminarProducto(productos):
    '''
    - Elimina uno o más productos.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con el o los productos seleccionados eliminados.
    '''
    while True:
        idProducto = int(input("Ingrese el ID del producto que quiere eliminar o 0 para volver: "))
        
        if idProducto == 0:
            print("Volviendo al menú")
            break
        
        # verifica si el producto existe
        if idProducto in productos:
            # se elimina el producto
            del productos[idProducto]    #no se puede usar pop----   solucion: <del productos[nombreProducto]>
            print(f"Producto '{idProducto}' eliminado")
        else:
            print(f"No se encontró el producto '{idProducto}'")
    return 