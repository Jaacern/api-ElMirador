# 🏢 El Mirador - Sistema de Gestión Residencial

<div align="center">

![El Mirador Logo](https://img.shields.io/badge/El%20Mirador-Sistema%20Residencial-blue?style=for-the-badge&logo=home)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vue.js)
![Flask](https://img.shields.io/badge/Flask-2.3.2-000000?style=for-the-badge&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-4.3.3-47A248?style=for-the-badge&logo=mongodb)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/el-mirador?style=for-the-badge)](https://github.com/tu-usuario/el-mirador/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/el-mirador?style=for-the-badge)](https://github.com/tu-usuario/el-mirador/network)

</div>

---

## 📋 Tabla de Contenidos

- [🚀 Descripción](#-descripción)
- [✨ Características](#-características)
- [🛠️ Tecnologías](#️-tecnologías)
- [📦 Instalación](#-instalación)
- [🎯 Uso](#-uso)
- [🏗️ Estructura del Proyecto](#️-estructura-del-proyecto)
- [📊 Capturas de Pantalla](#-capturas-de-pantalla)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia](#-licencia)

---

## 🚀 Descripción

**El Mirador** es un sistema de gestión residencial completo y moderno diseñado para administrar comunidades, edificios y conjuntos residenciales. Ofrece una interfaz intuitiva y funcionalidades avanzadas para la gestión de residentes, personal, gastos comunes y reportes.

### 🎯 Objetivo Principal

Simplificar y automatizar la administración de propiedades residenciales, proporcionando herramientas eficientes para:
- Gestión de residentes y personal
- Control de gastos comunes
- Generación de reportes y estadísticas
- Dashboard interactivo con métricas en tiempo real

---

## ✨ Características

### 👥 Gestión de Residentes
- 📝 Registro y gestión de residentes
- 🏠 Asignación de departamentos
- 📧 Comunicación integrada
- 📊 Historial de pagos y estados

### 👨‍💼 Gestión de Personal
- 👤 Registro de personal administrativo
- 🎯 Asignación de cargos y responsabilidades
- 📈 Control de estados activo/inactivo
- 📋 Gestión de horarios y permisos

### 💰 Gastos Comunes
- 💸 Generación automática de gastos
- 📅 Control por mes y año
- 💳 Seguimiento de pagos
- 📊 Reportes financieros

### 📊 Dashboard y Estadísticas
- 📈 Gráficos interactivos
- 📊 Métricas en tiempo real
- 🎨 Interfaz moderna y responsive
- 📱 Diseño adaptativo

### 📋 Reportes Avanzados
- 📄 Generación de reportes personalizados
- 📊 Exportación en múltiples formatos
- 🔍 Filtros avanzados
- 📈 Análisis histórico

---

## 🛠️ Tecnologías

### Frontend
![Vue.js](https://img.shields.io/badge/Vue.js-3.2.13-4FC08D?style=flat-square&logo=vue.js)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-7952B3?style=flat-square&logo=bootstrap)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4.6-FF6384?style=flat-square&logo=chart.js)
![Axios](https://img.shields.io/badge/Axios-1.7.7-5A29E4?style=flat-square&logo=axios)

### Backend
![Flask](https://img.shields.io/badge/Flask-2.3.2-000000?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-4.3.3-47A248?style=flat-square&logo=mongodb)

### Herramientas de Desarrollo
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code)
![Node.js](https://img.shields.io/badge/Node.js-16.x-339933?style=flat-square&logo=node.js)

---

## 📦 Instalación

### Prerrequisitos
- Node.js 16.x o superior
- Python 3.8 o superior
- MongoDB 4.4 o superior

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/el-mirador.git
cd el-mirador
```

### 2. Configurar Backend
```bash
cd Backend
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar Frontend
```bash
cd Frontend/elmirador
npm install
```

### 4. Configurar Base de Datos
```bash
# Asegúrate de que MongoDB esté ejecutándose
# Configura la conexión en Backend/config/config.py
```

---

## 🎯 Uso

### Iniciar Backend
```bash
cd Backend
python app.py
```

### Iniciar Frontend
```bash
cd Frontend/elmirador
npm run serve
```

### Acceder a la Aplicación
Abre tu navegador y ve a `http://localhost:8080`

---

## 🏗️ Estructura del Proyecto

```
el-mirador/
├── 📁 Backend/
│   ├── 🐍 app.py                 # Aplicación principal Flask
│   ├── 📁 config/
│   │   └── ⚙️ config.py         # Configuración de la aplicación
│   ├── 📁 models/
│   │   └── 🗃️ models.py         # Modelos de datos
│   ├── 📁 routes/
│   │   └── 🛣️ routes.py         # Rutas de la API
│   └── 📋 requirements.txt       # Dependencias Python
│
├── 📁 Frontend/
│   └── 📁 elmirador/
│       ├── 🎨 src/
│       │   ├── 📁 components/    # Componentes Vue.js
│       │   ├── 📁 views/         # Vistas de la aplicación
│       │   ├── 📁 assets/        # Recursos estáticos
│       │   └── 📁 router/        # Configuración de rutas
│       ├── 📦 package.json       # Dependencias Node.js
│       └── ⚙️ vue.config.js      # Configuración Vue.js
│
└── 📖 README.md                  # Este archivo
```

---

## 📊 Capturas de Pantalla

### 🏠 Dashboard Principal
![Dashboard](https://via.placeholder.com/800x400/4FC08D/FFFFFF?text=Dashboard+El+Mirador)

### 👥 Gestión de Residentes
![Residentes](https://via.placeholder.com/800x400/7952B3/FFFFFF?text=Gestión+de+Residentes)

### 💰 Gastos Comunes
![Gastos](https://via.placeholder.com/800x400/FF6384/FFFFFF?text=Gastos+Comunes)

### 📊 Estadísticas
![Estadísticas](https://via.placeholder.com/800x400/47A248/FFFFFF?text=Estadísticas)

---

## 🚀 Características Destacadas

### 🎨 Diseño Moderno
- Interfaz intuitiva y responsive
- Paleta de colores profesional
- Animaciones suaves y transiciones
- Diseño adaptativo para todos los dispositivos

### 📊 Dashboard Interactivo
- Métricas en tiempo real
- Gráficos dinámicos con Chart.js
- Filtros avanzados
- Exportación de datos

### 🔒 Seguridad
- Autenticación de usuarios
- Validación de datos
- Protección contra inyecciones
- Encriptación de información sensible

### 📱 Responsive Design
- Compatible con móviles
- Tablets y desktops
- Navegación táctil
- Interfaz adaptativa

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. 🍴 Haz un Fork del proyecto
2. 🌿 Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔄 Abre un Pull Request

### 📝 Guías de Contribución
- Mantén el código limpio y bien documentado
- Sigue las convenciones de nomenclatura
- Añade tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Autor

**Javier Cerna** - [@tjaacern](https://github.com/jaacern)

- 🌐 [Portfolio](https://javiercerna.dev)
- 📧 [Email](mailto:javiercernafr@gmail.com)
- 💼 [LinkedIn](https://[linkedin.com/in/tu-usuario](https://www.linkedin.com/in/javier-ignacio-cerna-chavez-32254030a/))

---

## 🙏 Agradecimientos

- [Vue.js](https://vuejs.org/) por el framework frontend
- [Flask](https://flask.palletsprojects.com/) por el framework backend
- [MongoDB](https://www.mongodb.com/) por la base de datos
- [Bootstrap](https://getbootstrap.com/) por el framework CSS
- [Chart.js](https://www.chartjs.org/) por las librerías de gráficos

---

<div align="center">

### ⭐ Si te gusta este proyecto, ¡dale una estrella!

[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/el-mirador?style=social)](https://github.com/tu-usuario/el-mirador/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/el-mirador?style=social)](https://github.com/tu-usuario/el-mirador/network)

---

**El Mirador** - Transformando la gestión residencial 🏢✨

</div> 
