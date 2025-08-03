from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime
import logging

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)

# Configuración de MongoDB - especificando la base de datos
app.config["MONGO_URI"] = ""

try:
    mongo = PyMongo(app)
    # Verificar la conexión
    mongo.db.command('ping')
    print("✅ Conexión a MongoDB establecida correctamente")
    print(f"📊 Base de datos: {mongo.db.name}")
except Exception as e:
    print(f"❌ Error al conectar con MongoDB: {e}")
    mongo = None
 