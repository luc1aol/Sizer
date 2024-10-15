def listarClientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for dni, detalles in clientes.items():
            print(f"DNI: {dni}, Nombre: {detalles['nombre']}, Dirección: {detalles['direccion']}, Teléfono: {detalles['telefono']}")
    return