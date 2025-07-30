inventario = {}
producto = {}

cantidad = int(input("Ingrese la cantidad que desea: "))

for i in range(cantidad):
    codigo = input("Ingrese el codigo del producto: ")
    while codigo in inventario:
        print("El producto ingresado ya existe")
        codigo = input("Ingrese el codigo del producto: ")

    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    talla = input("Ingrese la talla del producto: ")

    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        print("El precio ingresado debe ser mayor a 0")
        precio = float(input("Ingrese el precio del producto: "))

    stock = int(input("Ingrese el stock del producto: "))
    while stock <= 0:
        print("El stock ingresado debe ser mayor a Q,0.0")
        stock = int(input("Ingrese el stock del producto: "))

    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "talla": talla,
        "precio": precio,
        "stock": stock
    }

    if categoria in producto:
        producto[categoria] += 1
    else:
        producto[categoria] = 1

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Ver lista de productos")
    print("2. Buscar producto por código")
    print("3. Ver valor total del inventario")
    print("4. Ver cantidad por categoría")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            print("---Lista de productos---")
            for codigos1, datos in inventario.items():
                print(f"\nCódigo: {codigos1}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Categoría: {datos['categoria']}")
                print(f"Talla: {datos['talla']}")
                print(f"Precio: Q{datos['precio']:.2f}")
                print(f"Stock: {datos['stock']}")

        case "2":
            buscar = input("Ingrese el codigo a buscar: ")
            if buscar in inventario:
                produto = inventario[buscar]
                print(f"\nProducto entontrado: ")
                print(f"Nombre: {produto['nombre']}")
                print(f"Categoria: {produto['categoria']}")
                print(f"Talla: {produto['talla']}")
                print(f"Precio: Q{produto['precio']:.2f}")
                print(f"Stock: {produto['stock']}")
            else:
                print("No se encontro el producto")

        case "3":
            totalprecio = 0
            for datos in inventario.values():
                totalprecio += datos['precio'] * datos['stock']
            print(f"Total precio: {totalprecio:.2f}")

        case "4":
            print("\nCantidad de productos por categoria: ")
            for cantidad1, cant in producto.items():
                print(f"\n{cantidad1}: {cant} producto(s)")

        case "5":
            print("\nSaliendo...")
            break

        case _:
            print("Opción inválida.")
