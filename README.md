# Dream Cars

Bienvenido a **Dream Cars**, la aplicación de concesionaria desarrollada con Django para gestionar todos los aspectos de una concesionaria de autos. Este sistema web te permitirá administrar vehículos, ventas, inventarios, y mucho más con facilidad.

## Descripción del Proyecto

**Dream Cars** es una plataforma integral para concesionarias de autos, diseñada para facilitar la gestión de inventario, ventas, comentarios de usuarios y empleados. Con una estructura modular basada en Django, este proyecto incluye aplicaciones y modelos que cubren todos los aspectos necesarios para el funcionamiento eficiente de una concesionaria.

## Requisitos
- Python
- Django
- Postgresql
- psycopg2

## Aplicaciones y Modelos

### Foro

- **Comentarios**: Gestiona los comentarios de los usuarios en el foro.

### Inventario

- **Proveedor**: Maneja la información sobre los proveedores.
- **Compras**: Administra las compras realizadas a los proveedores.

### Personas

- **Usuarios**: Información sobre los usuarios del sistema.
- **Empleados**: Datos de los empleados de la concesionaria.

### Vehículos

- **Categorías**: Clasificación de los vehículos.
- **Marcas**: Información sobre las marcas de vehículos.
- **Fichas Técnicas**: Especificaciones técnicas de los vehículos.
- **Modelos**: Diferentes modelos de vehículos.
- **Vehículo**: Detalles de cada vehículo disponible en el inventario.

### Ventas

- **Ventas**: Registro y gestión de las ventas realizadas.

## Instalación y Configuración

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/hildmannn/appConcesionaria.git
    ```

2. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configura la base de datos:**

    ```bash
    python manage.py migrate
    ```

4. **Ejecuta el servidor:**

    ```bash
    python manage.py runserver
    ```

5. **Accede a la aplicación en tu navegador:**

    ```
    http://127.0.0.1:8000/
    ```
---

¡Gracias por usar **Dream Cars**!

### Autores
Lucas Salzotto & Valentin Hildmann
