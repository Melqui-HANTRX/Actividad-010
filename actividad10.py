inventario = {}

producto = {}

cantidad = int(input("Ingrese la cantidad que desea: "))

for i in range(cantidad):
    codigo = input("Ingrese el codigo del producto: ")
    while codigo in producto:
        print("El producto ingresado ya existe")
        codigo = input("Ingrese el codigo del producto: ")

    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese el categoria del producto: ")
    talla = input("Ingrese el talla del producto: ")

    precio = float(input("Ingrese el precio del producto: "))

    while precio <= 0:
        print("El precio ingresado debe ser mayor a 0")
        precio = float(input("Ingrese el precio del producto: "))

    stock = input("Ingrese el stock del producto: ")
    while stock <= 0:
        print("El stock ingresado debe ser mayor a 0")
        stock = float(input("Ingrese el stock del producto: "))
    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
    }
    if categoria in producto:

