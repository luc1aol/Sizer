def listarClientes(dicClientes):
    if not dicClientes:
        print("No se encuentran clientes registrados.")
    else:
        for dni, dato in dicClientes.items():
            print(f"DNI: {dni}, Nombre: {dato['nombre']}, Dirección: {dato['direccion']}, Teléfono: {dato['telefono']},")
    return