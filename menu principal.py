def main():
    while True:
            opciones = 3
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
                while True:
                    opciones = 4
                    while True:
                        print()
                        print("---------------------------")
                        print("MENÚ DE CLIENTES           ")
                        print("---------------------------")
                        print("[1] Cargar Cliente")
                        print("[4] Listar clientes ")
                        print("[2] Actualizar datos del cliente")
                        print("[3] Dar de baja al cliente")
                        print("[4]")
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
                        
                    elif opcion == "2":   # Opción 2
                        ...
                    elif opcion == "3":   # Opción 3
                        ...
                    elif opcion == "4":   # Opción 4
                        ...

            elif opcion == "2":   # Opción 2
                while True:
                    opciones = 5
                    while True:
                        print()
                        print("---------------------------")
                        print("MENÚ DE PEDIDOS          ")
                        print("---------------------------")
                        print("[1] Seleccion de producto")
                        print("[2] Seleccion de cantidad")
                        print("[3] Confirmar perdido")
                        print("[4] Seleccion de cliente")
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
            elif opcion == "3":   # Opción 3
                while True:
                    opciones = 3
                    while True:
                        print()
                        print("---------------------------")
                        print("MENÚ DE PRODUCTOS           ")
                        print("---------------------------")
                        print("[1] listar productos con sus descripciones")
                        print("[2] Actualizar stock y precio")
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

            input("\nPresione ENTER para volver al menú.")
            print("\n\n")
