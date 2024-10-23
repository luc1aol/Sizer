from Validar import dniValido

def actualizarCliente(dicClientes):
    '''
    - Actualiza los datos de un cliente seleccionado (nombre, dirección o telefono).
    - Parámetros: 
        Diccionario "dicClientes", con la información de los clientes.
    -Retorno:
        Diccionario "dicClientes" con la información actualizada.
    '''
    print("-----------------------------------\n EDITAR CLIENTE\n-----------------------------------")
    dni = dniValido("actualizar")
    
    # Verificar si el DNI está en el diccionario de clientes
    if dni in dicClientes:
        print("Cliente encontrado!")
        print(f"DNI: {dni}")
        for dni, detalles in dicClientes.items():
            print(f"Nombre: {detalles['nombre']}")
            print(f"Domicilio: {detalles['domicilio']}")
            print(f"Teléfono: {detalles['telefono']}")
            
        # Solicitar nuevos datos
        nuevos_datos = {
            "nombre": input("Ingrese el nuevo nombre del cliente (dejar en blanco para no cambiar): "),
            "domicilio": input("Ingrese la nueva dirección del cliente (dejar en blanco para no cambiar): "),
            "telefono": input("Ingrese el nuevo teléfono del cliente (dejar en blanco para no cambiar): ")
        }   

        # Actualizar solo los campos que no están vacíos
        for llave, nuevoValor in nuevos_datos.items():
            if nuevoValor:
                dicClientes[dni][llave] = nuevoValor
        
        print("Cliente actualizado exitosamente.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
        