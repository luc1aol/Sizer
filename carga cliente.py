def cargarCliente():
     clientes = {}
     while True:
        dni = input("Ingrese el DNI del cliente (o 0 para terminar): ")
        if dni == '0':  # Si el DNI es '0', termina el proceso de carga
            break
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        domicilio = input("Ingrese el domicilio del cliente: ")
        
        # Guardar los datos en el diccionario
        clientes[dni] = [nombre, apellido, domicilio]
     return clientes
def  imprimirDiccionario(clientes):
    print(clientes)
def main():
    clientes=cargarCliente()
    imprimirDiccionario(clientes)
    
main() 