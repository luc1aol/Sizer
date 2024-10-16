from CargarClientes import cargarCliente
from ActualizarCliente import actualizarCliente
from EliminarCliente import eliminarCliente
from ListarClientes import listarClientes

from GenerarPedido import generarPedido
from ListarPedidos import listarPedidos
from CancelarPedidos import cancelarPedido

def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    dicClientes = {}
    dicProductos = {}
    idPedidoActual = 10

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 3
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Gestión de Clientes")
            print("[2] Gestion de Pedidos")
            print("[3] Gestion de Productos")
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
            exit() 

        elif opcion == "1":   # Opción 1
            while True:
                opciones = 4
                while True:
                    print()
                    print("---------------------------")
                    print("MENÚ DE CLIENTES           ")
                    print("---------------------------")
                    print("[1] Cargar Clientes")
                    print("[2] Listar Clientes")
                    print("[3] Actualizar Cliente")
                    print("[4] Eliminar Cliente")
                    print("---------------------------")
                    print("[0] VOLVER AL MENÚ ANTERIOR")
                    print()
                    
                    op = input("Seleccione una opción: ")
                    if op in [str(i) for i in range(0, opciones)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if op == "0": # Opción salir del programa
                    break # No salimos del programa, volvemos al menú anterior
                elif op == "1":   # Opción 1
                    cargarCliente(dicClientes)
                elif op == "2":   # Opción 2
                    listarClientes(dicClientes)
                elif op == "3":   # Opción 3
                    actualizarCliente(dicClientes)
                elif op == "4":   # Opción 4
                    eliminarCliente(dicClientes)

        elif opcion == "2":
            while True:
                opciones = 4
                while True:
                    print("---------------------------")
                    print("MENÚ DE PEDIDOS          ")
                    print("---------------------------")
                    print("[1] Crear Nuevo Pedido")
                    print("[2] Listar Pedidos Activos")
                    print("[3] Cancelar Pedidos")
                    print("[4] Historial de Pedidos por Cliente")
                    print("[5] Reportes de Pedidos")
                    print("---------------------------")
                    print("[0] VOLVER AL MENÚ ANTERIOR")
                    print()

                    op = input("Seleccione una opción: ")
                    if op in [str(i) for i in range(0, opciones)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                if op=="0":
                    break
                elif op=="1":
                    generarPedido(dicClientes,dicProductos,idPedidoActual)
                elif op=="2":
                    listarPedidos(dicClientes)
                elif op=="3":
                    cancelarPedido(dicClientes)
                elif op=="4":
                    # Muestra el historial de pedidos para un cliente específico.
                    ...
                elif op=="5":
                    # Genera un reporte general de los pedidos (cantidad, estatus, etc.).
                    ...

        elif opcion == "3":
            while True:
                opciones = 4
                while True:
                    print()
                    print("---------------------------")
                    print("MENÚ DE PRODUCTOS           ")
                    print("---------------------------")
                    print("[1] Listar Productos")
                    print("[2] Añadir Productos")
                    print("[3] Actualizar Stock y Precios")
                    print("[4] Eliminar Producto")
                    print("---------------------------")
                    print("[0] VOLVER AL MENÚ ANTERIOR")
                    print()
                    op = input("Seleccione una opción: ")
                    if op in [str(i) for i in range(0, opciones)]:
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()
                if op=="0":
                    break
                elif op=="1":
                    # Listar los productos
                    ...
                elif op=="2":
                    # Añadir productos nuevos al inventario
                    ...
                elif op == "3":
                    # Actualizar el stock
                    ...
                elif op == "3":
                    # Eliminar un producto
                    ...


        input("\nPresione ENTER para volver al menú.")
        print("\n\n")
main()