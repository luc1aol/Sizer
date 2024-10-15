def listarProductos(productos):
    if productos:
        print("\nListado de productos:")
        print("-----------------------------")
        for nombre, detalles in productos.items():
            print(f"Producto: {nombre}")
            print(f"  Precio: ${detalles['precio']}")
            print(f"  Stock: {detalles['stock']} unidades")
            print("-----------------------------")
    else:
        print("No hay productos disponibles.")
    return