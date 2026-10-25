productos = []
cantidades = []


def buscar_producto(nombre):
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    if buscar_producto(nombre) != -1:
        print("Ese producto ya esta registrado.")
        return

    cantidad = int(input("Cantidad disponible: "))

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return

    productos.append(nombre)
    cantidades.append(cantidad)

    print("Producto registrado correctamente.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        print("\n--- INVENTARIO ---")

        for i in range(len(productos)):
            print(i + 1, ".", productos[i],
                  "- Cantidad:", cantidades[i])


def consultar_producto():
    nombre = input("Nombre del producto que busca: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        print("Producto:", productos[posicion])
        print("Cantidad disponible:", cantidades[posicion])
    else:
        print("El producto no existe en el inventario.")


def modificar_cantidad():
    nombre = input("Producto que desea modificar: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        nueva_cantidad = int(input("Nueva cantidad: "))

        if nueva_cantidad >= 0:
            cantidades[posicion] = nueva_cantidad
            print("Cantidad modificada correctamente.")
        else:
            print("La cantidad no puede ser negativa.")
    else:
        print("No se puede modificar. Producto no encontrado.")


def eliminar_producto():
    nombre = input("Producto que desea eliminar: ").strip()
    posicion = buscar_producto(nombre)

    if posicion != -1:
        productos.pop(posicion)
        cantidades.pop(posicion)
        print("Producto eliminado correctamente.")
    else:
        print("No se puede eliminar. Producto no encontrado.")


def contar_productos():
    print("Productos diferentes registrados:", len(productos))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else:
        posicion_mayor = 0

        for i in range(1, len(cantidades)):
            if cantidades[i] > cantidades[posicion_mayor]:
                posicion_mayor = i

        print("Producto con mayor cantidad:",
              productos[posicion_mayor])
        print("Cantidad disponible:",
              cantidades[posicion_mayor])


def menu():
    while True:
        print("\n========== GESTOR DE INVENTARIO ==========")
        print("1. Registrar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar cantidad")
        print("5. Eliminar producto")
        print("6. Contar productos")
        print("7. Mostrar producto con mayor cantidad")
        print("8. Salir")
        print("==========================================")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            consultar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            contar_productos()
        elif opcion == "7":
            mostrar_mayor_cantidad()
        elif opcion == "8":
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


menu()
