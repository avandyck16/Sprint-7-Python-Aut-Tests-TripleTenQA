# 1. Título del Proyecto:
## Test de Creación de Usuarios API
### Axel Van Dyck, Grupo 14, Sprint 7 
### 2. Descripción

Propósito: Este proyecto automatiza las pruebas de una API que permite crear nuevos usuarios. Incluye tanto pruebas positivas como negativas para validar el comportamiento de la API bajo diferentes condiciones.

### 3. Requisitos Previos

Lenguaje: Python 3.x

Bibliotecas:

#### requests: para realizar solicitudes HTTP.

#### pytest: para ejecutar los casos de prueba.

Instalación de dependencias:

pip install requests pytest

### 4. Estructura del Proyecto
##### Archivos principales:

##### create_user_test.py: Contiene las pruebas automatizadas para verificar la creación de usuarios con diferentes parámetros​(create_user_test).
##### data.py: Almacena datos comunes como los encabezados y el cuerpo de la solicitud POST​(data).
##### sender_stand_request.py: Define las funciones para realizar solicitudes HTTP hacia la API, incluyendo la creación de usuarios y la obtención de la tabla de usuarios​(sender_stand_request).
##### configuration.py: Configuración de las rutas de la API, como la URL base y los endpoints específicos​(configuration).

### 5. Instrucciones de Uso
Para ejecutar las pruebas, utiliza el siguiente comando:

pytest create_user_test.py

##### Pruebas disponibles:
- Pruebas positivas: Verifica que la API responda correctamente al crear usuarios con nombres válidos.
- Pruebas negativas: Verifica que la API maneje adecuadamente errores al proporcionar nombres inválidos (nombres demasiado largos, cortos, con caracteres especiales, etc.).


### 6. Casos de Prueba Principales
 - Positivos:

Crear usuario con nombre de 2 letras: 
test_create_user_2_letter_in_first_name_get_success_response.

Crear usuario con nombre de 15 letras: 
test_create_user_15_letter_in_first_name_get_success_response.

- Negativos:

Crear usuario con 1 letra: test_create_user_1_letter_in_first_name_get_error_response.

Crear usuario con nombre que contiene espacios: test_create_user_has_space_in_first_name_get_error_response.

### 7. Configuración
URL de la API: La URL base de la API utilizada para las pruebas es dinámica, asegúrate de cambiarla en la hoja configuration.py.

#### Rutas Importantes:
- Crear usuario: /api/v1/users/

- Tabla de usuarios: /api/db/resources/user_model.csv

### 8. Contribución
Si quieres contribuir, sigue los siguientes pasos:

- Haz un fork del proyecto (git@github.com:avandyck16/api_stand_tests.git).
- Crea una nueva rama para tu feature (git checkout -b nueva-feature).
- Realiza un commit de tus cambios (git commit -m 'Añadir nueva feature').
- Haz push a la rama (git push origin feature/nueva-feature).
- Crea un Pull Request

