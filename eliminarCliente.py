def eliminarCliente(clientes):
    dni = input("Ingrese el DNI del cliente a eliminar: ")# Solicitar el DNI al usuario y eliminar espacios
    if not dni:  # Validar que el DNI no esté vacío
        print("El DNI no puede estar vacío. Inténtalo de nuevo.")
        return

    if dni in clientes:  # Verificar si el DNI está en el diccionario
        del clientes[dni]  # Eliminar el cliente
        print(f"Cliente con DNI {dni} eliminado.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
    return