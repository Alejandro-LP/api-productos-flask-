from flask import Flask, jsonify, request

# Crear la aplicación Flask
app = Flask(__name__)

# ----------------------------------------------------------------
# "Base de datos" simulada en memoria.
# Cada producto tiene: id, nombre y precio.
# ----------------------------------------------------------------
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 75}
]


# Ruta principal
@app.route('/')
def inicio():
    return jsonify({"mensaje": "Bienvenido a la API de Productos"})


# ==================================================================
# GET: Obtener todos los productos
# ==================================================================
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos), 200


# ==================================================================
# GET: Obtener un producto por ID
# ==================================================================
@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)

    if producto:
        return jsonify(producto), 200

    return jsonify({"error": "Producto no encontrado"}), 404


# ==================================================================
# POST: Crear un nuevo producto
# ==================================================================
@app.route('/api/productos', methods=['POST'])
def add_producto():
    # Validar que la petición venga en formato JSON
    if not request.is_json:
        return jsonify({"error": "Solicitud debe ser JSON"}), 400

    datos = request.get_json()

    # Validar que vengan los campos obligatorios
    if not datos.get("nombre") or datos.get("precio") is None:
        return jsonify({"error": "Faltan campos requeridos: nombre y precio"}), 400

    # Validar que el precio sea un número válido y positivo
    if not isinstance(datos.get("precio"), (int, float)) or datos["precio"] < 0:
        return jsonify({"error": "El precio debe ser un número mayor o igual a 0"}), 400

    # Generar un id automático (el siguiente disponible)
    nuevo_id = max([p["id"] for p in productos]) + 1 if productos else 1

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "precio": datos["precio"]
    }

    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201


# ==================================================================
# PUT: Actualizar un producto existente (reemplazo completo)
# ==================================================================
@app.route('/api/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    if not request.is_json:
        return jsonify({"error": "Solicitud debe ser JSON"}), 400

    datos = request.get_json()

    if not datos.get("nombre") or datos.get("precio") is None:
        return jsonify({"error": "Faltan campos requeridos: nombre y precio"}), 400

    if not isinstance(datos.get("precio"), (int, float)) or datos["precio"] < 0:
        return jsonify({"error": "El precio debe ser un número mayor o igual a 0"}), 400

    # Actualizamos los datos, pero el id nunca cambia
    producto["nombre"] = datos["nombre"]
    producto["precio"] = datos["precio"]

    return jsonify(producto), 200


# ==================================================================
# PATCH: Actualizar parcialmente un producto (solo algunos campos)
# ==================================================================
@app.route('/api/productos/<int:id>', methods=['PATCH'])
def patch_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    if not request.is_json:
        return jsonify({"error": "Solicitud debe ser JSON"}), 400

    datos = request.get_json()

    if "precio" in datos and (not isinstance(datos["precio"], (int, float)) or datos["precio"] < 0):
        return jsonify({"error": "El precio debe ser un número mayor o igual a 0"}), 400

    # Solo se actualizan los campos enviados; el id nunca se toca
    for campo, valor in datos.items():
        if campo != "id":
            producto[campo] = valor

    return jsonify(producto), 200


# ==================================================================
# DELETE: Eliminar un producto
# ==================================================================
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    global productos
    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    productos = [p for p in productos if p["id"] != id]
    return jsonify({"mensaje": "Producto eliminado correctamente"}), 200


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)