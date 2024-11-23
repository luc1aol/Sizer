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
        for id, detalles in productos.items():
            print(f" ID: {id}")
            print((f" Producto: {detalles['Producto']}"))
            print((f" Descripcion: {detalles['descripcion']}"))
            print((f" Talle: {detalles['talle']}"))
            print(f" Precio: ${detalles['precio']}")
            print(f" Stock: {detalles['stock']} unidades")
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
            ultimo_id = max(productos.keys(), default=1000)  # Obtiene el ID más alto o 1000 si está vacío
            nuevo_id = ultimo_id + 1  # Incrementa el ID

            # Solicitar datos del producto
            descripcion = input("Ingrese la descripción del producto: ")
            marca = input("Ingrese la marca del producto: ")
            talle = input("Ingrese los talles separados por comas (ejemplo: s,m,l,xl,xx): ").split(',') #como uso split, me devuelve una lista
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad de stock disponible: "))

            # Agregar el producto al diccionario
            productos[nuevo_id] = {
                "Producto": nombreProducto,
                "descripcion": descripcion,
                "marca": marca,
                "talle": talle,
                "precio": precio,
                "stock": stock
            }

            print(f"Producto '{nombreProducto}' agregado con éxito con ID {nuevo_id}!")
            return productos
    

def actualizarProducto(productos):
    '''
    - Actualiza el precio y/o el stock de los productos.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con los parámetros actualizados.
    '''
    while True:
        
        idProducto = int(input("Ingrese el ID del producto a actualizar (o 0 para volver): "))
        
        if idProducto == 0:
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
                actualizarPrecio(productos,idProducto,nuevo_precio)
                
            elif opcion == "2":
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {idProducto} (actual: {productos[idProducto]['stock']} unidades): "))
                actualizar_stock(productos,idProducto,nuevo_stock)
                
            elif opcion == "3":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {idProducto} (actual: ${productos[idProducto]['precio']}): "))
                nuevo_stock = int(input(f"Ingrese el nuevo stock para {idProducto} (actual: {productos[idProducto]['stock']} unidades): "))
                actualizarPrecio(productos,idProducto,nuevo_precio)
                actualizar_stock(productos,idProducto,nuevo_stock)
                   
            elif opcion == "0":
                print("Actualización cancelada.")
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró un producto llamado '{idProducto}'.")
               
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
