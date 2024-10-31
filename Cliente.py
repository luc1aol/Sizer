from Validar import dniValido
from Validar import telValido
def cargarCliente(dicClientes):
    '''
    - Agrega nuevos clientes al sistema, guardando su nombre, apellido y domicilio.
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno:
        Diccionario "dicClientes" con el cliente y sus datos agregados.
    '''
    print("-----------------------------------\n CARGAR CLIENTES \n-----------------------------------")
    while True:
        dni = dniValido("cargar")

        # Verificar si el usuario desea finalizar
        if dni == 0:
            print("Finalizando carga de clientes...")
            break

        if dni in dicClientes:
            print(f"El cliente con DNI: {dni} ya existe. Saltando...")
            continue # Saltar al siguiente ciclo sin solicitar más datos

        nombre = input("Ingrese el nombre del cliente: \n")
        apellido = input("Ingrese el apellido del cliente: \n")
        domicilio = input("Ingrese el domicilio del cliente: \n")
        telefono = telValido("cargar")

        # Guardar los datos en el diccionario (Value,Key)
        dicClientes[dni] = {
            "nombre": nombre.capitalize(),
            "apellido": apellido.capitalize(),
            "domicilio": domicilio,
            "telefono": telefono,
            "pedidos": {} #Esto se inicializa vacío para llenarlo a medida que se hagan pedidos
        }
    return dicClientes
# Comprobamos si el diccionario de clientes está vacío
# Si el diccionario está vacío, mostramos un mensaje indicando que no hay clientes registrados
# Si el diccionario no está vacío, recorremos cada cliente en el diccionario

def listarClientes(dicClientes):
    '''
    - Imprime una lista de los clientes con sus datos (DNI, nombre completo, domicilio y telefono).
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno: --
    '''
    print("-----------------------------------\n LISTADO CLIENTES\n-----------------------------------")
    if not dicClientes:
        print("No se encuentran clientes registrados.")
    else:
        for dni, detalles in dicClientes.items():
            print(f"DNI: {dni}, Nombre: {detalles['nombre']}, Apellido: {detalles['apellido']}, Domicilio: {detalles['domicilio']}, Teléfono: {detalles['telefono']}")
    return
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
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
    return 
def eliminarCliente(dicClientes):
    '''
    - Elimina un cliente del sistema.
    - Parámetros: 
        Diccionario "dicClientes"
    -Retorno:
        Diccionario "dicClientes" con el cliente seleccionado eliminado.
    '''
    print("-----------------------------------\n ELIMINAR CLIENTE\n-----------------------------------")
    dni = dniValido("darle de baja")

    # Verificar si el DNI está en el diccionario
    if dni in dicClientes:  
        del dicClientes[dni]  # Eliminar el cliente
        print(f"Cliente con DNI {dni} eliminado.")
    else:
        print(f"No se encontró un cliente con el DNI {dni}.")
    return
