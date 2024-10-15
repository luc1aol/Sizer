from Validar import dniValido

def cargarCliente(dicClientes):
    while True:
        dni = dniValido("cargar")

        if dni in dicClientes:
            print(f"El cliente con DNI: {dni} ya existe. Saltando...")
            continue # Saltar al siguiente ciclo sin solicitar más datos

        nombre = input("Ingrese el nombre del cliente: \n")
        apellido = input("Ingrese el apellido del cliente: \n")
        domicilio = input("Ingrese el domicilio del cliente: \n")
        telefono = input("Ingrese el télefono del cliente: \n")

        # Guardar los datos en el diccionario (Value,Key)
        dicClientes[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "domicilio": domicilio,
            "telefono": telefono,
            "pedidos": {} #Esto se inicializa vacío para llenarlo a medida que se hagan pedidos
        }
        
        return dicClientes