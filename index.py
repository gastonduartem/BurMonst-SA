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

# Función para calcular el presupuesto
def calcular_presupuesto(insumos, cantidades):
    presupuesto_total = 0
    for insumo, cantidad in cantidades.items():
        if insumo in insumos:
            precio_unitario = insumos[insumo]
            costo_total = precio_unitario * cantidad
            presupuesto_total += costo_total
            print(f"{insumo}: {cantidad} x ${precio_unitario} = ${costo_total}")
    return presupuesto_total

# Función para verificar si el cliente es nuevo
def verificar_cliente(ruc_cliente):
    if ruc_cliente in clientes:
        return False
    else:
        return True

# Función principal
def main():
    while True:
        global contador_tickets  # Acceder a la variable global contador_tickets
        print("Bienvenido al sistema de presupuestos de insumos informáticos.")
        ruc_cliente = input("Ingrese el RUC del cliente: ")

        if verificar_cliente(ruc_cliente):
            nombre_cliente = input("Cliente nuevo. Ingrese el nombre del cliente: ")
            nuevo_ruc = input("Ingrese el número de RUC del cliente: ")
            clientes[nuevo_ruc] = nombre_cliente
        else:
            nombre_cliente = clientes[ruc_cliente]
            print(f"Cliente existente: {nombre_cliente} - RUC: {ruc_cliente}")

        cantidades = {}
        while True:
            insumo = input("Ingrese el nombre del insumo (o 'salir' para terminar): ").capitalize()
            if insumo == 'Salir':
                break
            if insumo in insumos_informaticos:
                cantidad = int(input(f"Ingrese la cantidad de {insumo}: "))
                cantidades[insumo] = cantidad
            else:
                print("Insumo no válido. Por favor, elija otro insumo.")

        presupuesto = calcular_presupuesto(insumos_informaticos, cantidades)
        print(f"Presupuesto total: ${presupuesto}")

        print(f"Cliente: {nombre_cliente} - RUC: {ruc_cliente}")
        print("Compra:")
        for insumo, cantidad in cantidades.items():
            print(f"{insumo}: {cantidad} unidades")

        # Generar e imprimir el número de ticket
        numero_ticket = f"{contador_tickets:03d}"
        print(f"Número de Ticket: {numero_ticket}")

        entrega = None

        while entrega not in ["entrega", "local"]:
            entrega = input("¿Desea entrega a domicilio (costo adicional de 10 Dolares) o retirar en el local? (Entrega/Local): ").strip().lower()

        if entrega == 'entrega':
            ubicacion = input("Ingrese su ubicación: ")
            numero_casa = input("Ingrese su número de casa: ")
            costo_entrega = 10
            presupuesto_total = presupuesto + costo_entrega
            print(f"Costo de entrega: ${costo_entrega}")
            print(f"La entrega se realizará en la ubicación: {ubicacion}.")
            print(f"Presupuesto total con entrega: ${presupuesto_total}")
            confirmacion = input("¿Desea confirmar la compra? (Sí/No): ").strip().lower()
            if confirmacion == 'si':
                print("La compra se ha realizado con éxito. Puede realizar el pago a través de los métodos de pago disponibles en nuestro sitio web presentando el ticket.")
                contador_tickets += 1  # Incrementar el contador de tickets
            else:
                print("La compra ha sido cancelada. Gracias por visitarnos. ¡Vuelva pronto!")
        elif entrega == 'local':
            print("Gracias por su compra. Lo esperamos en nuestro local. La ubicación está detallada en la página web.")
        else:
            print("Opción no válida. La compra se registrará para retiro en el local.")

        solicitar_otro_presupuesto = input("¿Desea solicitar otro presupuesto? (Sí/No): ").strip().lower()
        if solicitar_otro_presupuesto != 'si':
            print("Gracias por utilizar nuestro sistema de presupuestos.")
            break

if __name__ == "__main__":
    main()


