# Test Automatizados
## Axel Van Dyck, Grupo 14, Sprint 7 
### 2. Descripción

## 1. Automatización de pruebas API para creación de usuarios en plataforma (*api_stand_tests*)

-   Este proyecto automatiza las pruebas de una API que permite crear nuevos usuarios. Incluye tanto pruebas positivas como negativas para validar el comportamiento de la API bajo diferentes condiciones.

## 2. Test de Creacion de un Kit de Productos

- Este proyecto automatiza las pruebas de una API que permite crear nuevos usuarios. Incluye tanto pruebas positivas como negativas para validar el comportamiento de la API bajo diferentes condiciones.

### 3. Requisitos Previos

Lenguaje: Python 3.x

Bibliotecas:

#### requests: para realizar solicitudes HTTP.

#### pytest: para ejecutar los casos de prueba.

Instalación de dependencias:

pip install requests pytest

### 4. Estructura del Proyecto
##### Archivos principales:

##### Cada set de pruebas automatizadas está categorizado en:
##### data.py: Almacena datos como los encabezados y el cuerpo de las solicitudes
##### Métodos/Funciones: Archivo donde se definen las funciones para realizar solicitudes HTTP hacia la API
##### configuration.py: Configuración de las rutas de la API, como la URL base y los endpoints específicos

### 5. Instrucciones de Uso
Para ejecutar las pruebas, utiliza:

pytest

##### Pruebas disponibles:
- Pruebas positivas: Verifica las respuestas 200 / 201 del endpoint.
- Pruebas negativas: Verifica que la API maneje adecuadamente errores.

## api_stand_tests: 
- Ejecuta pruebas para crear usuarios.

## qa-project-Urban-Grocers-app-es: 
- Ejecuta pruebas de creacion de un Kit de Productos.

## Se proporciona una version 2 de qa-project-Urban-Grocers-app-es:

- Está escrita sin *hard-coding*: todos los datos de configuración están almacenados en data.py

- En esta version el token se obtiene en cada solicitud.

- En la otra version el token se obtuvo en la primera solicitud, se guarda y es el mismo que se va a utilizar en las demás solicitudes.
