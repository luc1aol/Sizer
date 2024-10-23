# Comprobamos si el diccionario de clientes está vacío
# Si el diccionario está vacío, mostramos un mensaje indicando que no hay clientes registrados
# Si el diccionario no está vacío, recorremos cada cliente en el diccionario

def listarClientes(dicClientes):
    '''
    - Imprime una lista de los clientes con sus datos (DNI, nombre completo, domicilio y telefono).
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno: --
    '''
    print("-----------------------------------\n LISTADO CLIENTES\n-----------------------------------")
    if not dicClientes:
        print("No se encuentran clientes registrados.")
    else:
        for dni, detalles in dicClientes.items():
            print(f"DNI: {dni}, Nombre: {detalles['nombre']}, Apellido: {detalles['apellido']}, Domicilio: {detalles['domicilio']}, Teléfono: {detalles['telefono']}")
    return