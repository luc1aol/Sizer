def cargarClientes(clientes):
    while True:
        dni = input("Ingrese el DNI del cliente (o '0' para terminar): ")
        if dni == '0':
            print("Finalizando la carga de clientes.")
            break
        if dni in clientes:
            print(f"El cliente con DNI {dni} ya existe.")
        else:
            nombre = input("Ingrese el nombre del cliente: ")
            direccion = input("Ingrese la dirección del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            clientes[dni] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'pedidos': []}
            print(f"Cliente {nombre} agregado exitosamente.")
    return 