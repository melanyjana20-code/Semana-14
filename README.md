# Restaurante App - Semana 14

## Descripción

Restaurante App es una aplicación desarrollada en Python como parte de la Semana 14 de la asignatura Programación Orientada a Objetos.

En esta etapa se continúa trabajando sobre el proyecto de la Semana 13, incorporando componentes y contenedores en la interfaz gráfica mediante Tkinter.

La aplicación permite iniciar sesión, consultar usuarios y realizar la gestión de productos del restaurante mediante operaciones de registro, consulta, actualización y eliminación.

La información se mantiene almacenada en archivos JSON.

## Objetivo

El objetivo de esta actividad es evolucionar el proyecto de la Semana 13 sin cambiar su arquitectura principal.

Se incorporan componentes gráficos y contenedores de Tkinter para organizar mejor la interfaz y permitir la gestión de los productos del restaurante.

El proyecto mantiene la separación entre modelos, servicios, datos e interfaz gráfica.

## Estructura del proyecto

```text
restaurante__app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
└── main.py

```

## Descripción de los componentes

### Datos

La carpeta `datos` contiene los archivos JSON utilizados para almacenar la información de la aplicación.

-   `productos.json`: contiene los productos registrados del restaurante.
    
-   `usuarios.json`: contiene los usuarios utilizados para el inicio de sesión.
    

### Modelos

La carpeta `modelos` contiene las clases principales del proyecto.

-   `producto.py`: representa los productos del restaurante.
    
-   `usuario.py`: representa los usuarios de la aplicación.
    

### Servicios

La carpeta `servicios` contiene la lógica encargada de trabajar con los datos.

-   `archivo_servicio.py`: permite leer y guardar información en los archivos JSON.
    
-   `restaurante_servicio.py`: contiene la lógica del restaurante, como la validación de usuarios y la gestión de productos.
    

### Interfaz gráfica

La carpeta `ui` contiene las vistas desarrolladas con Tkinter.

-   `login_view.py`: presenta la pantalla de inicio de sesión.
    
-   `main_view.py`: presenta el panel principal y las opciones para consultar y gestionar la información.
    

### main.py

Es el punto de entrada de la aplicación.

Se encarga de iniciar la ventana principal y conectar las diferentes partes del sistema.

## Componentes y contenedores utilizados

En esta versión se utilizan diferentes componentes de Tkinter para organizar la interfaz gráfica.

### Componentes

-   `Label`: muestra textos y títulos.
    
-   `Entry`: permite ingresar información.
    
-   `Button` o `ttk.Button`: permite ejecutar acciones mediante `command=`.
    
-   `Treeview`: permite mostrar los productos y usuarios en forma de tabla.
    
-   `Scrollbar`: permite desplazarse por la información.
    
-   `messagebox`: muestra mensajes de información, confirmación o error.
    

### Contenedores

-   `Tk`: ventana principal de la aplicación.
    
-   `Frame`: permite organizar diferentes partes de la interfaz.
    
-   `LabelFrame`: permite agrupar visualmente formularios y secciones.
    

## Organización de la interfaz

La interfaz principal se encuentra organizada mediante contenedores para facilitar la distribución de los elementos.

El sistema cuenta con una sección de navegación y un área principal donde se muestran las diferentes opciones.

La pantalla de productos contiene un formulario para ingresar información y botones para ejecutar las diferentes operaciones.

## Flujo de la aplicación

El funcionamiento de la aplicación sigue el siguiente flujo:

```text
Inicio
   ↓
Pantalla de Login
   ↓
Ingreso de usuario y contraseña
   ↓
Validación mediante RestauranteServicio
   ↓
Panel Principal
   ↓
Consultar Usuarios
   ↓
Gestionar Productos
   ↓
Registrar / Consultar / Actualizar / Eliminar
   ↓
Guardar información en productos.json
   ↓
Actualizar la interfaz
   ↓
Cerrar sesión
   ↓
Regreso al Login

```

## Funcionalidades

Actualmente la aplicación permite:

