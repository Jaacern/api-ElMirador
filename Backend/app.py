from flask import Flask
from config.config import app, mongo
from routes.routes import *
from flask_cors import CORS

# Habilitar CORS
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)