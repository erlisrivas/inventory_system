class Producto:
    def __init__(self, product_id, nombre, descripcion, cantidad, precio):
        self.product_id = product_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def obtener_informacion(self):
        return f"ID: {self.product_id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def modificar_informacion(self, nombre=None, descripcion=None, cantidad=None, precio=None):
        if nombre is not None:
            self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        if cantidad is not None:
            self.cantidad = cantidad
        if precio is not None:
            self.precio = precio


class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto):
        if producto.product_id not in self.inventario:
            self.inventario[producto.product_id] = producto
            print(f"Producto '{producto.nombre}' agregado al inventario.")
        else:
            print("Error: El producto ya existe en el inventario.")

    def eliminar_producto(self, product_id):
        if product_id in self.inventario:
            del self.inventario[product_id]
            print("Producto eliminado del inventario.")
        else:
            print("Error: El producto no existe en el inventario.")

    def actualizar_producto(self, product_id, **kwargs):
        if product_id in self.inventario:
            self.inventario[product_id].modificar_informacion(**kwargs)
            print("Información del producto actualizada.")
        else:
            print("Error: El producto no existe en el inventario.")

    def buscar_producto_por_id(self, product_id):
        if product_id in self.inventario:
            return self.inventario[product_id].obtener_informacion()
        else:
            return "Producto no encontrado."

    def listar_productos(self):
        if not self.inventario:
            return "Inventario vacío."
        informacion_inventario = "\n".join([producto.obtener_informacion() for producto in self.inventario.values()])
        cantidad_total = sum(producto.cantidad for producto in self.inventario.values())
        valor_total = sum(producto.cantidad * producto.precio for producto in self.inventario.values())
        informacion_total = f"\nCantidad total de productos: {cantidad_total}\nValor total del inventario: {valor_total}"

        return informacion_inventario + informacion_total


# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar información del producto")
    print("4. Buscar producto por ID")
    print("5. Listar todos los productos")
    print("6. Salir")


# Programa principal con menú interactivo
inventario = Inventario()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        try:
            product_id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))

            producto = Producto(product_id, nombre, descripcion, cantidad, precio)
            inventario.agregar_producto(producto)
        except ValueError:
            print("Error: Ingrese valores numéricos para ID, cantidad y precio.")

    elif opcion == "2":
        try:
            product_id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(product_id)
        except ValueError:
            print("Error: Ingrese un valor numérico para el ID del producto.")

    elif opcion == "3":
        try:
            product_id = int(input("Ingrese el ID del producto a actualizar: "))
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            cantidad = input("Nueva cantidad: ")
            precio = input("Nuevo precio: ")

            kwargs = {}
            if nombre:
                kwargs['nombre'] = nombre
            if descripcion:
                kwargs['descripcion'] = descripcion
            if cantidad:
                kwargs['cantidad'] = int(cantidad)
            if precio:
                kwargs['precio'] = float(precio)

            inventario.actualizar_producto(product_id, **kwargs)
        except ValueError:
            print("Error: Ingrese valores numéricos para ID, cantidad y precio.")

    elif opcion == "4":
        try:
            product_id = int(input("Ingrese el ID del producto a buscar: "))
            print(inventario.buscar_producto_por_id(product_id))
        except ValueError:
            print("Error: Ingrese un valor numérico para el ID del producto.")
    elif opcion == "5":
        print(inventario.listar_productos())

    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
