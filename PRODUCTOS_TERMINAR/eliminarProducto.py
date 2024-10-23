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
        nombreProducto = input("Ingrese el nombre del producto que quiere eliminar o 0 para volver: ")
        
        if nombreProducto == '0':
            print("Volviendo al menú")
            break
        
        # verifica si el producto existe
        if nombreProducto in productos:
            # se elimina el producto
            productos.pop(nombreProducto)    #no se puede usar pop----   solucion: <del productos[nombreProducto]>
            print(f"Producto '{nombreProducto}' eliminado")
        else:
            print(f"No se encontró el producto '{nombreProducto}'")


