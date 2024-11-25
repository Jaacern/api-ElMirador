from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)

# Configuración de MongoDB
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@edificiomirador.xtxn8.mongodb.net/ELMirador?retryWrites=true&w=majority&appName=EdificioMirador"
mongo = PyMongo(app)
