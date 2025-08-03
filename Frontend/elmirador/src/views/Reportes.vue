<template>
  <div class="main-container fade-in">
    <!-- Header -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-file-alt"></i>
            Generación de Reportes
          </h1>
          <div class="d-flex gap-2">
            <button class="btn btn-primary" @click="generarReporteCompleto">
              <i class="bi bi-file-earmark-pdf me-2"></i>
              Reporte Completo
            </button>
            <button class="btn btn-success" @click="exportarDatos">
              <i class="bi bi-download me-2"></i>
              Exportar Datos
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tarjetas de reportes disponibles -->
    <div class="row mb-4">
      <div class="col-md-3">
        <div class="card shadow-lg report-card" @click="generarReporteResidentes">
          <div class="card-body text-center">
            <div class="report-icon mb-3">
              <i class="bi bi-people-fill"></i>
            </div>
            <h5 class="card-title">Reporte de Residentes</h5>
            <p class="card-text">Lista completa de residentes con información detallada</p>
            <div class="report-stats">
              <span class="badge bg-primary">{{ totalResidentes }} residentes</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-3">
        <div class="card shadow-lg report-card" @click="generarReportePersonal">
          <div class="card-body text-center">
            <div class="report-icon mb-3" style="background: linear-gradient(135deg, #10b981, #059669);">
              <i class="bi bi-person-badge-fill"></i>
            </div>
            <h5 class="card-title">Reporte de Personal</h5>
            <p class="card-text">Información del personal activo e inactivo</p>
            <div class="report-stats">
              <span class="badge bg-success">{{ totalPersonal }} personal</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-3">
        <div class="card shadow-lg report-card" @click="generarReporteGastos">
          <div class="card-body text-center">
            <div class="report-icon mb-3" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
              <i class="bi bi-cash-coin"></i>
            </div>
            <h5 class="card-title">Reporte de Gastos</h5>
            <p class="card-text">Estado de pagos y gastos pendientes</p>
            <div class="report-stats">
              <span class="badge bg-warning">{{ gastosPendientes }} pendientes</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="col-md-3">
        <div class="card shadow-lg report-card" @click="generarReporteFinanciero">
          <div class="card-body text-center">
            <div class="report-icon mb-3" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
              <i class="bi bi-graph-up"></i>
            </div>
            <h5 class="card-title">Reporte Financiero</h5>
            <p class="card-text">Análisis financiero y estadísticas de recaudación</p>
            <div class="report-stats">
              <span class="badge bg-info">${{ totalRecaudado.toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Filtros para reportes -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header reportes">
            <h5 class="mb-0">
              <i class="bi bi-funnel me-2"></i>
              Filtros de Reporte
            </h5>
          </div>
          <div class="card-body">
            <div class="row g-3">
              <div class="col-md-3">
                <label class="form-label">
                  <i class="bi bi-calendar me-1"></i>Fecha Desde
                </label>
                <input type="date" class="form-control" v-model="filtros.fechaDesde">
              </div>
              <div class="col-md-3">
                <label class="form-label">
                  <i class="bi bi-calendar me-1"></i>Fecha Hasta
                </label>
                <input type="date" class="form-control" v-model="filtros.fechaHasta">
              </div>
              <div class="col-md-3">
                <label class="form-label">
                  <i class="bi bi-building me-1"></i>Departamento
                </label>
                <select class="form-select" v-model="filtros.departamento">
                  <option value="">Todos los departamentos</option>
                  <option v-for="depto in departamentos" :key="depto" :value="depto">
                    Departamento {{ depto }}
                  </option>
                </select>
              </div>
              <div class="col-md-3">
                <label class="form-label">
                  <i class="bi bi-toggle-on me-1"></i>Estado
                </label>
                <select class="form-select" v-model="filtros.estado">
                  <option value="">Todos</option>
                  <option value="activo">Activo</option>
                  <option value="inactivo">Inactivo</option>
                  <option value="pagado">Pagado</option>
                  <option value="pendiente">Pendiente</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Vista previa del reporte -->
    <div class="row" v-if="reporteGenerado">
      <div class="col-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header reportes d-flex justify-content-between align-items-center">
            <h5 class="mb-0">
              <i class="bi bi-eye me-2"></i>
              Vista Previa del Reporte
            </h5>
            <div class="d-flex gap-2">
              <button class="btn btn-outline-light btn-sm" @click="descargarReporte">
                <i class="bi bi-download me-1"></i>Descargar
              </button>
              <button class="btn btn-outline-light btn-sm" @click="imprimirReporte">
                <i class="bi bi-printer me-1"></i>Imprimir
              </button>
            </div>
          </div>
          <div class="card-body">
            <div class="reporte-preview">
              <div class="reporte-header mb-4">
                <div class="row align-items-center">
                  <div class="col-md-8">
                    <h2 class="mb-1">Reporte de {{ reporteActual.titulo }}</h2>
                    <p class="text-muted mb-0">Generado el {{ fechaActual }}</p>
                    <p class="text-muted mb-0">{{ reporteActual.descripcion }}</p>
                  </div>
                  <div class="col-md-4 text-end">
                    <div class="reporte-stats-summary">
                      <div class="stat-item">
                        <span class="stat-label">Total Registros:</span>
                        <span class="stat-value">{{ reporteActual.datos.length }}</span>
                      </div>
                      <div class="stat-item" v-if="reporteActual.totalFinanciero">
                        <span class="stat-label">Total Financiero:</span>
                        <span class="stat-value">${{ reporteActual.totalFinanciero.toLocaleString() }}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tabla del reporte -->
              <div class="table-responsive">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th v-for="columna in reporteActual.columnas" :key="columna">
                        {{ columna }}
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in reporteActual.datos" :key="index">
                      <td v-for="columna in reporteActual.columnas" :key="columna">
                        <span v-if="columna === 'Estado'" :class="getEstadoClass(item[columna])">
                          {{ item[columna] }}
                        </span>
                        <span v-else-if="columna === 'Valor'" class="fw-bold text-success">
                          ${{ item[columna].toLocaleString() }}
                        </span>
                        <span v-else>
                          {{ item[columna] }}
                        </span>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Resumen del reporte -->
              <div class="reporte-footer mt-4">
                <div class="row">
                  <div class="col-md-6">
                    <h6>Resumen:</h6>
                    <ul class="list-unstyled">
                      <li v-for="resumen in reporteActual.resumen" :key="resumen.label">
                        <strong>{{ resumen.label }}:</strong> {{ resumen.valor }}
                      </li>
                    </ul>
                  </div>
                  <div class="col-md-6">
                    <h6>Filtros Aplicados:</h6>
                    <ul class="list-unstyled">
                      <li v-for="filtro in filtrosAplicados" :key="filtro.label">
                        <strong>{{ filtro.label }}:</strong> {{ filtro.valor }}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Historial de reportes -->
    <div class="row">
      <div class="col-12">
        <div class="card shadow-lg">
          <div class="card-header custom-header recaudacion">
            <h5 class="mb-0">
              <i class="bi bi-clock-history me-2"></i>
              Historial de Reportes
            </h5>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th>Fecha</th>
                    <th>Tipo de Reporte</th>
                    <th>Filtros</th>
                    <th>Registros</th>
                    <th>Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="reporte in historialReportes" :key="reporte.id" class="fade-in">
                    <td>{{ formatearFecha(reporte.fecha) }}</td>
                    <td>
                      <span class="badge bg-primary">{{ reporte.tipo }}</span>
                    </td>
                    <td>{{ reporte.filtros }}</td>
                    <td>{{ reporte.registros }} registros</td>
                    <td>
                      <div class="btn-group btn-group-sm">
                        <button class="btn btn-outline-primary" @click="verReporte(reporte)">
                          <i class="bi bi-eye"></i>
                        </button>
                        <button class="btn btn-outline-success" @click="descargarReporte(reporte)">
                          <i class="bi bi-download"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                  <tr v-if="historialReportes.length === 0">
                    <td colspan="5" class="text-center py-4">
                      <div class="text-muted">
                        <i class="bi bi-file-earmark-text fs-1 d-block mb-3"></i>
                        <h5>No hay reportes generados</h5>
                        <p>Genera tu primer reporte usando las opciones arriba</p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ReportesView',
  data() {
    return {
      filtros: {
        fechaDesde: '',
        fechaHasta: '',
        departamento: '',
        estado: ''
      },
      reporteGenerado: false,
      reporteActual: {
        titulo: '',
        descripcion: '',
        datos: [],
        columnas: [],
        resumen: [],
        totalFinanciero: 0
      },
      historialReportes: [],
      departamentos: [],
      residentes: [],
      personal: [],
      gastos: []
    };
  },
  computed: {
    totalResidentes() {
      return this.residentes.length;
    },
    totalPersonal() {
      return this.personal.length;
    },
    gastosPendientes() {
      return this.gastos.filter(g => !g.estado_pago).length;
    },
    totalRecaudado() {
      return this.gastos
        .filter(g => g.estado_pago)
        .reduce((total, gasto) => total + gasto.valor, 0);
    },
    fechaActual() {
      return new Date().toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    },
    filtrosAplicados() {
      const filtros = [];
      if (this.filtros.fechaDesde) {
        filtros.push({ label: 'Fecha Desde', valor: this.filtros.fechaDesde });
      }
      if (this.filtros.fechaHasta) {
        filtros.push({ label: 'Fecha Hasta', valor: this.filtros.fechaHasta });
      }
      if (this.filtros.departamento) {
        filtros.push({ label: 'Departamento', valor: this.filtros.departamento });
      }
      if (this.filtros.estado) {
        filtros.push({ label: 'Estado', valor: this.filtros.estado });
      }
      return filtros;
    },
    porcentajePago() {
      const total = this.gastos.length;
      if (total === 0) return 0;
      return Math.round((this.gastos.filter(g => g.estado_pago).length / total) * 100);
    },
    promedioPorResidente() {
      if (this.residentes.length === 0) return 0;
      return Math.round(this.totalRecaudado / this.residentes.length);
    }
  },
  mounted() {
    this.cargarDatos();
  },
  methods: {
    async cargarDatos() {
      try {
        const [residentesRes, personalRes, gastosRes] = await Promise.all([
          axios.get('http://localhost:5000/residentes'),
          axios.get('http://localhost:5000/personal'),
          axios.get('http://localhost:5000/gastos-comunes')
        ]);

        this.residentes = residentesRes.data;
        this.personal = personalRes.data;
        this.gastos = gastosRes.data;

        // Generar lista de departamentos
        this.departamentos = [...new Set(this.residentes.map(r => r.nro_departamento))];
              } catch (error) {
          console.error('Error al cargar datos:', error);
          this.$alert.mostrarError('Error al cargar datos');
        }
    },

    generarReporteResidentes() {
      this.reporteActual = {
        titulo: 'Residentes',
        descripcion: 'Lista completa de residentes del edificio',
        columnas: ['Nombre', 'Rut', 'Email', 'Departamento', 'Teléfono'],
        datos: this.residentes.map(r => ({
          Nombre: `${r.Nombre} ${r.ApePat} ${r.ApeMat}`,
          Rut: r.RutArre,
          Email: r.Email,
          Departamento: r.nro_departamento,
          Teléfono: r.Fono1 || 'No registrado'
        })),
        resumen: [
          { label: 'Total Residentes', valor: this.residentes.length },
          { label: 'Departamentos Ocupados', valor: this.departamentos.length },
          { label: 'Con Email', valor: this.residentes.filter(r => r.Email).length },
          { label: 'Con Teléfono', valor: this.residentes.filter(r => r.Fono1).length }
        ]
      };
      this.reporteGenerado = true;
      this.agregarAlHistorial('Residentes');
    },

    generarReportePersonal() {
      this.reporteActual = {
        titulo: 'Personal',
        descripcion: 'Información del personal del edificio',
        columnas: ['Nombre', 'Rut', 'Cargo', 'Email', 'Estado'],
        datos: this.personal.map(p => ({
          Nombre: `${p.Nombre} ${p.ApePat} ${p.ApeMat}`,
          Rut: p.RutPersonal,
          Cargo: p.Cargo,
          Email: p.Email,
          Estado: p.Estado
        })),
        resumen: [
          { label: 'Total Personal', valor: this.personal.length },
          { label: 'Personal Activo', valor: this.personal.filter(p => p.Estado === 'Activo').length },
          { label: 'Personal Inactivo', valor: this.personal.filter(p => p.Estado === 'Inactivo').length },
          { label: 'Cargos Diferentes', valor: [...new Set(this.personal.map(p => p.Cargo))].length }
        ]
      };
      this.reporteGenerado = true;
      this.agregarAlHistorial('Personal');
    },

    generarReporteGastos() {
      this.reporteActual = {
        titulo: 'Gastos Comunes',
        descripcion: 'Estado de gastos comunes y pagos',
        columnas: ['Departamento', 'Mes/Año', 'Valor', 'Estado'],
        datos: this.gastos.map(g => ({
          Departamento: g.nro_departamento,
          'Mes/Año': `${g.mes} ${g.anio}`,
          Valor: g.valor,
          Estado: g.estado_pago ? 'Pagado' : 'Pendiente'
        })),
        totalFinanciero: this.gastos.reduce((total, g) => total + g.valor, 0),
        resumen: [
          { label: 'Total Gastos', valor: this.gastos.length },
          { label: 'Gastos Pagados', valor: this.gastos.filter(g => g.estado_pago).length },
          { label: 'Gastos Pendientes', valor: this.gastos.filter(g => !g.estado_pago).length },
          { label: 'Total Recaudado', valor: `$${this.totalRecaudado.toLocaleString()}` }
        ]
      };
      this.reporteGenerado = true;
      this.agregarAlHistorial('Gastos');
    },

    generarReporteFinanciero() {
      const gastosPorMes = {};
      this.gastos.forEach(g => {
        const key = `${g.mes} ${g.anio}`;
        if (!gastosPorMes[key]) {
          gastosPorMes[key] = { total: 0, pagados: 0, pendientes: 0 };
        }
        gastosPorMes[key].total += g.valor;
        if (g.estado_pago) {
          gastosPorMes[key].pagados += g.valor;
        } else {
          gastosPorMes[key].pendientes += g.valor;
        }
      });

      this.reporteActual = {
        titulo: 'Reporte Financiero',
        descripcion: 'Análisis financiero detallado',
        columnas: ['Período', 'Total', 'Pagado', 'Pendiente', 'Porcentaje Pago'],
        datos: Object.entries(gastosPorMes).map(([periodo, datos]) => ({
          Período: periodo,
          Total: datos.total,
          Pagado: datos.pagados,
          Pendiente: datos.pendientes,
          'Porcentaje Pago': `${Math.round((datos.pagados / datos.total) * 100)}%`
        })),
        totalFinanciero: this.totalRecaudado,
        resumen: [
          { label: 'Total Recaudado', valor: `$${this.totalRecaudado.toLocaleString()}` },
          { label: 'Gastos Pendientes', valor: `$${(this.gastos.filter(g => !g.estado_pago).reduce((total, g) => total + g.valor, 0)).toLocaleString()}` },
          { label: 'Porcentaje de Pago', valor: `${this.porcentajePago}%` },
          { label: 'Promedio por Residente', valor: `$${this.promedioPorResidente.toLocaleString()}` }
        ]
      };
      this.reporteGenerado = true;
      this.agregarAlHistorial('Financiero');
    },

    generarReporteCompleto() {
      // Generar un reporte que combine todos los datos
      this.reporteActual = {
        titulo: 'Reporte Completo del Edificio',
        descripcion: 'Resumen completo de residentes, personal y finanzas',
        columnas: ['Categoría', 'Total', 'Activos', 'Inactivos', 'Porcentaje'],
        datos: [
          {
            Categoría: 'Residentes',
            Total: this.residentes.length,
            Activos: this.residentes.length,
            Inactivos: 0,
            Porcentaje: '100%'
          },
          {
            Categoría: 'Personal',
            Total: this.personal.length,
            Activos: this.personal.filter(p => p.Estado === 'Activo').length,
            Inactivos: this.personal.filter(p => p.Estado === 'Inactivo').length,
            Porcentaje: `${Math.round((this.personal.filter(p => p.Estado === 'Activo').length / this.personal.length) * 100)}%`
          },
          {
            Categoría: 'Gastos',
            Total: this.gastos.length,
            Activos: this.gastos.filter(g => g.estado_pago).length,
            Inactivos: this.gastos.filter(g => !g.estado_pago).length,
            Porcentaje: `${this.porcentajePago}%`
          }
        ],
        totalFinanciero: this.totalRecaudado,
        resumen: [
          { label: 'Total Residentes', valor: this.residentes.length },
          { label: 'Total Personal', valor: this.personal.length },
          { label: 'Total Gastos', valor: this.gastos.length },
          { label: 'Total Recaudado', valor: `$${this.totalRecaudado.toLocaleString()}` }
        ]
      };
      this.reporteGenerado = true;
      this.agregarAlHistorial('Completo');
    },

    agregarAlHistorial(tipo) {
      this.historialReportes.unshift({
        id: Date.now(),
        fecha: new Date(),
        tipo: tipo,
        filtros: this.filtrosAplicados.length > 0 ? 
          this.filtrosAplicados.map(f => `${f.label}: ${f.valor}`).join(', ') : 
          'Sin filtros',
        registros: this.reporteActual.datos.length
      });
    },

    getEstadoClass(estado) {
      if (estado === 'Activo' || estado === 'Pagado') {
        return 'estado-pagado';
      } else if (estado === 'Inactivo' || estado === 'Pendiente') {
        return 'estado-pendiente';
      }
      return 'badge bg-secondary';
    },

    descargarReporte(reporte = null) {
      const datos = reporte || this.reporteActual;
      const jsonData = JSON.stringify(datos, null, 2);
      const blob = new Blob([jsonData], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `reporte-${datos.titulo.toLowerCase().replace(/\s+/g, '-')}-${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      
              this.$alert.mostrarExito('Reporte descargado exitosamente');
    },

    imprimirReporte() {
      window.print();
    },

    exportarDatos() {
      const datosCompletos = {
        residentes: this.residentes,
        personal: this.personal,
        gastos: this.gastos,
        estadisticas: {
          totalResidentes: this.totalResidentes,
          totalPersonal: this.totalPersonal,
          gastosPendientes: this.gastosPendientes,
          totalRecaudado: this.totalRecaudado
        }
      };

      const jsonData = JSON.stringify(datosCompletos, null, 2);
      const blob = new Blob([jsonData], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `datos-completos-${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
      
              this.$alert.mostrarExito('Datos exportados exitosamente');
    },

    verReporte(reporte) { // eslint-disable-line no-unused-vars
      // Implementar vista del reporte histórico
      this.$alert.mostrarInfo('Función de vista histórica en desarrollo');
    },

    formatearFecha(fecha) {
      return new Date(fecha).toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    },


  }
};
</script>

<style scoped>
.report-card {
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.report-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.report-icon {
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

.reporte-preview {
  background: white;
  padding: 2rem;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-sm);
}

.reporte-header {
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 1rem;
}

.reporte-stats-summary {
  text-align: right;
}

.stat-item {
  margin-bottom: 0.5rem;
}

.stat-label {
  font-weight: 600;
  color: var(--dark-color);
}

.stat-value {
  font-weight: 700;
  color: var(--primary-color);
  margin-left: 0.5rem;
}

.reporte-footer {
  border-top: 1px solid var(--border-color);
  padding-top: 1rem;
}

.table tbody tr {
  transition: all 0.2s ease;
}

.table tbody tr:hover {
  background-color: rgba(37, 99, 235, 0.05);
  transform: scale(1.01);
}

@media print {
  .main-container {
    background: white !important;
  }
  
  .card {
    box-shadow: none !important;
    border: 1px solid #ddd !important;
  }
  
  .btn, .report-card {
    display: none !important;
  }
}
</style>