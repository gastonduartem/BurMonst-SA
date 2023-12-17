import numpy as np
import matplotlib.pyplot as plt
import os
# Clase Producto que representa un producto en el catálogo
class Producto:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.sales = np.random.randint(50, 300)  # Generar ventas aleatorias al inicio

    def aumentar_ventas(self, cantidad):
        self.sales += cantidad

# Clase CarroDeCompras para gestionar los productos en el carrito
class CarroDeCompras:
    def __init__(self):
        # Catálogo de productos predefinidos
        self.catalogo = {
            1: Producto(1, "Laptop", 800),
            2: Producto(2, "Monitor", 200),
            3: Producto(3, "Teclado", 30),
            4: Producto(4, "Ratón", 20),
            5: Producto(5, "Impresora", 150)
        }
        self.cart_items = {}  # Productos agregados al carrito

    # Mostrar los productos en el carrito
    def mostrar_carrito(self):
        if not self.cart_items:
            print("El carrito está vacío.")
        else:
            print("Contenido del carrito:")
            for product_id, quantity in self.cart_items.items():
                producto = self.catalogo[product_id]
                print(f"Producto: {producto.name} - Cantidad: {quantity}")

    # Agregar un producto al carrito
    def agregar_item(self, product_id, quantity):
        try:
            producto = self.catalogo[product_id]
            producto_existente = self.cart_items.get(product_id, 0)
            self.cart_items[product_id] = producto_existente + quantity
            ventas_simuladas = np.random.randint(0, 10, size=quantity)
            producto.aumentar_ventas(sum(ventas_simuladas))
        except KeyError:
            raise ProductoNoEncontrado("Producto no encontrado en el catálogo.")
        
          # Eliminar un producto del carrito
    def eliminar_item(self, producto_a_eliminar):
        eliminado = False
        for product_id, producto in self.catalogo.items():
            if producto.name.lower() == producto_a_eliminar.lower() and product_id in self.cart_items:
                del self.cart_items[product_id]
                eliminado = True
                print("Producto eliminado del carrito.")
                break

    # Clase de excepción para producto no encontrado
    class ProductoNoEncontrado(Exception):
     pass
# Realizar la compra y mostrar detalles
    def realizar_compra(self, ruc_cliente, nombre_cliente):
        # Detalles de la compra
        total_cost = 0
        print("Detalles de la compra:")
        for product_id, quantity in self.cart_items.items():
            producto = self.catalogo[product_id]
            costo_total_producto = producto.price * quantity
            total_cost += costo_total_producto
            print(f"Producto: {producto.name} - Cantidad: {quantity} - Costo total: ${costo_total_producto}")
            
 # Mostrar detalles del cliente y costo total
        print(f"Costo total de la compra: ${total_cost}")
        print(f"RUC del cliente: {ruc_cliente}")
        print(f"Nombre del cliente: {nombre_cliente}")
        print("¡Gracias por tu compra!")
        
# Gráfico de productos más vendidos
        productos = [producto.name for producto in self.catalogo.values()]
        ventas = [producto.sales for producto in self.catalogo.values()]
        total_sales = sum(ventas)
        porcentajes = [100 * venta / total_sales for venta in ventas]

        plt.figure(figsize=(8, 6))
        plt.barh(productos, ventas, color='lightblue')
        plt.xlabel('Cantidad vendida')
        plt.ylabel('Productos')
        plt.title('Productos más vendidos de la semana')
        plt.tight_layout()

        # Mostrar porcentajes en el gráfico
        for i, porcentaje in enumerate(porcentajes):
            plt.text(ventas[i] + 5, i, f'{porcentaje:.1f}%', va='center')

        plt.show()
# Función principal para ejecutar el programa
def main():
    # Datos predefinidos de clientes
    datos_clientes = {
        "123456": "Jorge Perez",
        "12345": "Claudia Portillo"
    }
    #Implementacion de registro de usuario
    ruc_cliente = input("Ingrese su RUC: ")
    nombre_cliente = datos_clientes.get(ruc_cliente)
    if nombre_cliente:
        print(f"Bienvenido, {nombre_cliente}!")
    else:
        print("Cliente no registrado.")
        nuevo_cliente = input("Ingrese su nombre para registrarse como nuevo cliente: ")
        datos_clientes[ruc_cliente] = nuevo_cliente
        print("Registro completado.")
        
    carrito = CarroDeCompras()  # Crear un nuevo carrito

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

        # Mostrar productos disponibles
        print("\nBurMont S.A")
        print("\nInsumos Informáticos")
        print("\nProductos disponibles:")
        for product_id, producto in carrito.catalogo.items():
            print(f"{product_id}. {producto.name} - ${producto.price}")

        if carrito.cart_items:
            print(f"Tienes {sum(carrito.cart_items.values())} en el carrito")

        # Opciones para agregar, ver o eliminar productos, o finalizar la compra
        opcion = input("Selecciona un producto (1-5) para agregar al carrito, 6 para ver el carrito, 7 para eliminar un producto del carrito, o 8 para finalizar la compra y ver el gráfico de productos más vendidos: ")

        if opcion in ["1", "2", "3", "4", "5"]:
            cantidad = int(input(f"Ingrese la cantidad del producto seleccionado ({opcion}): "))
            try:
                carrito.agregar_item(int(opcion), cantidad)
            except ProductoNoEncontrado as e:
                print(e)
        elif opcion == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            carrito.mostrar_carrito()
            input("Presiona Enter para continuar...")
        elif opcion == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            carrito.mostrar_carrito()
            producto_a_eliminar = input("Escribe el nombre del producto que deseas eliminar del carrito: ")
            carrito.eliminar_item(producto_a_eliminar)
            input("Presiona Enter para continuar.")
        elif opcion == "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            carrito.realizar_compra(ruc_cliente, nombre_cliente)
            break
        else:
            print("Opción inválida. Selecciona un número del 1 al 8.")
# Ejecutar la función principal al iniciar el programa
if __name__ == "__main__":
    main()


