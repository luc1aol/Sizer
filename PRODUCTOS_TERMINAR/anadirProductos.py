def agregarProducto(productos):
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
