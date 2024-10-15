from Validar import dniValido

def actualizarCliente(dicClientes):

    dni = dniValido("actualizar")
    
    # Verificar si el DNI está en el diccionario de clientes
    if dni in dicClientes:
        print("Cliente encontrado!")
        print(f"DNI: {dni}")
        for key, value in dicClientes[dni].items():
            print(f"  {key.capitalize()}: {value}")
            
        # Solicitar nuevos datos
        nuevos_datos = {
            "nombre": input("Ingrese el nuevo nombre del cliente (dejar en blanco para no cambiar): "),
            "direccion": input("Ingrese la nueva dirección del cliente (dejar en blanco para no cambiar): "),
            "telefono": input("Ingrese el nuevo teléfono del cliente (dejar en blanco para no cambiar): ")
        }   

        # Actualizar solo los campos que no están vacíos
        for llave, nuevoValor in nuevos_datos.items():
            if nuevoValor:
                dicClientes[dni][llave] = nuevoValor
        
        print("Cliente actualizado exitosamente.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
        