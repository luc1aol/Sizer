import json

def cargarProductosDesdeArchivo():
    '''Cargar los productos desde un archivo JSON.'''
    try:
        file = open("productos.json", mode="r", encoding="utf-8")
        dicProductos = json.load(file)
        file.close()
        return dicProductos
    except FileNotFoundError:
        # Si el archivo no existe, retornamos un diccionario vacío
        return {}

def guardarProductoEnArchivo(dicProductos):
    '''Guardar los clientes en un archivo JSON.'''
    try:
        file = open("productos.json", mode="w", encoding="utf-8")
        json.dump(dicProductos, file, ensure_ascii=False, indent=4)
        file.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abirir archivo:", detalle)

#actualizar el precio
def actualizarPrecio(productoLista,productoID,precio_nuevo):
    productoLista[productoID]['precio'] = precio_nuevo
    print(f"El precio ha sido actualizado para {productoLista[productoID]['Producto']}. Precio actual: {productoLista[productoID]['precio']}")

    return

# se actualiza el stock
def actualizarStock(dicProductos, idProducto):
    """
    Actualiza el stock por talle de un producto utilizando su ID.
    Permite sumar o restar stock por cada talle.
    """

    # Verificar si el producto con el ID existe en el diccionario
    if idProducto not in dicProductos:
        print(f"Producto con ID {idProducto} no encontrado.")
        return

    print(f"\nStock actual del producto '{dicProductos[idProducto]['Producto']}':")
    
    # Mostrar el stock actual por talle
    for talle, info in dicProductos[idProducto]['talles'].items():
        print(f"  {talle.upper()}: {info['stock']} unidades")

    print("\nIngrese la cantidad a sumar (+) o restar (-) para cada talle. Presione Enter si no desea modificar el talle.")

    # Iterar por cada talle y actualizar el stock según lo ingresado
    for talle, info in dicProductos[idProducto]['talles'].items():
        cambio_stock = input(f"Cantidad para {talle.upper()} (actual: {info['stock']}): ")
        
        # Si el usuario no presiona Enter y deja el campo vacío, no se modificará el stock
        if cambio_stock.strip():  
            try:
                cantidad = int(cambio_stock)  # Convertir la entrada a un número entero
                nuevo_stock = info['stock'] + cantidad
                
                if nuevo_stock >= 0:
                    dicProductos[idProducto]['talles'][talle]['stock'] = nuevo_stock
                    print(f"El stock de {talle.upper()} ha sido actualizado a {nuevo_stock} unidades.")
                else:
                    print(f"No es posible reducir el stock de {talle.upper()} por debajo de 0. No se realizaron cambios.")
            except ValueError:
                print(f"Entrada no válida para el talle {talle.upper()}, el stock no fue modificado.")

    print(f"\nStock actualizado para el producto '{dicProductos[idProducto]['Producto']}':")
    
    # Mostrar el nuevo stock actualizado por talle
    for talle, info in dicProductos[idProducto]['talles'].items():
        print(f"  {talle.upper()}: {info['stock']} unidades")

    # Guardar los cambios en el archivo
    guardarProductoEnArchivo(dicProductos)




def listarProductos(dicProductos):
    '''
    - Imprime una lista de los productos con su precio y stock.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Impresión por pantalla del listado resultante.
    '''
    if dicProductos:
        print("\nListado de productos:")
        print("-----------------------------")
        for id, detalles in dicProductos.items():
            print(f" ID: {id}")
            print((f" Producto: {detalles['Producto']}"))
            print((f" Descripcion: {detalles['descripcion']}"))
            print(f" Precio: ${detalles['precio']}")

            print(f" Stock por talle:")
            for talle, info in detalles['talles'].items():
                print(f"    {talle.upper()}: {info['stock']} unidades")  #con el UPPER las pongo en MAYUSCULA al mostrar por pantalla

            print("-----------------------------")
    
    else:
        print("No hay productos disponibles.")
    return

def agregarProducto(dicProductos):
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
        
        ## Invocamos el JSON que contiene el archivo de productos
        dicProductos=cargarProductosDesdeArchivo()

        if nombreProducto in dicProductos:
            print(f"El producto '{nombreProducto}' ya existe")
        else:
            ultimo_id = max(dicProductos.keys(), default=1000)  # Obtiene el ID más alto o 1000 si está vacío
            nuevo_id = int(ultimo_id) + 1  # Incrementa el ID

            # Solicitar datos del producto
            descripcion = input("Ingrese la descripción del producto: ")
            marca = input("Ingrese la marca del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            talles=['s', 'm', 'l', 'xl', 'xx']
            stockPorTalle = {}
            for t in talles:
                stock = int(input(f"Ingrese el stock para talle {t.upper()}: "))  # Solicita el stock por talle
                stockPorTalle[t] = {"stock": stock}  # Asigna el stock al talle correspondiente

            # Agregar el producto al diccionario
            dicProductos[nuevo_id] = {
                "Producto": nombreProducto,
                "descripcion": descripcion,
                "marca": marca,
                "talles": stockPorTalle,
                "precio": precio,
            }

            print(f"Producto '{nombreProducto}' agregado con éxito con ID {nuevo_id}!")
            guardarProductoEnArchivo(dicProductos)
    

def actualizarProducto(dicProductos):
    '''
    - Actualiza el precio y/o el stock de los productos.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con los parámetros actualizados.
    '''
    while True:
        
        idProducto = input("Ingrese el ID del producto a actualizar (o 0 para volver): ")
        
        if idProducto == "0":
            print("Volviendo al menú anterior.")
            break
        
        if idProducto in dicProductos:
            print(f"Producto seleccionado: {idProducto}")
            
            # Preguntar qué desea actualizar
            print("¿Qué desea actualizar?")
            print("[1] Precio")
            print("[2] Stock")
            print("[0] Cancelar")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {idProducto} (actual: ${dicProductos[idProducto]['precio']}): "))
                actualizarPrecio(dicProductos,idProducto,nuevo_precio)
                
            elif opcion == "2":
                actualizarStock(dicProductos,idProducto)
                   
            elif opcion == "0":
                print("Actualización cancelada.")
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró un producto llamado '{idProducto}'.")
        guardarProductoEnArchivo(dicProductos)
               
    return 

def eliminarProducto(dicProductos):
    '''
    - Elimina uno o más productos.
    - Parámetros: 
        Diccionario "productos": Nombre del producto, stock, precio.
    -Retorno:
        Diccionario "productos" con el o los productos seleccionados eliminados.
    '''
    while True:
        idProducto = input("Ingrese el ID del producto que quiere eliminar o 0 para volver: ")
        
        if idProducto == "0":
            print("Volviendo al menú")
            break
        
        # verifica si el producto existe
        if idProducto in dicProductos:
            # se elimina el producto
            del dicProductos[idProducto]    #no se puede usar pop----   solucion: <del productos[nombreProducto]>
            print(f"Producto '{idProducto}' eliminado")
        else:
            print(f"No se encontró el producto '{idProducto}'")
    return 
