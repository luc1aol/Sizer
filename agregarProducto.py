from actualizarStock import actualizarProducto

def nuevoProducto(productos):
    while True:
        productoNuevo = input("Ingrse el nombre del nuevo producto ('0' para volver): ")
        if productoNuevo == "0":
            print("Volviendo al menu principal")
            break
        else:
            if productoNuevo not in productos:
                productos[productoNuevo] = {"precio":None, "stock":None}
                precio = float(input("Ingrese el precio del nuevo producto: "))
                stock = int(input("Ingrese la cantidad de stock ingresado: "))
                productos[productoNuevo]["precio"] = precio
                productos[productoNuevo]["stock"] = stock
                print("Producto agregado correctamente.")
                print("\n")
            else:
                print("El producto ya se encuentra en el sistema.")
                print("\n")
                actualizar = input("Para actualizar precio o stock apriete '1', para agregar otro producto apriete otra tecla: ")
                if actualizar == "1":
                    actualizarProducto(productos)
                else:
                    productoNuevo = input("Ingrese el nombre de otro producto o '0' para regresar al menu: ")
                    if productoNuevo == "0":
                        break
    return productos
