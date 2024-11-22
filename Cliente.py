import json
from Validar import dniValido, telValido

def cargarClientesDesdeArchivo():
    '''Cargar los clientes desde un archivo JSON.'''
    try:
        file = open("clientes.json", mode="r", encoding="utf-8")
        dicClientes = json.load(file)
        file.close()
        return dicClientes
    except FileNotFoundError:
        # Si el archivo no existe, retornamos un diccionario vacío
        return {}

def guardarClientesEnArchivo(dicClientes):
    '''Guardar los clientes en un archivo JSON.'''
    try:
        file = open("clientes.json", mode="w", encoding="utf-8")
        json.dump(dicClientes, file, ensure_ascii=False, indent=4)
        file.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abirir archivo:", detalle)

def cargarCliente():
    '''
    - Agrega nuevos clientes al sistema, guardando su nombre, apellido y domicilio.
    - Parámetros: 
        Diccionario "dicClientes"
    - Retorno:
        Diccionario "dicClientes" con el cliente y sus datos agregados.
    '''
    print("-----------------------------------\n CARGAR CLIENTES \n-----------------------------------")
    while True:
        dni = dniValido("cargar")

        # Verificar si el usuario desea finalizar
        if dni == "0":
            print("Finalizando carga de clientes...")
            break
        
        # Invocamos el JSON que contiene el archivo de clientes
        dicClientes = cargarClientesDesdeArchivo()

        if dni in dicClientes:
            print(f"El cliente con DNI: {dni} ya existe. Saltando...")
            continue # Saltar al siguiente ciclo sin solicitar más datos

        nombre = input("Ingrese el nombre del cliente: \n")
        apellido = input("Ingrese el apellido del cliente: \n")
        domicilio = input("Ingrese el domicilio del cliente: \n")
        telefono = telValido("cargar")

        # Guardar los datos en el diccionario (Value, Key)
        dicClientes[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "domicilio": domicilio,
            "telefono": telefono,
            "pedidos": {}  # Esto se inicializa vacío para llenarlo a medida que se hagan pedidos
        }

        guardarClientesEnArchivo(dicClientes)

def listarClientes():
    '''
    - Imprime una lista de los clientes con sus datos (DNI, nombre completo, domicilio y telefono).
    '''
    dicClientes = cargarClientesDesdeArchivo()
    if not dicClientes:
        print("No se encuentran clientes registrados.")
    else:
        print("-" * 40)
        print("LISTADO DE CLIENTES")
        print("-" * 40)
        for dni, detalles in dicClientes.items():
            print(f"DNI: {dni}, Nombre: {detalles['nombre']}, Apellido: {detalles['apellido']}, Domicilio: {detalles['domicilio']}, Teléfono: {detalles['telefono']}")

def actualizarCliente():
    '''
    - Actualiza los datos de un cliente seleccionado (nombre, dirección o telefono).
    - Retorno:
        Diccionario "dicClientes" con la información actualizada.
    '''
    print("-----------------------------------\n EDITAR CLIENTE\n-----------------------------------")
    dni = dniValido("actualizar")
    dicClientes = cargarClientesDesdeArchivo()

    # Verificar si el DNI está en el diccionario de clientes
    print(dicClientes)
    if dni in dicClientes:
        print("Cliente encontrado!")
        detalles = dicClientes[dni]
        print(f"DNI: {dni}")
        print(f"Nombre: {detalles['nombre']}")
        print(f"Domicilio: {detalles['domicilio']}")
        print(f"Apellido: {detalles['apellido']}")
        print(f"Teléfono: {detalles['telefono']}")
        
        # Solicitar nuevos datos
        nuevos_datos = {
            "nombre": input("Ingrese el nuevo nombre del cliente (dejar en blanco para no cambiar): "),
            "apellido": input("Ingrese el nuevo apellido del cliente (dejar en blanco para no cambiar): "),
            "domicilio": input("Ingrese la nueva dirección del cliente (dejar en blanco para no cambiar): "),
            "telefono": input("Ingrese el nuevo teléfono del cliente (dejar en blanco para no cambiar): ")
        }

        # Actualizar solo los campos que no están vacíos
        for llave, nuevoValor in nuevos_datos.items():
            if nuevoValor:
                dicClientes[dni][llave] = nuevoValor
        
        print("Cliente actualizado exitosamente.")
        guardarClientesEnArchivo(dicClientes)
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")

def eliminarCliente():
    '''
    - Elimina un cliente del sistema.
    - Retorno:
        Diccionario "dicClientes" con el cliente seleccionado eliminado.
    '''
    print("-----------------------------------\n ELIMINAR CLIENTE\n-----------------------------------")
    dni = dniValido("darle de baja")
    dicClientes = cargarClientesDesdeArchivo()

    # Verificar si el DNI está en el diccionario
    if str(dni) in dicClientes:
        del dicClientes[dni]  # Eliminar el cliente
        print(f"Cliente con DNI {dni} eliminado.")
        guardarClientesEnArchivo(dicClientes)
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")