"""
Módulo: restaurante.py
Contiene la clase Restaurante, encargada de administrar las listas
de productos y clientes registrados en el sistema.
"""

# Importación de las clases definidas en el paquete modelos.
# Esto demuestra la comunicación entre archivos mediante importaciones.
from modelos import Producto, Cliente


class Restaurante:
    """
    Clase de servicio que administra las operaciones principales del
    sistema: registro de productos, registro de clientes y gestión
    de pedidos, utilizando listas como tipo de dato compuesto.

    Atributos:
        nombre_restaurante (str): Nombre del restaurante.
        lista_productos (list): Lista de objetos Producto disponibles en el menú.
        lista_clientes (list): Lista de objetos Cliente registrados en el sistema.
    """

    def __init__(self, nombre_restaurante: str):
        # Constructor: inicializa el nombre del restaurante y las listas vacías
        self.nombre_restaurante: str = nombre_restaurante
        self.lista_productos: list = []  # Lista (tipo de dato compuesto) de objetos Producto
        self.lista_clientes: list = []   # Lista (tipo de dato compuesto) de objetos Cliente

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto a la lista del menú del restaurante."""
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un nuevo cliente en la lista de clientes del sistema."""
        self.lista_clientes.append(cliente)

    def realizar_pedido(self, cliente: Cliente, producto: Producto) -> bool:
        """
        Permite que un cliente registrado realice un pedido de un
        producto disponible en el menú. Retorna True si el pedido
        se realizó con éxito, False en caso contrario.
        """
        pedido_exitoso: bool = producto in self.lista_productos and producto.esta_disponible
        if pedido_exitoso:
            cliente.agregar_pedido(producto)
        return pedido_exitoso

    def contar_productos_disponibles(self) -> int:
        """Cuenta cuántos productos del menú están actualmente disponibles."""
        cantidad_disponibles: int = sum(1 for producto in self.lista_productos if producto.esta_disponible)
        return cantidad_disponibles

    def mostrar_menu(self) -> None:
        """Muestra en consola todos los productos registrados en el menú."""
        print(f"\n--- Menú de {self.nombre_restaurante} ---")
        if not self.lista_productos:
            print("El menú aún no tiene productos registrados.")
        for producto in self.lista_productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        """Muestra en consola la información de todos los clientes registrados."""
        print(f"\n--- Clientes registrados en {self.nombre_restaurante} ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        for cliente in self.lista_clientes:
            print(cliente)

    def __str__(self) -> str:
        # Representación legible del restaurante como texto
        return (f"Restaurante: {self.nombre_restaurante} | "
                f"Productos en menú: {len(self.lista_productos)} "
                f"(disponibles: {self.contar_productos_disponibles()}) | "
                f"Clientes registrados: {len(self.lista_clientes)}")
