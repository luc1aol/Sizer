def actualizarCliente(clientes):
    dni = input("Ingrese el DNI a actualizar: ")
    
    # Verificar si el DNI está en el diccionario de clientes
    if dni in clientes:
        print("Cliente encontrado:")
        print(f"Nombre: {clientes[dni]['nombre']}")
        print(f"Dirección: {clientes[dni]['direccion']}")
        print(f"Teléfono: {clientes[dni]['telefono']}")
        
        # Solicitar nuevos datos
        nuevo_nombre = input("Ingrese el nuevo nombre del cliente (dejar en blanco para no cambiar): ")
        nueva_direccion = input("Ingrese la nueva dirección del cliente (dejar en blanco para no cambiar): ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente (dejar en blanco para no cambiar): ")
        
        # Actualizar solo los campos que tienen nuevo valor
        if nuevo_nombre:
            clientes[dni]['nombre'] = nuevo_nombre
        if nueva_direccion:
            clientes[dni]['direccion'] = nueva_direccion
        if nuevo_telefono:
            clientes[dni]['telefono'] = nuevo_telefono
        
        print("Cliente actualizado exitosamente.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")