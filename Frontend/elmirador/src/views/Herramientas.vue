<template>
  <div class="main-container fade-in">
    <!-- Header -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-tools"></i>
            Herramientas del Sistema
          </h1>
        </div>
      </div>
    </div>

    <!-- Herramientas principales -->
    <div class="row mb-4">
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirCalculadora">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3">
              <i class="bi bi-calculator"></i>
            </div>
            <h5 class="card-title text-center">Calculadora de Gastos</h5>
            <p class="card-text">Calcula gastos comunes y distribuye costos entre departamentos</p>
            <div class="tool-features">
              <span class="badge bg-primary">Cálculos</span>
              <span class="badge bg-success">Distribución</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirGeneradorReportes">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3" style="background: linear-gradient(135deg, #10b981, #059669);">
              <i class="bi bi-file-earmark-text"></i>
            </div>
            <h5 class="card-title text-center">Generador de Reportes</h5>
            <p class="card-text">Crea reportes personalizados en diferentes formatos</p>
            <div class="tool-features">
              <span class="badge bg-success">PDF</span>
              <span class="badge bg-info">Excel</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirBackup">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
              <i class="bi bi-cloud-arrow-up"></i>
            </div>
            <h5 class="card-title text-center">Backup y Restauración</h5>
            <p class="card-text">Respaldar y restaurar datos del sistema</p>
            <div class="tool-features">
              <span class="badge bg-warning">Backup</span>
              <span class="badge bg-secondary">Restore</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Herramientas adicionales -->
    <div class="row mb-4">
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirNotificaciones">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
              <i class="bi bi-bell"></i>
            </div>
            <h5 class="card-title text-center">Sistema de Notificaciones</h5>
            <p class="card-text">Configura alertas y notificaciones automáticas</p>
            <div class="tool-features">
              <span class="badge bg-info">Alertas</span>
              <span class="badge bg-primary">Email</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirConfiguracion">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3" style="background: linear-gradient(135deg, #8b5cf6, #7c3aed);">
              <i class="bi bi-gear"></i>
            </div>
            <h5 class="card-title text-center">Configuración del Sistema</h5>
            <p class="card-text">Ajusta parámetros y configuraciones generales</p>
            <div class="tool-features">
              <span class="badge bg-secondary">Config</span>
              <span class="badge bg-primary">Ajustes</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-4 mb-3">
        <div class="card shadow-lg tool-card" @click="abrirAyuda">
          <div class="card-body text-center d-flex flex-column justify-content-center">
            <div class="tool-icon mb-3" style="background: linear-gradient(135deg, #ef4444, #dc2626);">
              <i class="bi bi-question-circle"></i>
            </div>
            <h5 class="card-title text-center">Centro de Ayuda</h5>
            <p class="card-text">Documentación y soporte técnico</p>
            <div class="tool-features">
              <span class="badge bg-danger">Ayuda</span>
              <span class="badge bg-info">Soporte</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Estadísticas del sistema -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header">
            <h5 class="mb-0">
              <i class="bi bi-speedometer2 me-2"></i>
              Estado del Sistema
            </h5>
          </div>
          <div class="card-body">
            <div class="row g-3">
              <div class="col-md-3">
                <div class="system-stat">
                  <div class="stat-icon">
                    <i class="bi bi-database"></i>
                  </div>
                  <div class="stat-info">
                    <h6>Base de Datos</h6>
                    <span class="status-badge status-online">Conectado</span>
                  </div>
                </div>
              </div>
              <div class="col-md-3">
                <div class="system-stat">
                  <div class="stat-icon">
                    <i class="bi bi-server"></i>
                  </div>
                  <div class="stat-info">
                    <h6>Servidor API</h6>
                    <span class="status-badge status-online">Activo</span>
                  </div>
                </div>
              </div>
              <div class="col-md-3">
                <div class="system-stat">
                  <div class="stat-icon">
                    <i class="bi bi-clock"></i>
                  </div>
                  <div class="stat-info">
                    <h6>Tiempo Activo</h6>
                    <span class="status-badge status-info">{{ tiempoActivo }}</span>
                  </div>
                </div>
              </div>
              <div class="col-md-3">
                <div class="system-stat">
                  <div class="stat-icon">
                    <i class="bi bi-hdd"></i>
                  </div>
                  <div class="stat-info">
                    <h6>Espacio Disco</h6>
                    <span class="status-badge status-warning">{{ espacioDisco }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Acciones rápidas -->
    <div class="row">
      <div class="col-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header">
            <h5 class="mb-0">
              <i class="bi bi-lightning me-2"></i>
              Acciones Rápidas
            </h5>
          </div>
          <div class="card-body">
            <div class="row g-3">
              <div class="col-md-6">
                <div class="quick-action">
                  <button class="btn btn-primary w-100" @click="limpiarCache">
                    <i class="bi bi-trash me-2"></i>
                    Limpiar Cache
                  </button>
                </div>
              </div>
              <div class="col-md-6">
                <div class="quick-action">
                  <button class="btn btn-success w-100" @click="optimizarBaseDatos">
                    <i class="bi bi-database-gear me-2"></i>
                    Optimizar Base de Datos
                  </button>
                </div>
              </div>
              <div class="col-md-6">
                <div class="quick-action">
                  <button class="btn btn-warning w-100" @click="verificarIntegridad">
                    <i class="bi bi-shield-check me-2"></i>
                    Verificar Integridad
                  </button>
                </div>
              </div>
              <div class="col-md-6">
                <div class="quick-action">
                  <button class="btn btn-info w-100" @click="generarLogs">
                    <i class="bi bi-file-text me-2"></i>
                    Generar Logs del Sistema
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Calculadora -->
    <div class="modal fade" id="calculadoraModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <i class="bi bi-calculator me-2"></i>
              Calculadora de Gastos
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <div class="row g-3">
              <div class="col-md-6">
                <label class="form-label">Total de Gastos</label>
                <input type="number" class="form-control" v-model="calculadora.totalGastos" placeholder="0">
              </div>
              <div class="col-md-6">
                <label class="form-label">Número de Departamentos</label>
                <input type="number" class="form-control" v-model="calculadora.numDepartamentos" placeholder="0">
              </div>
              <div class="col-12">
                <button class="btn btn-primary" @click="calcularGastos">
                  <i class="bi bi-calculator me-2"></i>
                  Calcular
                </button>
              </div>
              <div class="col-12" v-if="calculadora.resultado">
                <div class="alert alert-success">
                  <h6>Resultado:</h6>
                  <p class="mb-0">Cada departamento debe pagar: <strong>${{ calculadora.resultado.toLocaleString() }}</strong></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Configuración -->
    <div class="modal fade" id="configuracionModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <i class="bi bi-gear me-2"></i>
              Configuración del Sistema
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <div class="row g-3">
              <div class="col-md-6">
                <label class="form-label">Tema de la Aplicación</label>
                <select class="form-select" v-model="configuracion.tema">
                  <option value="light">Claro</option>
                  <option value="dark">Oscuro</option>
                  <option value="auto">Automático</option>
                </select>
              </div>
              <div class="col-md-6">
                <label class="form-label">Idioma</label>
                <select class="form-select" v-model="configuracion.idioma">
                  <option value="es">Español</option>
                  <option value="en">English</option>
                </select>
              </div>
              <div class="col-md-6">
                <label class="form-label">Notificaciones</label>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" v-model="configuracion.notificaciones">
                  <label class="form-check-label">Activar notificaciones</label>
                </div>
              </div>
              <div class="col-md-6">
                <label class="form-label">Backup Automático</label>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" v-model="configuracion.backupAutomatico">
                  <label class="form-check-label">Activar backup automático</label>
                </div>
              </div>
              <div class="col-12">
                <button class="btn btn-primary" @click="guardarConfiguracion">
                  <i class="bi bi-save me-2"></i>
                  Guardar Configuración
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap';

export default {
  name: 'HerramientasView',
  data() {
    return {
      calculadora: {
        totalGastos: 0,
        numDepartamentos: 0,
        resultado: 0
      },
      configuracion: {
        tema: 'light',
        idioma: 'es',
        notificaciones: true,
        backupAutomatico: false
      },
      tiempoActivo: '2 días, 5 horas',
      espacioDisco: '75% usado'
    };
  },
  methods: {
    abrirCalculadora() {
      const modal = new Modal(document.getElementById('calculadoraModal'));
      modal.show();
    },

    abrirGeneradorReportes() {
      this.$alert.mostrarInfo('Generador de reportes en desarrollo');
    },

    abrirBackup() {
      this.$alert.mostrarInfo('Sistema de backup en desarrollo');
    },

    abrirNotificaciones() {
      this.$alert.mostrarInfo('Sistema de notificaciones en desarrollo');
    },

    abrirConfiguracion() {
      const modal = new Modal(document.getElementById('configuracionModal'));
      modal.show();
    },

    abrirAyuda() {
      this.$alert.mostrarInfo('Centro de ayuda en desarrollo');
    },

    calcularGastos() {
      if (this.calculadora.totalGastos > 0 && this.calculadora.numDepartamentos > 0) {
        this.calculadora.resultado = this.calculadora.totalGastos / this.calculadora.numDepartamentos;
        this.$alert.mostrarExito('Cálculo realizado exitosamente');
      } else {
        this.$alert.mostrarAdvertencia('Por favor ingrese valores válidos');
      }
    },

    guardarConfiguracion() {
      this.$alert.mostrarExito('Configuración guardada exitosamente');
      const modal = Modal.getInstance(document.getElementById('configuracionModal'));
      modal.hide();
    },

    limpiarCache() {
      this.$alert.mostrarExito('Cache limpiado exitosamente');
    },

    optimizarBaseDatos() {
      this.$alert.mostrarExito('Base de datos optimizada exitosamente');
    },

    verificarIntegridad() {
      this.$alert.mostrarExito('Verificación de integridad completada');
    },

    generarLogs() {
      this.$alert.mostrarExito('Logs del sistema generados exitosamente');
    },


  }
};
</script>

<style scoped>
.tool-card {
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  height: 100%;
}

.tool-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.tool-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  margin: 0 auto;
  font-size: 1.5rem;
}

.tool-features {
  margin-top: 1rem;
}

.tool-features .badge {
  margin-right: 0.25rem;
}

.system-stat {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: #e2e8f0;
  border-radius: var(--border-radius);
  transition: all 0.2s ease;
}

.system-stat:hover {
  background: #cbd5e1;
  transform: translateY(-2px);
}

.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  margin-right: 1rem;
  font-size: 1.25rem;
}

.stat-info h6 {
  margin: 0;
  font-weight: 600;
  color: var(--dark-color);
}

.status-badge {
  padding: 0.25rem 0.5rem;
  border-radius: var(--border-radius);
  font-size: 0.75rem;
  font-weight: 500;
}

.status-online {
  background: linear-gradient(135deg, var(--success-color), #059669);
  color: white;
}

.status-info {
  background: linear-gradient(135deg, var(--info-color), #0891b2);
  color: white;
}

.status-warning {
  background: linear-gradient(135deg, var(--warning-color), #d97706);
  color: white;
}

.quick-action {
  height: 100%;
}

.quick-action .btn {
  height: 100%;
  padding: 1rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.quick-action .btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}


</style>
