<template>
  <div class="main-container fade-in">
    <!-- Header -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-chart-line"></i>
            Estadísticas del Edificio
          </h1>
          <div class="d-flex gap-2">
            <button class="btn btn-primary" @click="cargarEstadisticas">
              <i class="bi bi-arrow-clockwise me-2"></i>
              Actualizar Datos
            </button>
            <button class="btn btn-success" @click="exportarReporte">
              <i class="bi bi-download me-2"></i>
              Exportar Reporte
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tarjetas de estadísticas principales -->
    <div class="row mb-4">
      <div class="col-md-3">
        <div class="stats-card">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ estadisticas.totalResidentes || 0 }}</h3>
              <p>Total Residentes</p>
            </div>
            <i class="bi bi-people-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #10b981, #059669);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ estadisticas.totalPersonal || 0 }}</h3>
              <p>Personal Activo</p>
            </div>
            <i class="bi bi-person-badge-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ estadisticas.gastosPendientes || 0 }}</h3>
              <p>Gastos Pendientes</p>
            </div>
            <i class="bi bi-clock-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>${{ (estadisticas.totalRecaudado || 0).toLocaleString() }}</h3>
              <p>Total Recaudado</p>
            </div>
            <i class="bi bi-currency-dollar" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Gráficos y análisis -->
    <div class="row">
      <!-- Gráfico de residentes por departamento -->
      <div class="col-md-6 mb-4">
        <div class="card shadow-lg">
          <div class="card-header custom-header estadisticas">
            <h5 class="mb-0">
              <i class="bi bi-pie-chart me-2"></i>
              Distribución de Residentes
            </h5>
          </div>
          <div class="card-body">
            <div class="chart-container" style="position: relative; height: 300px;">
              <canvas id="residentesChart"></canvas>
              <div v-if="!residentes || residentes.length === 0" class="no-data-message">
                <i class="bi bi-pie-chart" style="font-size: 3rem; opacity: 0.3;"></i>
                <p class="text-muted mt-2">No hay datos de residentes disponibles</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Gráfico de gastos por mes -->
      <div class="col-md-6 mb-4">
        <div class="card shadow-lg">
          <div class="card-header custom-header estadisticas">
            <h5 class="mb-0">
              <i class="bi bi-bar-chart me-2"></i>
              Gastos por Mes
            </h5>
          </div>
          <div class="card-body">
            <div class="chart-container" style="position: relative; height: 300px;">
              <canvas id="gastosChart"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Tablas de información detallada -->
    <div class="row">
      <!-- Top 5 departamentos con más gastos -->
      <div class="col-md-6 mb-4">
        <div class="card shadow-lg">
          <div class="card-header custom-header estadisticas">
            <h5 class="mb-0">
              <i class="bi bi-trophy me-2"></i>
              Top 5 - Departamentos con Más Gastos
            </h5>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th>Departamento</th>
                    <th>Residente</th>
                    <th>Total Gastos</th>
                    <th>Estado</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(depto, index) in topDepartamentos" :key="index" class="fade-in">
                    <td>
                      <div class="d-flex align-items-center">
                        <div class="avatar me-2">
                          <i class="bi bi-building fs-6"></i>
                        </div>
                        <span class="fw-semibold">Depto. {{ depto.nro_departamento }}</span>
                      </div>
                    </td>
                    <td>{{ depto.residente }}</td>
                    <td>
                      <span class="fw-bold text-success">
                        ${{ depto.totalGastos.toLocaleString() }}
                      </span>
                    </td>
                    <td>
                      <span :class="depto.estado === 'Al día' ? 'estado-pagado' : 'estado-pendiente'">
                        {{ depto.estado }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <!-- Resumen de personal -->
      <div class="col-md-6 mb-4">
        <div class="card shadow-lg">
          <div class="card-header custom-header estadisticas">
            <h5 class="mb-0">
              <i class="bi bi-person-badge me-2"></i>
              Resumen del Personal
            </h5>
          </div>
          <div class="card-body">
            <div class="row g-3">
              <div class="col-6">
                <div class="text-center p-3 bg-light rounded">
                  <h4 class="text-primary mb-1">{{ estadisticas.personalActivo || 0 }}</h4>
                  <small class="text-muted">Personal Activo</small>
                </div>
              </div>
              <div class="col-6">
                <div class="text-center p-3 bg-light rounded">
                  <h4 class="text-warning mb-1">{{ estadisticas.personalInactivo || 0 }}</h4>
                  <small class="text-muted">Personal Inactivo</small>
                </div>
              </div>
              <div class="col-12">
                <h6 class="mb-3">Distribución por Cargo:</h6>
                <div v-for="cargo in distribucionCargos" :key="cargo.nombre" class="mb-2">
                  <div class="d-flex justify-content-between align-items-center">
                    <span>{{ cargo.nombre }}</span>
                    <span class="badge bg-primary">{{ cargo.cantidad }}</span>
                  </div>
                  <div class="progress mt-1" style="height: 6px;">
                    <div 
                      class="progress-bar" 
                      :style="{ width: (cargo.cantidad / estadisticas.totalPersonal * 100) + '%' }"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Información adicional -->
    <div class="row">
      <div class="col-md-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header recaudacion">
            <h5 class="mb-0">
              <i class="bi bi-info-circle me-2"></i>
              Información Adicional
            </h5>
          </div>
          <div class="card-body">
            <div class="row g-4">
              <div class="col-md-3">
                <div class="text-center">
                  <div class="avatar-large mb-3">
                    <i class="bi bi-calendar-check" style="font-size: 2rem;"></i>
                  </div>
                  <h5>Gastos Pagados</h5>
                  <p class="text-success fw-bold">{{ estadisticas.gastosPagados || 0 }}</p>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center">
                  <div class="avatar-large mb-3" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
                    <i class="bi bi-clock" style="font-size: 2rem;"></i>
                  </div>
                  <h5>Gastos Pendientes</h5>
                  <p class="text-warning fw-bold">{{ estadisticas.gastosPendientes || 0 }}</p>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center">
                  <div class="avatar-large mb-3" style="background: linear-gradient(135deg, #10b981, #059669);">
                    <i class="bi bi-percent" style="font-size: 2rem;"></i>
                  </div>
                  <h5>Porcentaje de Pago</h5>
                  <p class="text-success fw-bold">{{ porcentajePago }}%</p>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center">
                  <div class="avatar-large mb-3" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
                    <i class="bi bi-graph-up" style="font-size: 2rem;"></i>
                  </div>
                  <h5>Promedio por Residente</h5>
                  <p class="text-info fw-bold">${{ promedioPorResidente.toLocaleString() }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';

// Registrar todos los componentes necesarios
Chart.register(...registerables);

export default {
  name: 'EstadisticasView',
  data() {
    return {
      estadisticas: {
        totalResidentes: 0,
        totalPersonal: 0,
        personalActivo: 0,
        personalInactivo: 0,
        gastosPagados: 0,
        gastosPendientes: 0,
        totalRecaudado: 0
      },
      residentes: [],
      personal: [],
      gastos: [],
      topDepartamentos: [],
      distribucionCargos: []
    };
  },
  computed: {
    porcentajePago() {
      const total = this.estadisticas.gastosPagados + this.estadisticas.gastosPendientes;
      if (total === 0) return 0;
      return Math.round((this.estadisticas.gastosPagados / total) * 100);
    },
    promedioPorResidente() {
      if (this.estadisticas.totalResidentes === 0) return 0;
      return Math.round(this.estadisticas.totalRecaudado / this.estadisticas.totalResidentes);
    }
  },
  mounted() {
    this.cargarEstadisticas();
  },
  beforeUnmount() {
    // Limpiar gráficos al desmontar el componente
    if (this.residentesChart) {
      this.residentesChart.destroy();
    }
    if (this.gastosChart) {
      this.gastosChart.destroy();
    }
  },
  methods: {
    async cargarEstadisticas() {
      try {
        const [residentesRes, personalRes, gastosRes] = await Promise.all([
          axios.get('http://localhost:5000/residentes'),
          axios.get('http://localhost:5000/personal'),
          axios.get('http://localhost:5000/gastos-comunes')
        ]);

        this.residentes = residentesRes.data;
        this.personal = personalRes.data;
        this.gastos = gastosRes.data;

        this.calcularEstadisticas();
        this.generarTopDepartamentos();
        this.generarDistribucionCargos();
        
        // Pequeño retraso para asegurar que el DOM esté listo
        this.$nextTick(() => {
          setTimeout(() => {
            this.crearGraficos();
          }, 100);
        });

      } catch (error) {
        console.error('Error al cargar estadísticas:', error);
        this.mostrarAlerta('Error al cargar estadísticas', 'danger');
      }
    },

    calcularEstadisticas() {
      this.estadisticas = {
        totalResidentes: this.residentes.length,
        totalPersonal: this.personal.length,
        personalActivo: this.personal.filter(p => p.Estado === 'Activo').length,
        personalInactivo: this.personal.filter(p => p.Estado === 'Inactivo').length,
        gastosPagados: this.gastos.filter(g => g.estado_pago).length,
        gastosPendientes: this.gastos.filter(g => !g.estado_pago).length,
        totalRecaudado: this.gastos
          .filter(g => g.estado_pago)
          .reduce((total, gasto) => total + gasto.valor, 0)
      };
    },

    generarTopDepartamentos() {
      const gastosPorDepartamento = {};
      
      this.gastos.forEach(gasto => {
        if (!gastosPorDepartamento[gasto.nro_departamento]) {
          gastosPorDepartamento[gasto.nro_departamento] = {
            totalGastos: 0,
            gastosPendientes: 0,
            residente: this.obtenerResidente(gasto.nro_departamento)
          };
        }
        gastosPorDepartamento[gasto.nro_departamento].totalGastos += gasto.valor;
        if (!gasto.estado_pago) {
          gastosPorDepartamento[gasto.nro_departamento].gastosPendientes++;
        }
      });

      this.topDepartamentos = Object.entries(gastosPorDepartamento)
        .map(([nro_departamento, datos]) => ({
          nro_departamento,
          residente: datos.residente,
          totalGastos: datos.totalGastos,
          estado: datos.gastosPendientes > 0 ? 'Pendiente' : 'Al día'
        }))
        .sort((a, b) => b.totalGastos - a.totalGastos)
        .slice(0, 5);
    },

    generarDistribucionCargos() {
      const cargos = {};
      this.personal.forEach(p => {
        if (p.Estado === 'Activo') {
          cargos[p.Cargo] = (cargos[p.Cargo] || 0) + 1;
        }
      });

      this.distribucionCargos = Object.entries(cargos)
        .map(([nombre, cantidad]) => ({ nombre, cantidad }))
        .sort((a, b) => b.cantidad - a.cantidad);
    },

    obtenerResidente(departamento) {
      const residente = this.residentes.find(r => r.nro_departamento === departamento);
      return residente ? `${residente.Nombre} ${residente.ApePat}` : 'Sin asignar';
    },

    crearGraficos() {
      // Gráfico de residentes por departamento
      this.crearGraficoResidentes();
      
      // Gráfico de gastos por mes
      this.crearGraficoGastos();
    },

    crearGraficoResidentes() {
      const ctx = document.getElementById('residentesChart');
      if (!ctx) {
        console.error('No se encontró el elemento canvas para el gráfico de residentes');
        return;
      }

      // Destruir gráfico existente si existe
      if (this.residentesChart) {
        this.residentesChart.destroy();
      }

      // Verificar si hay datos
      if (!this.residentes || this.residentes.length === 0) {
        console.warn('No hay datos de residentes para mostrar en el gráfico');
        return;
      }

      const departamentos = [...new Set(this.residentes.map(r => r.nro_departamento))];
      const datos = departamentos.map(depto => 
        this.residentes.filter(r => r.nro_departamento === depto).length
      );

      // Verificar si hay datos válidos
      if (datos.length === 0 || datos.every(d => d === 0)) {
        console.warn('No hay datos válidos para el gráfico de residentes');
        return;
      }

      try {
        this.residentesChart = new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: departamentos.map(d => `Depto. ${d}`),
            datasets: [{
              data: datos,
              backgroundColor: [
                '#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
                '#06b6d4', '#84cc16', '#f97316', '#ec4899', '#6366f1'
              ],
              borderWidth: 2,
              borderColor: '#ffffff'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'bottom',
                labels: {
                  padding: 10,
                  font: {
                    size: 12
                  },
                  usePointStyle: true
                }
              },
              tooltip: {
                callbacks: {
                  label: function(context) {
                    const label = context.label || '';
                    const value = context.parsed;
                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                    const percentage = ((value / total) * 100).toFixed(1);
                    return `${label}: ${value} residentes (${percentage}%)`;
                  }
                }
              }
            }
          }
        });
      } catch (error) {
        console.error('Error al crear el gráfico de residentes:', error);
      }
    },

    crearGraficoGastos() {
      const ctx = document.getElementById('gastosChart');
      if (!ctx) {
        console.error('No se encontró el elemento canvas para el gráfico de gastos');
        return;
      }

      // Destruir gráfico existente si existe
      if (this.gastosChart) {
        this.gastosChart.destroy();
      }

      // Verificar si hay datos
      if (!this.gastos || this.gastos.length === 0) {
        console.warn('No hay datos de gastos para mostrar en el gráfico');
        return;
      }

      const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
      
      const gastosPorMes = meses.map(mes => {
        const gastosMes = this.gastos.filter(g => g.mes === mes);
        return gastosMes.reduce((total, gasto) => total + gasto.valor, 0);
      });

      // Verificar si hay datos válidos
      if (gastosPorMes.every(g => g === 0)) {
        console.warn('No hay datos válidos para el gráfico de gastos');
        return;
      }

      try {
        this.gastosChart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: meses,
            datasets: [{
              label: 'Gastos por Mes',
              data: gastosPorMes,
              backgroundColor: 'rgba(59, 130, 246, 0.8)',
              borderColor: 'rgba(59, 130, 246, 1)',
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            scales: {
              y: {
                beginAtZero: true,
                ticks: {
                  callback: function(value) {
                    return '$' + value.toLocaleString();
                  }
                }
              }
            },
            plugins: {
              legend: {
                display: false
              },
              tooltip: {
                callbacks: {
                  label: function(context) {
                    return 'Gastos: $' + context.parsed.y.toLocaleString();
                  }
                }
              }
            }
          }
        });
      } catch (error) {
        console.error('Error al crear el gráfico de gastos:', error);
      }
    },

    exportarReporte() {
      const reporte = {
        fecha: new Date().toISOString(),
        estadisticas: this.estadisticas,
        topDepartamentos: this.topDepartamentos,
        distribucionCargos: this.distribucionCargos
      };

      const jsonData = JSON.stringify(reporte, null, 2);
      const blob = new Blob([jsonData], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `reporte-estadisticas-${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);

      this.$alert.mostrarExito('Reporte exportado exitosamente');
    },

    mostrarAlerta(mensaje, tipo) {
      const alerta = document.createElement('div');
      alerta.className = `alert alert-${tipo} alert-dismissible fade show position-fixed`;
      alerta.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
      alerta.innerHTML = `
        ${mensaje}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      `;
      document.body.appendChild(alerta);
      
      setTimeout(() => {
        if (alerta.parentNode) {
          alerta.parentNode.removeChild(alerta);
        }
      }, 3000);
    },
  },
};
</script>

<style scoped>
.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
}

.avatar-large {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  margin: 0 auto;
}

.table tbody tr {
  transition: all 0.2s ease;
}

.table tbody tr:hover {
  background-color: rgba(37, 99, 235, 0.05);
  transform: scale(1.01);
}

.stats-card {
  transition: transform 0.2s ease;
}

.stats-card:hover {
  transform: translateY(-5px);
}

.progress {
  background-color: #e2e8f0;
}

.progress-bar {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
}

.no-data-message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  z-index: 1;
}

.chart-container {
  position: relative;
}
</style>