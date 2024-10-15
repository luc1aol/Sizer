from crearCliente import cargarClientes
from listarClientes import listarClientes
from actualizarCliente import actualizarCliente
from eliminarCliente import eliminarCliente
from actualizarStock import actualizarProducto
from listarProductos import listarProductos
from agregarProducto import nuevoProducto

def main():
    clientes={}
    productos = {
    'chomba': {'precio': 1500.0, 'stock': 100},
    'remera': {'precio': 1200.0, 'stock': 200},
    'pantalon': {'precio': 2500.0, 'stock': 150}}
    while True:
            opciones = 4
            while True:
                print()
                print("---------------------------")
                print("MENÚ DEL SISTEMA           ")
                print("---------------------------")
                print("[1] Gestión de clientes")
                print("[2] Gestion de pedido")
                print("[3] Gestion de productos")
                print("---------------------------")
                print("[0] Salir del programa")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0": # Opción salir del programa
                exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

            elif opcion == "1":   # Opción 1
                clientes:{}
                while True:
                    opciones = 5
                    while True:
                        print()
                        print("---------------------------")
                        print("MENÚ DE CLIENTES           ")
                        print("---------------------------")
                        print("[1] Cargar Cliente")
                        print("[2] Listar clientes ")
                        print("[3] Actualizar datos del cliente")
                        print("[4] Dar de baja al cliente")
                        print("---------------------------")
                        print("[0] VOLVER AL MENÚ ANTERIOR")
                        print()
                        
                        opcion = input("Seleccione una opción: ")
                        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                            break
                        else:
                            input("Opción inválida. Presione ENTER para volver a seleccionar.")
                    print()

                    if opcion == "0": # Opción salir del programa
                        break # No salimos del programa, volvemos al menú anterior
                    elif opcion == "1":   # Opción 1
                        cargarClientes(clientes)
                    elif opcion == "2":   # Opción 2
                        listarClientes(clientes)
                    elif opcion == "3":   # Opción 3
                        actualizarCliente(clientes)
                    elif opcion == "4":   # Opción 4
                        eliminarCliente(clientes)

            #elif opcion == "2":   # Opción 2
            #    while True:
            #        opciones = 5
            #        while True:
            #            print("MENÚ DE PEDIDOS          ")
            #            print("---------------------------")
            #            print("[1] Seleccion de producto")
            #            print("[2] Seleccion de cantidad")
            #            print("[4] seleccion de cliente")
            #            print("---------------------------")
            #            print("[0] VOLVER AL MENÚ ANTERIOR")
            #            print()
             #           elif opcion=="1":
            elif opcion=="3":
                while True:
                    opciones = 4
                    while True:
                        print()
                        print("---------------------------")
                        print("MENÚ DE PRODUCTOS           ")
                        print("---------------------------")
                        print("[1] Listar productos")
                        print("[2] Actualizar stock y precio")
                        print("[3] Agregar nuevo producto")
                        print("---------------------------")
                        print("[0] VOLVER AL MENÚ ANTERIOR")
                        print()
                        opcion = input("Seleccione una opción: ")
                        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                            break
                        else:
                            input("Opción inválida. Presione ENTER para volver a seleccionar.")
                    print()
                    if opcion=="0":
                        break
                    elif opcion=="1":
                        listarProductos(productos)
                    elif opcion=="2":
                        actualizarProducto(productos)
                        print(productos)
                    elif opcion == "3":
                        nuevoProducto(productos)
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")
main()