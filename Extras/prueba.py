import json
from Validar import dniValido
from Validar import telValido

def cargarClientesDesdeArchivo():
    '''Cargar los clientes desde un archivo JSON.'''
    try:
        file = open("clientes.json", mode="r", encoding="utf-8")
        clientes = json.load(file)
        file.close()
        return clientes
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
        if dni == 0:
            print("Finalizando carga de clientes...")
            break
        
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
    return 

def listarClientes():
    '''
    - Imprime una lista de los clientes con sus datos (DNI, nombre completo, domicilio y telefono).
    - Parámetros: 
        Diccionario "dicClientes"
    - Retorno: --
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
    return

def actualizarCliente():
    '''
    - Actualiza los datos de un cliente seleccionado (nombre, dirección o telefono).
    - Parámetros: 
        Diccionario "dicClientes", con la información de los clientes.
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
    return 

def eliminarCliente():
    '''
    - Elimina un cliente del sistema.
    - Parámetros: 
        Diccionario "dicClientes"
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
    return

def main():
    clientes = {
    "12345678": {"nombre": "Juan", "apellido": "Pérez", "domicilio": "Calle Falsa 123", "telefono": "+5423456789"},
    "23456789": {"nombre": "María", "apellido": "López", "domicilio": "Avenida Siempreviva 456", "telefono": "+5487654321"},
    "34567890": {"nombre": "Carlos", "apellido": "Gómez", "domicilio": "Plaza Central 789", "telefono": "+5467890123"},
    "45678901": {"nombre": "Ana", "apellido": "Martínez", "domicilio": "Calle Luna 321", "telefono": "+5478901234"},
    "56789012": {"nombre": "Luis", "apellido": "Rodríguez", "domicilio": "Calle Sol 654", "telefono": "+5490123456"},
    "67890123": {"nombre": "Sofía", "apellido": "Sánchez", "domicilio": "Avenida del Parque 12", "telefono": "+5445678901"},
    "78901234": {"nombre": "Miguel", "apellido": "Díaz", "domicilio": "Calle Norte 98", "telefono": "+5401234567"},
    "89012345": {"nombre": "Elena", "apellido": "Morales", "domicilio": "Avenida Sur 74", "telefono": "+5434567890"},
    "90123456": {"nombre": "Pedro", "apellido": "Ramírez", "domicilio": "Calle Este 56", "telefono": "+5423098456"},
    "01234567": {"nombre": "Lucía", "apellido": "Torres", "domicilio": "Calle Oeste 44", "telefono": "+5467123890"},
    "11223344": {"nombre": "Javier", "apellido": "Navarro", "domicilio": "Plaza Mayor 22", "telefono": "+5478345901"},
    "22334455": {"nombre": "Laura", "apellido": "Méndez", "domicilio": "Calle Roja 11", "telefono": "+5490567123"},
    "33445566": {"nombre": "Raúl", "apellido": "Vargas", "domicilio": "Avenida Azul 23", "telefono": "+5434890345"},
    "44556677": {"nombre": "Carmen", "apellido": "Ibáñez", "domicilio": "Calle Verde 90", "telefono": "+5456901234"},
    "55667788": {"nombre": "Fernando", "apellido": "Pacheco", "domicilio": "Calle Amarilla 67", "telefono": "+5489012345"},
    "66778899": {"nombre": "Patricia", "apellido": "Lara", "domicilio": "Plaza Rosa 32", "telefono": "+5423456780"},
    "77889900": {"nombre": "Diego", "apellido": "Serrano", "domicilio": "Avenida Blanca 10", "telefono": "+5434567890"},
    "88990011": {"nombre": "Verónica", "apellido": "Herrera", "domicilio": "Calle Dorada 45", "telefono": "+5445678912"},
    "99001122": {"nombre": "Santiago", "apellido": "Ortiz", "domicilio": "Calle Plata 28", "telefono": "+5456789012"},
    "00112233": {"nombre": "Isabel", "apellido": "Ríos", "domicilio": "Plaza Bronce 19", "telefono": "+5467890123"},
    "11001122": {"nombre": "Andrés", "apellido": "Arias", "domicilio": "Calle Mármol 39", "telefono": "+5478901234"},
    "22002233": {"nombre": "Rosa", "apellido": "Muñoz", "domicilio": "Avenida Piedras 7", "telefono": "+5489012345"},
    "33003344": {"nombre": "José", "apellido": "Peña", "domicilio": "Calle Granito 84", "telefono": "+5490123456"},
    "44004455": {"nombre": "Clara", "apellido": "Roldán", "domicilio": "Avenida Luna 61", "telefono": "+5401234567"},
    "55005566": {"nombre": "Francisco", "apellido": "Cruz", "domicilio": "Calle Sol 49", "telefono": "+5423456789"},
    "66006677": {"nombre": "Teresa", "apellido": "Palacios", "domicilio": "Calle Amanecer 25", "telefono": "+5487654321"},
    "77007788": {"nombre": "Emilio", "apellido": "Cordero", "domicilio": "Plaza del Sol 37", "telefono": "+5445678901"},
    "88008899": {"nombre": "Marta", "apellido": "Reyes", "domicilio": "Avenida Océano 17", "telefono": "+5467890123"},
    "99009900": {"nombre": "Roberto", "apellido": "López", "domicilio": "Calle del Río 73", "telefono": "+5478901234"},
    "10101010": {"nombre": "Paula", "apellido": "Salazar", "domicilio": "Avenida del Valle 6", "telefono": "+5489012345"},
    "12121212": {"nombre": "Héctor", "apellido": "Castro", "domicilio": "Plaza Nueva 85", "telefono": "+5490123456"}
    }
    guardarClientesEnArchivo(clientes)
    
main()
    
