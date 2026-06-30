"""
Módulo: main.py
Punto de arranque del programa. Aquí se crean los objetos
(productos, clientes, restaurante), se agregan al servicio
principal y se muestra la información registrada en consola.
"""

# Importación de las clases necesarias desde sus respectivos paquetes.
# Gracias a las importaciones definidas en los __init__.py de cada
# paquete, se pueden importar directamente así (sin indicar el módulo).
from modelos import Producto, Cliente
from servicios import Restaurante


def main() -> None:
    # 1. Creamos el objeto Restaurante, que actuará como servicio principal
    restaurante_actual: Restaurante = Restaurante("El Buen Sabor")

    # 2. Creamos varios objetos Producto, aplicando tipos de datos básicos:
    #    str (nombre, categoria), float (precio), bool (disponibilidad)
    producto_ceviche: Producto = Producto("Ceviche de camarón", "Plato fuerte", 8.50, True)
    producto_seco_pollo: Producto = Producto("Seco de pollo", "Plato fuerte", 6.00, True)
    producto_jugo_naranja: Producto = Producto("Jugo de naranja", "Bebida", 2.00, True)
    producto_flan: Producto = Producto("Flan de caramelo", "Postre", 2.50, False)

    # 3. Agregamos los productos a la lista administrada por el servicio principal
    restaurante_actual.agregar_producto(producto_ceviche)
    restaurante_actual.agregar_producto(producto_seco_pollo)
    restaurante_actual.agregar_producto(producto_jugo_naranja)
    restaurante_actual.agregar_producto(producto_flan)

    # 4. Mostramos el menú completo del restaurante
    restaurante_actual.mostrar_menu()

    # 5. Creamos objetos Cliente, aplicando tipos de datos básicos:
    #    str (nombre, cedula), int (visitas), bool (cliente frecuente)
    cliente_maria: Cliente = Cliente("María Pérez", "0102030405", 6, True)
    cliente_juan: Cliente = Cliente("Juan Torres", "0607080910", 2, False)

    # 6. Registramos los clientes en la lista administrada por el servicio principal
    restaurante_actual.registrar_cliente(cliente_maria)
    restaurante_actual.registrar_cliente(cliente_juan)

    # 7. Realizamos pedidos: asociamos productos del menú a cada cliente
    restaurante_actual.realizar_pedido(cliente_maria, producto_ceviche)
    restaurante_actual.realizar_pedido(cliente_maria, producto_jugo_naranja)
    restaurante_actual.realizar_pedido(cliente_juan, producto_seco_pollo)

    # Intento de pedir un producto no disponible (debe fallar de forma controlada)
    pedido_realizado: bool = restaurante_actual.realizar_pedido(cliente_juan, producto_flan)
    if not pedido_realizado:
        print(f"\nAviso: el producto '{producto_flan.nombre_producto}' no está disponible actualmente.")

    # 8. Registramos una visita adicional para un cliente, usando el método correspondiente
    cliente_juan.registrar_visita()

    # 9. Mostramos la información de los clientes registrados
    restaurante_actual.mostrar_clientes()

    # 10. Mostramos la información general del restaurante usando __str__
    print(f"\n--- Resumen general ---\n{restaurante_actual}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
