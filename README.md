# 🏢 ResidentePro: Sistema Integral de Gestión de Residentes 🚀

## 🌐 Descripción del Proyecto
Sistema fullstack para administración de residentes y gastos comunes, diseñado para optimizar la gestión de comunidades residenciales.

## 🔧 Arquitectura Tecnológica

### Backend
- **Lenguaje**: Python 🐍
- **Framework**: Flask
- **Base de Datos**: MongoDB Atlas
- **ODM**: PyMongo

### Frontend
- **Framework**: Vue.js
- **Visualización**: Chart.js
- **Cliente HTTP**: Axios
- **Testing**: Postman

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.8+
- MongoDB Atlas
- Node.js 14+
- Gestor de paquetes (npm/yarn)

### Configuración del Entorno

#### Backend
```bash
# Clonar repositorio
git clone https://github.com/Jaacern/api-ElMirador
cd ResidentePro

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
export MONGO_URI='mongodb+srv://tu-cadena-de-conexion'
export FLASK_ENV=development
```

#### Frontend
```bash
# Instalar dependencias de Vue
cd frontend
npm install

# Iniciar servidor de desarrollo
npm run serve
```

## 🔍 Endpoints de API

### Gestión de Residentes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/residentes` | Crear nuevo residente |
| GET | `/residentes` | Listar todos los residentes |
| GET | `/residentes/<id>` | Obtener residente específico |
| PUT | `/residentes/<id>` | Actualizar datos de residente |
| DELETE | `/residentes/<id>` | Eliminar residente |

### Gestión de Gastos Comunes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/gastos-comunes` | Registrar nuevo gasto común |
| GET | `/gastos-comunes` | Listar gastos comunes |
| GET | `/gastos-comunes/pendientes` | Consultar gastos pendientes |
| PUT | `/gastos-comunes/<id>` | Actualizar estado de pago |
| DELETE | `/gastos-comunes/<id>` | Eliminar gasto común |

## 🧪 Estrategia de Testing

### Backend
- Pruebas unitarias con `pytest`
- Cobertura de código
- Validación de esquemas

### Frontend
- Componentes con `vue-test-utils`
- Testing end-to-end con Cypress

## 🔒 Seguridad

### Medidas de Protección
- Autenticación JWT
- Validación de esquemas
- Sanitización de inputs
- CORS configurado
- Variables de entorno seguras

## 📊 Características Avanzadas
- Dashboard de administración
- Generación de reportes
- Notificaciones automáticas
- Integración con pasarelas de pago

## 🚀 Despliegue

### Infraestructura Recomendada
- Backend: Heroku, AWS, DigitalOcean
- Frontend: Netlify, Vercel
- Base de Datos: MongoDB Atlas

## 🤝 Contribución
1. Fork del repositorio
2. Crear rama de características
3. Commits descriptivos
4. Pull Requests con descripción detallada

## 📄 Licencia
MIT License

## 📞 Contacto
- Email: javiercernadh@gmail.com
- LinkedIn: https://cl.linkedin.com/in/javier-ignacio-cerna-chavez-32254030a
- GitHub: https://github.com/Jaacern

## 🌟 Próximas Mejoras
- Módulo de pagos en línea
- Integración con servicios de mensajería
- Panel de analytics avanzado
- Panel de Herramientas
- Sistema de login y registro avanzado
- Medidores Personalizados y estadisticas adaptables

¡Construye comunidades más inteligentes! 🏘️💻
