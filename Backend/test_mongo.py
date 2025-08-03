#!/usr/bin/env python3
"""
Script de prueba para verificar la conexión a MongoDB
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

def test_mongo_connection():
    """Prueba la conexión a MongoDB"""
    
    # URI de conexión
    uri = "mongodb+srv://fox:pNHwCtXxhgNLXigL@cluster0.1d1sfvm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    try:
        print("🔌 Intentando conectar a MongoDB...")
        
        # Crear cliente con timeout
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        
        # Verificar conexión
        client.admin.command('ping')
        print("✅ Conexión exitosa a MongoDB!")
        
        # Listar bases de datos
        databases = client.list_database_names()
        print(f"📊 Bases de datos disponibles: {databases}")
        
        # Probar acceso a la base de datos
        db = client.get_database()
        collections = db.list_collection_names()
        print(f"📁 Colecciones disponibles: {collections}")
        
        client.close()
        return True
        
    except ConnectionFailure as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except ServerSelectionTimeoutError as e:
        print(f"❌ Timeout del servidor: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    test_mongo_connection() 