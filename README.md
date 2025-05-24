# Progra_3r_semestre_1er_parcial
# Sistema de Gestión de Inventario para una PyME

## Grupo 4
Proyecto desarrollado por:
- Gomez Mendoza Zury Luisiana
- Santillan Troya Jose Joel
- Navarrete Camba Jordy Josue
- Ramirez Quinde Luis Enrique
- Pinto Mejia Rebeca Sarai

---

## Descripción del Proyecto

Sistema de Gestión de Inventario para una PyME es una aplicación que permite controlar eficientemente el inventario de una pequeña o mediana empresa.

El sistema facilita la administración de productos (clasificados en perecibles y no perecibles), la gestión de proveedores y el seguimiento del stock. También incorpora una simulación del paso del tiempo que afecta el estado de los productos perecibles, permitiendo identificar cuándo caducan.

Desarrollado con principios de Programación Orientada a Objetos (POO) como herencia, encapsulamiento y polimorfismo, el sistema proporciona una estructura modular y reutilizable, ideal para ampliar sus funcionalidades en el futuro.


Incluye funcionalidades como:
- Registro y eliminación de productos.
- Clasificación de productos en perecibles y no perecibles.
- Control de stock y estado de vigencia.
- Registro de proveedores.
- Simulación del paso del tiempo para productos perecibles.

---

## Instrucciones para Ejecutar el Sistema

### Requisitos
- Python 3.7 o superior

### Pasos para ejecutar

1. Asegúrate de que todos los archivos del sistema estén en la misma carpeta:
   - `producto_2.py`
   - `producto_perecible_2.py`
   - `producto_no_perecible_2.py`
   - `proveedor_2.py`
   - `inventario_2.py`

2. Abre una terminal o consola en esa carpeta.

3. Ejecuta el archivo principal:


### Descripción de cada clase
- Producto: Clase base que representa un producto genérico del inventario. Maneja atributos comunes como código, nombre, precio, stock y un costo encapsulado. Proporciona métodos para actualizar el stock y verificar el estado del producto de forma genérica.

- ProductoPerecible: Subclase de Producto que incorpora la lógica para productos con fecha de caducidad. Permite reducir los días restantes mediante pasar_dia() y determinar si el producto está vigente o caducado a través de un método polimórfico.

- ProductoNoPerecible: Subclase de Producto diseñada para artículos que no se vencen. Redefine el método verificarEstado() para indicar que el producto está siempre vigente, diferenciándolo funcionalmente de los perecibles.

- Proveedor: Representa a los proveedores del sistema de inventario, almacenando información de contacto como nombre, teléfono y correo electrónico. Es una entidad clave para registrar la fuente de los productos.

- Inventario: Clase principal que gestiona el registro y control de todos los productos y proveedores. Permite agregar, buscar, listar y eliminar elementos, así como simular el paso del tiempo para actualizar el estado de productos perecibles.

