from Validar import dniValido

def eliminarCliente(dicClientes):
    '''
    - Elimina un cliente del sistema.
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno:
        Diccionario "dicClientes" con el cliente seleccionado eliminado.
    '''
    print("-----------------------------------\n ELIMINAR CLIENTE\n-----------------------------------")
    dni = dniValido("darle de baja")

    # Verificar si el DNI está en el diccionario
    if dni in dicClientes:  
        del dicClientes[dni]  # Eliminar el cliente
        print(f"Cliente con DNI {dni} eliminado.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
    return
