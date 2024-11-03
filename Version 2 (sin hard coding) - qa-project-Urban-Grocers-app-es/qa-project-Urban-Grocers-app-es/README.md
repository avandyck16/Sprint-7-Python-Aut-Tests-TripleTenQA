# Proyecto Urban Grocers 

# 1. Título del Proyecto:
## Proyecto Urban.Grocers 
### Test de Creacion de un Kit de Productos con el campo "name"
### Axel Van Dyck, Grupo 14, Sprint 7 
### 2. Descripción

Propósito: Este proyecto automatiza las pruebas de una API que permite crear kits de productos para un usuario. 
Incluye tanto pruebas positivas como negativas para validar el comportamiento de la API bajo diferentes condiciones de nombre de Kit.


### **3. Requisitos Previos**

Lenguaje: Python 3.x

Bibliotecas:

#### requests:para realizar solicitudes HTTP.

#### pytest: para ejecutar los casos de prueba.

Instalación de dependencias:

pip install requests pytest

1. Crea un usuario e imprime el auth token, y guardalo.
2. Asegurate de almacenar el authorization token en data.py; 
ese auth token es el que se va a utilizar para asignar el kit que vas a crear, 
en el header de la solicitud de creacion de kit.
3. Después de crear el usuario, ejecuta la solicitud POST para crear un kit, y asegúrate que
el token coincide con el que almacenaste en data.py



### 4. Estructura del Proyecto
##### Archivos principales:

##### configuration.py: Configuración de las rutas de la API, como la URL base y los endpoints específicos.
##### data.py: Almacena datos necesarios: los encabezados, auth token, y el cuerpo de las solicitudes POST. 
##### sender_stand_request.py: Define las funciones para realizar solicitudes HTTP hacia la API, incluyendo la creación de usuarios y la creación de un kit.
##### create_user_test.py: Contiene las pruebas automatizadas para verificar la creación de kits con diferentes parámetros para "name". 



### 5. Instrucciones de Uso
Para ejecutar las pruebas, utiliza el siguiente comando:

pytest create_kit_name_kit_test.py

##### Pruebas disponibles:
- Pruebas positivas: Verifica que la API responda correctamente al crear kits con nombres válidos.
- Pruebas negativas: Verifica que la API maneje adecuadamente errores al proporcionar nombres inválidos (nombres demasiado largos, cortos, con caracteres especiales, etc.).


### 6. Casos de Prueba Principales
### - Positivos:
 - - Se espera un código de respuesta 201, y que el nombre en la respuesta coincida con el nombre en la solicitud. 

### 1. Crear kit con nombre de 1 letra: 
def test_create_kit_allowed_chars_1_success():
    
### 2. Crear kit con nombre permitido máximo de 511 letras:
def test_create_kit_max_allowed_chars_511_success():
    
### 3. Crear kit con nombre que contiene caracteres especiales:
def test_create_kit_with_special_chars_success():
    
### 4. Crear kit con nombre con espacios:
def test_create_kit_with_spaces_success():
    
### 5. Crear kit con nombre que son números en forma de string:
def test_create_kit_with_numbers_success():


### - Negativos:
- - Se espera un código de respuesta 400

### 1. Crear un kit con cero caracteres:
def test_create_kit_zero_chars_code_400():
    
### 2. Crear un kit con 512 caracteres que exceden el máximo permitido:
def test_create_kit_512_chars_code_400():
    
### 3. Crear un kit sin enviar parámetros:
def test_create_kit_empty_params_code_400():
    
### 4. Crear un kit con números por nombre:
def test_create_kit_integer_code_400():
    

## 7. Configuración
URL de la API: La URL base de la API utilizada para las pruebas es dinámica, asegúrate de cambiarla en la hoja configuration.py.

#### Rutas Importantes:
- Crear usuario: /api/v1/users/

- Creación de Kits: "/api/v1/kits"

- API_DOCS = "/docs/"

### 8. Contribución
Si quieres contribuir, sigue los siguientes pasos:

- Haz un fork del proyecto (URL de Repo GitHub).
- Crea una nueva rama para tu feature (git checkout -b feature/nueva-feature).
- Realiza un commit de tus cambios (git commit -m 'Añadir nueva feature').
- Haz push a la rama (git push origin feature/nueva-feature).
- Crea un Pull Request.

