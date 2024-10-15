def actualizarProducto(productos):
    while True:
        nombre_producto = input("Ingrese el nombre del producto a actualizar (o '0' para volver): ")
        
        if nombre_producto == '0':
            print("Volviendo al menú anterior.")
            break
        
        if nombre_producto in productos:
            print(f"Producto seleccionado: {nombre_producto}")
            
            # Preguntar qué desea actualizar
            print("¿Qué desea actualizar?")
            print("[1] Precio")
            print("[2] Stock")
            print("[3] Ambos")
            print("[0] Cancelar")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombre_producto} (actual: ${productos[nombre_producto]['precio']}): "))
                productos[nombre_producto]['precio'] = nuevo_precio
                print(f"Precio actualizado a ${nuevo_precio} para {nombre_producto}.")
                
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