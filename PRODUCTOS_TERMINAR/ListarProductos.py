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