# API de Productos con Flask (GET, POST, PUT, PATCH, DELETE)

API REST desarrollada en Python con Flask para gestionar una lista de productos en memoria. Permite consultar, crear, actualizar (completa y parcialmente) y eliminar productos, y fue probada usando Postman.

## Contenido del repositorio

- `api_productos.py`: código fuente de la API.
- `README.md`: este instructivo.

## Requisitos previos

- Python 3.10 o superior instalado ([python.org/downloads](https://www.python.org/downloads/)).
- Postman instalado ([postman.com/downloads](https://www.postman.com/downloads/)).
- Git instalado (opcional, solo si vas a clonar el repositorio).

## Instalación y ejecución paso a paso

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/Alejandro-LP/api-productos-flask.git
cd api-productos-flask
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

Activarlo:

- En Windows (PowerShell):
  ```bash
  .\venv\Scripts\Activate
  ```
- En Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Flask

```bash
pip install flask
```

### 4. Ejecutar el servidor

```bash
python api_productos.py
```

Si todo sale bien, en la terminal verás un mensaje similar a:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

El servidor queda escuchando en `http://127.0.0.1:5000`. Déjalo corriendo mientras haces las pruebas en Postman.

## Endpoints disponibles

| Método | Ruta                        | Descripción                              |
|--------|-----------------------------|-------------------------------------------|
| GET    | `/`                         | Mensaje de bienvenida                     |
| GET    | `/api/productos`            | Obtener todos los productos               |
| GET    | `/api/productos/<id>`       | Obtener un producto por su id             |
| POST   | `/api/productos`            | Crear un nuevo producto                   |
| PUT    | `/api/productos/<id>`       | Actualizar un producto completo           |
| PATCH  | `/api/productos/<id>`       | Actualizar solo algunos campos            |
| DELETE | `/api/productos/<id>`       | Eliminar un producto                      |

## Cómo probar cada método desde Postman

Abre Postman Desktop y sigue estos pasos para cada método. Con el servidor corriendo, crea una nueva petición (botón "+") y configura lo siguiente:

### 1. GET - Obtener todos los productos

- Método: `GET`
- URL: `http://127.0.0.1:5000/api/productos`
- Sin body.
- Resultado esperado: código `200` y un JSON con la lista de productos.

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla del GET en Postman -->
![GET todos los productos](capturas/get-todos.png)

### 2. GET - Obtener un producto por id

- Método: `GET`
- URL: `http://127.0.0.1:5000/api/productos/1`
- Resultado esperado: código `200` con el producto de id 1, o `404` si no existe.

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla -->
![GET un producto](capturas/get-uno.png)

### 3. POST - Crear un producto

- Método: `POST`
- URL: `http://127.0.0.1:5000/api/productos`
- Pestaña **Body** → `raw` → tipo `JSON`:
  ```json
  {
    "nombre": "Monitor",
    "precio": 300
  }
  ```
- Resultado esperado: código `201` con el producto creado (incluyendo su nuevo id).

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla -->
![POST crear producto](capturas/post-crear.png)

### 4. PUT - Actualizar un producto completo

- Método: `PUT`
- URL: `http://127.0.0.1:5000/api/productos/2`
- Pestaña **Body** → `raw` → tipo `JSON`:
  ```json
  {
    "nombre": "Mouse inalámbrico",
    "precio": 40
  }
  ```
- Resultado esperado: código `200` con el producto actualizado.

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla -->
![PUT actualizar producto](capturas/put-actualizar.png)

### 5. PATCH - Actualizar parcialmente un producto

- Método: `PATCH`
- URL: `http://127.0.0.1:5000/api/productos/2`
- Pestaña **Body** → `raw` → tipo `JSON`:
  ```json
  {
    "precio": 35
  }
  ```
- Resultado esperado: código `200`, solo el campo `precio` cambia.

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla -->
![PATCH modificar producto](capturas/patch-modificar.png)

### 6. DELETE - Eliminar un producto

- Método: `DELETE`
- URL: `http://127.0.0.1:5000/api/productos/3`
- Sin body.
- Resultado esperado: código `200` con el mensaje `"Producto eliminado"`.

**Pantallazo:**

<!-- Inserta aquí tu captura de pantalla -->
![DELETE eliminar producto](capturas/delete-eliminar.png)

## Validaciones implementadas

- Toda petición `POST`, `PUT` y `PATCH` debe enviarse en formato JSON (header `Content-Type: application/json`); de lo contrario responde `400` con el error `"Solicitud debe ser JSON"`.
- En `POST` y `PUT` los campos `nombre` y `precio` son obligatorios.
- El campo `precio` debe ser un número mayor o igual a 0; si no, responde `400`.
- El campo `id` nunca puede ser modificado por el cliente, incluso si se envía en el body de `PUT` o `PATCH`.
- Si el producto solicitado no existe, cualquier operación (`GET`, `PUT`, `PATCH`, `DELETE`) responde `404` con el mensaje `"Producto no encontrado"`.

## Notas

- Los datos se almacenan en memoria (una lista de Python), por lo que se reinician cada vez que se detiene y se vuelve a ejecutar el servidor.
- Para detener el servidor, presiona `Ctrl + C` en la terminal donde está corriendo.

## Autor

- Nombre: Alejandro López
- Curso: Nuevas Tecnologías de Desarrollo