-   Iniciar sesión mediante usuario y contraseña.
    
-   Validar las credenciales del usuario.
    
-   Mostrar mensajes cuando los campos están vacíos.
    
-   Consultar los usuarios registrados.
    
-   Consultar los productos registrados.
    
-   Registrar nuevos productos.
    
-   Buscar y cargar productos.
    
-   Actualizar productos existentes.
    
-   Eliminar productos.
    
-   Limpiar los campos del formulario.
    
-   Guardar los cambios en el archivo `productos.json`.
    
-   Actualizar la información mostrada en la interfaz.
    
-   Cerrar sesión y regresar al inicio.
    

## CRUD de productos

La gestión de productos se realiza desde la pantalla principal.

### Registrar

Permite agregar un nuevo producto al sistema.

Antes de registrar el producto se comprueba la información ingresada para evitar datos incorrectos o repetidos.

### Consultar

Permite cargar y mostrar los productos almacenados en el archivo JSON.

### Actualizar

Permite modificar la información de un producto existente.

### Eliminar

Permite eliminar un producto registrado.

### Limpiar

Permite borrar la información ingresada en el formulario para realizar una nueva operación.

## Uso de `command=`

Los botones de la aplicación utilizan el parámetro `command=` para ejecutar las funciones correspondientes.

Por ejemplo:

```python
ttk.Button(
    frame,
    text="Registrar",
    command=registrar_producto
)

```

De esta manera, cada botón ejecuta una acción específica.

En esta actividad no se utilizan eventos avanzados como:

-   `bind()`
    
-   Doble clic.
    
-   Eventos de teclado.
    
-   Eventos de mouse.
    
-   Edición directa dentro del `Treeview`.
    

## Persistencia de datos

La aplicación utiliza archivos JSON para conservar la información.

Los productos se almacenan en:

```text
datos/productos.json

```

Los usuarios se almacenan en:

```text
datos/usuarios.json

```

Cuando se realizan cambios en los productos, la información se guarda nuevamente en el archivo JSON.

## Arquitectura del proyecto

El proyecto mantiene una separación de responsabilidades entre sus diferentes capas:

```text
Interfaz gráfica
       ↓
Servicios
       ↓
Modelos
       ↓
Archivos JSON

```

Esta organización permite mantener el código ordenado y facilita agregar nuevas funcionalidades al proyecto.

## Requisitos

Para ejecutar el proyecto se necesita:

-   Python 3.
    
-   Tkinter.
    
-   Visual Studio Code u otro editor de código.
    

Tkinter se utiliza para crear la interfaz gráfica de la aplicación.

## Ejecución

Para ejecutar el proyecto:

1.  Abrir la carpeta `restaurante__app` en Visual Studio Code.
    
2.  Abrir una terminal.
    
3.  Ubicarse dentro de la carpeta del proyecto.
    
4.  Ejecutar:
    

```bash
python main.py

```

También se puede utilizar:

```bash
py main.py

```

5.  Se mostrará la pantalla de inicio de sesión.
    
6.  Ingresar las credenciales de prueba.
    
7.  Desde el panel principal se pueden consultar usuarios y gestionar productos.
    

## Credenciales de prueba

Para realizar las pruebas de acceso se puede utilizar:

```text
Usuario: admin
Contraseña: 1234

```

## Tecnologías utilizadas

-   Python
    
-   Tkinter
    
-   Programación Orientada a Objetos
    
-   Archivos JSON
    
-   Visual Studio Code
    
-   GitHub
    

## Conclusión

La Semana 14 permite continuar con el desarrollo del Restaurante App incorporando componentes y contenedores en la interfaz gráfica.

La aplicación mantiene la estructura de la Semana 13 y agrega la gestión de productos mediante formularios, botones y tablas.

El uso de servicios y archivos JSON permite separar la lógica del programa de la interfaz y mantener los datos almacenados de manera sencilla.

El proyecto queda preparado para continuar incorporando nuevas funcionalidades en las siguientes semanas.