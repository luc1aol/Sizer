from Validar import dniValido

def eliminarCliente(dicClientes):
    print("-----------------------------------\n ELIMINAR CLIENTE\n-----------------------------------")
    dni = dniValido("darle de baja")

    # Verificar si el DNI está en el diccionario
    if dni in dicClientes:  
        del dicClientes[dni]  # Eliminar el cliente
        print(f"Cliente con DNI {dni} eliminado.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
    return
