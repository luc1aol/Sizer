def listarClientes(dicClientes):
    if not dicClientes:
        print("No se encuentran clientes registrados.")
    else:
        for dni, detalles in dicClientes.items():
            print(f"DNI: {dni}, Nombre: {detalles['nombre']}, Domicilio: {detalles['domicilio']}, Teléfono: {detalles['telefono']}")
    return