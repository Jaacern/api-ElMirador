from flask import jsonify, request
from config.config import app, mongo
from models.models import Departamento, Residente, GastoComun
from bson import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@app.route('/departamentos', methods=['POST'])
def create_departamento():
    try:
        data = request.json
        if data:
            # Validar que CodDepto no exista
            if mongo.db.departamentos.find_one({"CodDepto": data["CodDepto"]}):
                return jsonify({"error": "CodDepto ya existe"}), 400
            
            # Convertir fechas de string a datetime si existen
            if "FechaIniC" in data and data["FechaIniC"]:
                data["FechaIniC"] = datetime.strptime(data["FechaIniC"], "%Y-%m-%d")
            if "FechaFinC" in data and data["FechaFinC"]:
                data["FechaFinC"] = datetime.strptime(data["FechaFinC"], "%Y-%m-%d")
            
            result = mongo.db.departamentos.insert_one(data)
            return jsonify({"message": "Departamento creado exitosamente", "id": str(result.inserted_id)}), 201
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/departamentos', methods=['GET'])
def get_departamentos():
    try:
        departamentos = list(mongo.db.departamentos.find())
        return jsonify([Departamento.to_json(depto) for depto in departamentos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/departamentos/<int:cod_depto>', methods=['GET'])
def get_departamento(cod_depto):
    try:
        departamento = mongo.db.departamentos.find_one({"CodDepto": cod_depto})
        if departamento:
            return jsonify(Departamento.to_json(departamento)), 200
        return jsonify({"error": "Departamento no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/departamentos/<int:cod_depto>', methods=['PUT'])
def update_departamento(cod_depto):
    try:
        data = request.json
        if data:
            # Convertir fechas de string a datetime si existen
            if "FechaIniC" in data and data["FechaIniC"]:
                data["FechaIniC"] = datetime.strptime(data["FechaIniC"], "%Y-%m-%d")
            if "FechaFinC" in data and data["FechaFinC"]:
                data["FechaFinC"] = datetime.strptime(data["FechaFinC"], "%Y-%m-%d")
            
            result = mongo.db.departamentos.update_one(
                {"CodDepto": cod_depto},
                {"$set": data}
            )
            if result.modified_count:
                return jsonify({"message": "Departamento actualizado exitosamente"}), 200
            return jsonify({"error": "Departamento no encontrado"}), 404
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/departamentos/<int:cod_depto>', methods=['DELETE'])
def delete_departamento(cod_depto):
    try:
        result = mongo.db.departamentos.delete_one({"CodDepto": cod_depto})
        if result.deleted_count:
            return jsonify({"message": "Departamento eliminado exitosamente"}), 200
        return jsonify({"error": "Departamento no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/accesos', methods=['POST'])
def create_acceso():
    try:
        data = request.json
        if data:
            # Verificar si el username ya existe
            if mongo.db.accesos.find_one({"username": data["username"]}):
                return jsonify({"error": "Username ya existe"}), 400
            
            # Establecer fechas
            data["fechaCreacion"] = datetime.now()
            if "fechaultimoacceso" in data and data["fechaultimoacceso"]:
                data["fechaultimoacceso"] = datetime.strptime(data["fechaultimoacceso"], "%Y-%m-%d %H:%M:%S")
            
            # Hash de la contraseña antes de guardar
            data["password"] = generate_password_hash(data["password"])
            
            result = mongo.db.accesos.insert_one(data)
            return jsonify({"message": "Acceso creado exitosamente", "id": str(result.inserted_id)}), 201
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/accesos', methods=['GET'])
def get_accesos():
    try:
        accesos = list(mongo.db.accesos.find())
        return jsonify([acceso.to_json(acceso) for acceso in accesos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/accesos/<string:username>', methods=['GET'])
def get_acceso(username):
    try:
        acceso = mongo.db.accesos.find_one({"username": username})
        if acceso:
            return jsonify(acceso.to_json(acceso)), 200
        return jsonify({"error": "Acceso no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/accesos/<string:username>', methods=['PUT'])
def update_acceso(username):
    try:
        data = request.json
        if data:
            # Si se actualiza la contraseña, hashearla
            if "password" in data:
                data["password"] = generate_password_hash(data["password"])
            
            # Si se actualiza fechaultimoacceso
            if "fechaultimoacceso" in data and data["fechaultimoacceso"]:
                data["fechaultimoacceso"] = datetime.strptime(data["fechaultimoacceso"], "%Y-%m-%d %H:%M:%S")
            
            result = mongo.db.accesos.update_one(
                {"username": username},
                {"$set": data}
            )
            if result.modified_count:
                return jsonify({"message": "Acceso actualizado exitosamente"}), 200
            return jsonify({"error": "Acceso no encontrado"}), 404
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/accesos/<string:username>', methods=['DELETE'])
def delete_acceso(username):
    try:
        result = mongo.db.accesos.delete_one({"username": username})
        if result.deleted_count:
            return jsonify({"message": "Acceso eliminado exitosamente"}), 200
        return jsonify({"error": "Acceso no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rutas para CuotaGC
@app.route('/cuotas', methods=['POST'])
def create_cuota():
    try:
        data = request.json
        if data:
            # Obtener el último IdCuotaGC para autoincremento
            last_cuota = mongo.db.cuotas.find_one(sort=[("IdCuotaGC", -1)])
            if last_cuota:
                data["IdCuotaGC"] = last_cuota["IdCuotaGC"] + 1
            else:
                data["IdCuotaGC"] = 1
            
            # Convertir fecha si existe
            if "FechaPago" in data and data["FechaPago"]:
                data["FechaPago"] = datetime.strptime(data["FechaPago"], "%Y-%m-%d")
            
            # Validar que el CodDepto exista
            if not mongo.db.departamentos.find_one({"CodDepto": data["CodDepto"]}):
                return jsonify({"error": "Departamento no existe"}), 400
            
            result = mongo.db.cuotas.insert_one(data)
            return jsonify({"message": "Cuota creada exitosamente", "id": str(result.inserted_id)}), 201
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cuotas', methods=['GET'])
def get_cuotas():
    try:
        cuotas = list(mongo.db.cuotas.find())
        return jsonify([cuota.to_json(cuota) for cuota in cuotas]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cuotas/<int:id_cuota>', methods=['GET'])
def get_cuota(id_cuota):
    try:
        cuota = mongo.db.cuotas.find_one({"IdCuotaGC": id_cuota})
        if cuota:
            return jsonify(cuota.to_json(cuota)), 200
        return jsonify({"error": "Cuota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cuotas/<int:id_cuota>', methods=['PUT'])
def update_cuota(id_cuota):
    try:
        data = request.json
        if data:
            # Convertir fecha si existe
            if "FechaPago" in data and data["FechaPago"]:
                data["FechaPago"] = datetime.strptime(data["FechaPago"], "%Y-%m-%d")
            
            result = mongo.db.cuotas.update_one(
                {"IdCuotaGC": id_cuota},
                {"$set": data}
            )
            if result.modified_count:
                return jsonify({"message": "Cuota actualizada exitosamente"}), 200
            return jsonify({"error": "Cuota no encontrada"}), 404
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cuotas/<int:id_cuota>', methods=['DELETE'])
def delete_cuota(id_cuota):
    try:
        result = mongo.db.cuotas.delete_one({"IdCuotaGC": id_cuota})
        if result.deleted_count:
            return jsonify({"message": "Cuota eliminada exitosamente"}), 200
        return jsonify({"error": "Cuota no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    





# Ruta para crear un nuevo Residente (POST)
@app.route('/residentes', methods=['POST'])
def add_residente():
    data = request.get_json()  # Obtener datos del cuerpo de la solicitud
    
    # Verificamos si los campos necesarios están presentes
    if not data.get("RutArre") or not data.get("Nombre"):
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    # Crear un nuevo residente
    residente = {
        "RutArre": data.get("RutArre"),
        "Nombre": data.get("Nombre"),
        "ApePat": data.get("ApePat", ""),
        "ApeMat": data.get("ApeMat", ""),
        "Email": data.get("Email", ""),
        "Fono1": data.get("Fono1", ""),
        "Fono2": data.get("Fono2", ""),
        "nro_departamento": data.get("nro_departamento")
    }
    
    # Insertar el residente en la base de datos
    result = mongo.db.residentes.insert_one(residente)
    return jsonify({
        "message": "Residente creado exitosamente",
          "_id": str(result.inserted_id)}), 201

# Ruta para obtener todos los Residentes (GET)
@app.route('/residentes', methods=['GET'])
def get_residentes():
    residentes = mongo.db.residentes.find()  # Buscar todos los residentes
    return jsonify([Residente.to_json(res) for res in residentes]), 200

# Ruta para obtener un Residente por ID (GET)
@app.route('/residentes/<id>', methods=['GET'])
def get_residente(id):
    residente = mongo.db.residentes.find_one({"_id": ObjectId(id)})  # Buscar por ID
    if residente:
        return jsonify(Residente.to_json(residente)), 200
    return jsonify({"error": "Residente no encontrado"}), 404

# Ruta para actualizar un Residente (PUT)
@app.route('/residentes/<id>', methods=['PUT'])
def update_residente(id):
    data = request.get_json()
    
    # Verificamos si los campos requeridos son válidos
    if not data.get("RutArre") or not data.get("Nombre"):
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    # Actualizamos los datos del residente
    result = mongo.db.residentes.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "RutArre": data.get("RutArre"),
            "Nombre": data.get("Nombre"),
            "ApePat": data.get("ApePat", ""),
            "ApeMat": data.get("ApeMat", ""),
            "Email": data.get("Email", ""),
            "Fono1": data.get("Fono1", ""),
            "Fono2": data.get("Fono2", ""),
            "nro_departamento": data.get("nro_departamento")
        }}
    )
    
    if result.matched_count > 0:
        return jsonify({"message": "Residente actualizado"}), 200
    return jsonify({"error": "Residente no encontrado"}), 404

# Ruta para eliminar un Residente (DELETE)
@app.route('/residentes/<id>', methods=['DELETE'])
def delete_residente(id):
    result = mongo.db.residentes.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count > 0:
        return jsonify({"message": "Residente eliminado"}), 200
    return jsonify({"error": "Residente no encontrado"}), 404







# Rutas para GastoComun
@app.route('/gastos-comunes', methods=['POST'])
def add_gasto_comun():
    data = request.get_json()
    
    if not all(key in data for key in ["mes", "anio", "valor", "nro_departamento"]):
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    
    gasto_comun = {
        "mes": data.get("mes"),
        "anio": data.get("anio"),
        "valor": data.get("valor"),
        "nro_departamento": data.get("nro_departamento"),
        "estado_pago": False  # Por defecto el estado es no pagado
    }
    
    result = mongo.db.gastos_comunes.insert_one(gasto_comun)
    return jsonify({
        "message": "Gasto común creado exitosamente",
        "_id": str(result.inserted_id)}), 201

@app.route('/gastos-comunes', methods=['GET'])
def get_gastos_comunes():
    depto = request.args.get('departamento')
    if depto:
        gastos = mongo.db.gastos_comunes.find({"nro_departamento": depto})
    else:
        gastos = mongo.db.gastos_comunes.find()
    return jsonify([GastoComun.to_json(gasto) for gasto in gastos]), 200

@app.route('/gastos-comunes/<id>', methods=['PUT'])
def update_gasto_comun(id):
    data = request.get_json()
    
    result = mongo.db.gastos_comunes.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "estado_pago": data.get("estado_pago", False)
        }}
    )
    
    if result.matched_count > 0:
        return jsonify({"message": "Gasto común actualizado"}), 200
    return jsonify({"error": "Gasto común no encontrado"}), 404

@app.route('/gastos-comunes/<id>', methods=['DELETE'])
def delete_gasto_comun(id):
    result = mongo.db.gastos_comunes.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count > 0:
        return jsonify({"message": "Gasto común eliminado"}), 200
    return jsonify({"error": "Gasto común no encontrado"}), 404

@app.route('/gastos-comunes/pendientes', methods=['GET'])
def get_gastos_pendientes():
    gastos = mongo.db.gastos_comunes.find({"estado_pago": False})
    return jsonify([GastoComun.to_json(gasto) for gasto in gastos]), 200





