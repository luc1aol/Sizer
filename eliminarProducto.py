# Funcion para eliminar un producto
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


