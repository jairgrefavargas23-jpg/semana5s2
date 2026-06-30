# Tarea Semana 5 — Aplicación de identificadores y tipos de datos en un proyecto Python modular

**Estudiante:** Bryan Jair Grefa Alvarado

## Descripción del sistema

Este proyecto implementa un **sistema básico de gestión de restaurante** utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar productos del menú, registrar clientes, asociar pedidos a cada cliente, registrar visitas y calcular el total a pagar, mostrando toda la información organizada en consola.

El proyecto no busca ser una aplicación compleja ni un menú interactivo, sino **demostrar el uso correcto de identificadores descriptivos, convenciones de nombres de Python, tipos de datos básicos y listas como tipo de dato compuesto**, dentro de un proyecto organizado de forma modular.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py      -> Expone Producto y Cliente para importarlos desde el paquete
│   ├── producto.py      -> Clase Producto (representa un plato, bebida o producto del menú)
│   └── cliente.py       -> Clase Cliente (representa a una persona registrada en el sistema)
├── servicios/
│   ├── __init__.py      -> Expone Restaurante para importarla desde el paquete
│   └── restaurante.py   -> Clase Restaurante (administra listas de productos y clientes)
└── main.py               -> Punto de arranque del programa
README.md
```

### Explicación de cada módulo

- **modelos/__init__.py**: archivo que convierte a `modelos` en un paquete de Python; importa y expone las clases `Producto` y `Cliente` para que puedan usarse directamente como `from modelos import Producto, Cliente`.
- **modelos/producto.py**: define la clase `Producto`, con atributos `nombre_producto` (str), `categoria` (str), `precio_unitario` (float) y `esta_disponible` (bool). Incluye métodos para cambiar disponibilidad, aplicar descuentos y representar el objeto como texto mediante `__str__`.
- **modelos/cliente.py**: define la clase `Cliente`, con atributos `nombre_completo` (str), `numero_cedula` (str), `visitas_realizadas` (int), `es_cliente_frecuente` (bool) y `lista_pedidos` (list, tipo de dato compuesto que almacena objetos `Producto`). Incluye métodos para agregar pedidos, registrar visitas y calcular el total del pedido.
- **servicios/__init__.py**: archivo que convierte a `servicios` en un paquete de Python; importa y expone la clase `Restaurante` para que pueda usarse directamente como `from servicios import Restaurante`.
- **servicios/restaurante.py**: define la clase `Restaurante`, que administra `lista_productos` y `lista_clientes` (ambas listas, tipo de dato compuesto). Coordina la lógica de negocio: agregar productos, registrar clientes, realizar pedidos y mostrar la información en consola. Importa las clases `Producto` y `Cliente` desde el paquete `modelos`.
- **main.py**: punto de arranque del programa. Crea objetos `Producto` y `Cliente`, los agrega al servicio principal (`Restaurante`) y ejecuta los métodos necesarios para demostrar el funcionamiento completo del sistema.

## Identificadores y convenciones de nombres aplicadas

- **PascalCase** para las clases: `Producto`, `Cliente`, `Restaurante`.
- **snake_case** para variables, atributos, métodos y archivos: `nombre_producto`, `precio_unitario`, `lista_pedidos`, `agregar_pedido()`, `producto.py`, `cliente.py`, `restaurante.py`.
- Identificadores **descriptivos**, evitando nombres genéricos como `x`, `dato` u `objeto`; por ejemplo, en lugar de `c` se usa `cliente_maria`, y en lugar de `lista` se usa `lista_pedidos`.

## Tipos de datos básicos utilizados

| Tipo de dato | Atributo / uso |
|---|---|
| `str` | `nombre_producto`, `categoria`, `nombre_completo`, `numero_cedula`, `nombre_restaurante` |
| `int` | `visitas_realizadas` |
| `float` | `precio_unitario`, total calculado en `calcular_total_pedido()` |
| `bool` | `esta_disponible`, `es_cliente_frecuente` |
| `list` | `lista_pedidos` (en `Cliente`), `lista_productos` y `lista_clientes` (en `Restaurante`) — tipo de dato compuesto usado para almacenar múltiples objetos |

## Cómo ejecutar el proyecto

Desde la raíz del repositorio, entrar a la carpeta `restaurante_app` y ejecutar `main.py`:

```bash
cd restaurante_app
python main.py
```

## Reflexión sobre identificadores, tipos de datos y listas

Usar identificadores descriptivos y respetar las convenciones de nombres de Python (PascalCase para clases, snake_case para variables, métodos y archivos) hace que el código sea mucho más legible y fácil de entender, tanto para quien lo escribe como para cualquier otra persona que lo revise después. De igual manera, elegir el tipo de dato adecuado para cada atributo (str para texto, int para cantidades enteras, float para valores monetarios y bool para estados lógicos) evita errores de interpretación y permite que el programa se comporte de forma predecible. Finalmente, el uso de listas como tipo de dato compuesto es fundamental en un sistema como este, ya que permite manejar colecciones completas de objetos (productos, clientes, pedidos) sin necesidad de crear una variable individual por cada uno, lo que hace que el sistema sea escalable y mucho más fácil de mantener a futuro.
