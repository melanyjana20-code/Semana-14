# Restaurante App - Semana 13

## Descripción

Restaurante App es una aplicación desarrollada en Python como parte de la Semana 13 de la asignatura Programación Orientada a Objetos.

En esta etapa se implementa una interfaz gráfica de usuario utilizando Tkinter. La aplicación permite simular el acceso de usuarios y consultar los productos y usuarios registrados mediante archivos JSON.

El proyecto utiliza una estructura organizada en modelos, servicios, datos e interfaz gráfica.

## Objetivo

El objetivo de esta actividad es adaptar la estructura del proyecto docente Biblioteca App al contexto de un restaurante, utilizando una interfaz gráfica con Tkinter y manteniendo una separación de responsabilidades entre modelos, servicios y vistas.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── main.py
```
## Descripción de los componentes

## Datos

La carpeta `datos` contiene los archivos JSON utilizados para almacenar la información de usuarios y productos.

-   `productos.json`: contiene los productos registrados del restaurante.
-   `usuarios.json`: contiene los usuarios utilizados para la simulación de acceso.

### Modelos

La carpeta `modelos` contiene las clases principales del proyecto.

-   `producto.py`: representa los productos del restaurante.
-   `usuario.py`: representa los usuarios de la aplicación.

### Servicios

La carpeta `servicios` contiene la lógica para trabajar con los datos.

-   `archivo_servicio.py`: se encarga de leer la información almacenada en los archivos JSON.
-   `restaurante_servicio.py`: convierte los datos en objetos y permite validar usuarios, listar usuarios y listar productos.

### Interfaz gráfica

La carpeta `ui` contiene las vistas desarrolladas con Tkinter.

-   `login_view.py`: presenta la pantalla de inicio de sesión.
-   `main_view.py`: presenta el panel principal y permite consultar productos y usuarios.

### main.py

Es el punto de entrada de la aplicación. Se encarga de crear la ventana principal, cargar los datos, preparar los servicios y conectar las diferentes vistas.

## Flujo de la aplicación

El funcionamiento de la aplicación sigue el siguiente flujo:

```
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
Consultar Productos / Consultar Usuarios
  ↓
Cerrar sesión
  ↓
Regreso al Login
```

La aplicación utiliza una única ventana principal de Tkinter.

## Funcionalidades

Actualmente la aplicación permite:

-   Iniciar sesión mediante usuario y contraseña.
-   Mostrar mensajes cuando los campos están vacíos.
-   Validar las credenciales del usuario.
-   Mostrar los productos registrados.
-   Mostrar los usuarios registrados.
-   Cerrar sesión y regresar al inicio.
-   Mostrar la opción de Ventas como funcionalidad pendiente.

## Credenciales de prueba

Para realizar las pruebas de acceso se puede utilizar:

```
Usuario: admin
Contraseña: 1234
```

## Requisitos

Para ejecutar el proyecto se necesita:

-   Python 3.
-   Tkinter.
-   Visual Studio Code u otro editor de código.

Tkinter forma parte de la instalación habitual de Python.

## Ejecución

1.  Abrir la carpeta `restaurante_app` en Visual Studio Code.
2.  Abrir una terminal.
3.  Ubicarse dentro de la carpeta del proyecto.
4.  Ejecutar el siguiente comando:

```
python main.py
```

5.  Se mostrará la pantalla de inicio de sesión.
6.  Ingresar las credenciales de prueba.
7.  Desde el panel principal se pueden consultar los productos y usuarios.

## Funcionalidades pendientes

La opción de **Ventas** se mantiene como pendiente en esta etapa. Las funcionalidades adicionales del restaurante serán desarrolladas progresivamente en las siguientes semanas.

## Conclusión

Esta versión permite comprender la integración entre programación orientada a objetos archivos JSON, servicios e interfaces gráficas mediante Tkinter. La estructura del proyecto facilita continuar agregando nuevas funcionalidades en las siguientes etapas.