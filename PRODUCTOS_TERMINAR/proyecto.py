def mostrarProductos():   #todos los talles tienen el mismo precio
    productos = {
    1001: {"Producto": "Remera","descripcion": "Remera de algodón","marca": "Marca Escolar","talle": ['s','m','l','xl','xx'],"precio": 10000,"stock": 10},
    1002: {"Producto":"Chomba","descripcion": "Chomba de piqué poliester","marca": "Marca Escolar","talle": ['s','m','l','xl','xx'],"precio": 15000,"stock": 15},
    1003: {"Producto":"Pantalon","descripcion": "Algodon Rustico y frizado","marca": "Marca Escolar","talle": ['s','m','l','xl','xx'],"precio": 15000,"stock": 20}
    }
    return productos


#actualizar el precio
def actualizarPrecio(productoLista,productoID,precio_nuevo):
    productoLista[productoID]['precio'] = precio_nuevo
    print(f"El precio ha sido actualizado para {productoLista[productoID]['Producto']}. Precio actual: {productoLista[productoID]['precio']}")

    return

# se actualiza el stock
def actualizar_stock(productoLista,productoNombre, cantidad):
    producto = productoLista.get(productoNombre)
    if producto:
        if producto["stock"] + cantidad >= 0:

            producto["stock"] += cantidad   #se suma la cantidad 
            print(f"El stock ha sido actualizado para {productoNombre}. Stock actual: {producto['stock']}")
        else:
            print("No es posible actualizar el stock. La cantidad es insuficiente.")

    else:
        print("Producto no encontrado.")



#submenu de actualizar producto
def actualizarProducto():
    productosLista=mostrarProductos()   #lo llamo a esta zona local para poder trabajar con ella
    while True:
        nombreProductoID = int(input("Ingrese el nombre del producto a actualizar (o '0' para volver): "))
        
        if nombreProductoID == 0:     #dado que la entrada es un entero, y debe comparar con otro entero, 
            print("Volviendo al menú anterior.")
            break
        

        if nombreProductoID in productosLista:
            print(f"Producto seleccionado: {nombreProductoID}")
            
            # Preguntar qué desea actualizar
            print("¿Qué desea actualizar?")
            print("[1] Precio")
            print("[2] Stock")
            print("[3] Ambos")
            print("[0] Cancelar")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombreProductoID} (actual: ${productosLista[nombreProductoID]['precio']}): "))
                actualizarPrecio(productosLista,nombreProductoID,nuevo_precio)
                
            elif opcion == "2":
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {nombreProductoID} (actual: {productosLista[nombreProductoID]['stock']} unidades): "))
                actualizar_stock(productosLista,nombreProductoID,nuevo_stock)
                
            elif opcion == "3":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {nombreProductoID} (actual: ${productosLista[nombreProductoID]['precio']}): "))
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {nombreProductoID} (actual: {productosLista[nombreProductoID]['stock']} unidades): "))
                actualizarPrecio(productosLista,nombreProductoID,nuevo_precio)
                actualizar_stock(productosLista,nombreProductoID,nuevo_stock)
                
            
                
            elif opcion == "0":
                print("Actualización cancelada.")
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró un producto llamado '{nombreProductoID}'.")


actualizarProducto()