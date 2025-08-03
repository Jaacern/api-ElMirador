<template>
  <div class="main-container fade-in">
    <!-- Header con estadísticas -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-money-bill-wave"></i>
            Gestión de Gastos Comunes
          </h1>
        </div>
      </div>
    </div>

    <!-- Tarjetas de estadísticas -->
    <div class="row mb-4" v-if="gastosFiltrados.length > 0">
      <div class="col-md-3">
        <div class="stats-card">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ gastosFiltrados.length }}</h3>
              <p>Total Gastos</p>
            </div>
            <i class="bi bi-cash-stack" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #10b981, #059669);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ gastosPagados }}</h3>
              <p>Gastos Pagados</p>
            </div>
            <i class="bi bi-check-circle-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ gastosPendientes }}</h3>
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
              <h3>${{ totalRecaudado.toLocaleString() }}</h3>
              <p>Total Recaudado</p>
            </div>
            <i class="bi bi-currency-dollar" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Generar Gasto Común Card -->
    <div class="card shadow-lg mb-4">
      <div class="card-header custom-header d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-plus-square me-2"></i>Generar Gasto Común
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="generarGastoComun" class="row g-3">
          <div class="col-md-3">
            <label class="form-label">
              <i class="bi bi-calendar me-1"></i>Mes
            </label>
            <select v-model="gastoForm.mes" class="form-select" required>
              <option value="">Seleccionar mes</option>
              <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
            </select>
          </div>
          <div class="col-md-3">
            <label class="form-label">
              <i class="bi bi-calendar-year me-1"></i>Año
            </label>
            <input type="number" v-model="gastoForm.anio" class="form-control" placeholder="2024" required />
          </div>
          <div class="col-md-3">
            <label class="form-label">
              <i class="bi bi-currency-dollar me-1"></i>Valor
            </label>
            <input type="number" v-model="gastoForm.valor" class="form-control" placeholder="50000" required />
          </div>
          <div class="col-md-3">
            <label class="form-label">
              <i class="bi bi-building me-1"></i>Departamento
            </label>
            <select v-model="gastoForm.nro_departamento" class="form-select" required>
              <option value="">Seleccionar departamento</option>
              <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
              </option>
            </select>
          </div>
          <div class="col-12">
            <div class="d-flex justify-content-end">
              <button type="submit" class="btn btn-primary">
                <i class="bi bi-save me-2"></i>Generar Gasto Común
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Lista de Gastos Comunes -->
    <div class="card shadow-lg">
      <div class="card-header custom-header d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-list-check me-2"></i>Lista de Gastos Comunes
        </h4>
        <div class="d-flex align-items-center gap-3">
          <button 
            v-if="gastosFiltrados.length > 0" 
            class="btn btn-success btn-sm" 
            @click="pagarAnoCompleto"
          >
            <i class="bi bi-calendar-check me-1"></i>Pagar Año Completo
          </button>
          <span class="badge bg-light text-dark fs-6">
            {{ gastosFiltrados.length }} gastos
          </span>
        </div>
      </div>
      <div class="card-body">
        <!-- Filtros -->
        <div class="row mb-4">
          <div class="col-md-3 mb-2">
            <label class="form-label">
              <i class="bi bi-building me-1"></i>Departamento
            </label>
            <select v-model="filtros.departamento" class="form-select" @change="aplicarFiltros">
              <option value="">Todos los departamentos</option>
              <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
              </option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">
              <i class="bi bi-toggle-on me-1"></i>Estado
            </label>
            <select v-model="filtros.estado" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option value="pagado">Pagados</option>
              <option value="pendiente">Pendientes</option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">
              <i class="bi bi-calendar-year me-1"></i>Año
            </label>
            <select v-model="filtros.anio" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option v-for="anio in aniosDisponibles" :key="anio" :value="anio">{{ anio }}</option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">
              <i class="bi bi-calendar me-1"></i>Mes
            </label>
            <select v-model="filtros.mes" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
            </select>
          </div>
          <div class="col-md-3 mb-2">
            <label class="form-label">
              <i class="bi bi-search me-1"></i>Buscar
            </label>
            <input 
              type="text" 
              class="form-control" 
              placeholder="Buscar gastos..."
              v-model="busqueda"
              @input="aplicarFiltros"
            >
          </div>
        </div>

        <!-- Tabla de gastos -->
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th class="text-center">#</th>
                <th>Departamento</th>
                <th>Mes/Año</th>
                <th>Valor</th>
                <th>Estado</th>
                <th class="text-center">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(gasto, index) in gastosFiltrados" :key="gasto._id" class="fade-in">
                <td class="text-center fw-bold">{{ index + 1 }}</td>
                <td>
                  <div class="d-flex align-items-center">
                    <div class="avatar me-3">
                      <i class="bi bi-building fs-4 text-primary"></i>
                    </div>
                    <div>
                      <div class="fw-semibold">Depto. {{ gasto.nro_departamento }}</div>
                      <small class="text-muted">
                        {{ obtenerResidente(gasto.nro_departamento) }}
                      </small>
                    </div>
                  </div>
                </td>
                <td>
                  <span class="badge bg-info">
                    <i class="bi bi-calendar me-1"></i>
                    {{ gasto.mes }} {{ gasto.anio }}
                  </span>
                </td>
                <td>
                  <span class="fw-bold text-success">
                    ${{ gasto.valor.toLocaleString() }}
                  </span>
                </td>
                <td>
                  <span :class="gasto.estado_pago ? 'estado-pagado' : 'estado-pendiente'">
                    <i :class="gasto.estado_pago ? 'bi bi-check-circle me-1' : 'bi bi-clock me-1'"></i>
                    {{ gasto.estado_pago ? 'Pagado' : 'Pendiente' }}
                  </span>
                </td>
                <td>
                  <div class="d-flex justify-content-center gap-1">
                    <button 
                      v-if="!gasto.estado_pago"
                      class="btn btn-success btn-sm tooltip-custom" 
                      @click="marcarComoPagado(gasto._id)"
                      data-tooltip="Marcar como Pagado"
                    >
                      <i class="bi bi-check-circle"></i>
                    </button>
                    <button 
                      v-else
                      class="btn btn-warning btn-sm tooltip-custom" 
                      @click="marcarComoPendiente(gasto._id)"
                      data-tooltip="Marcar como Pendiente"
                    >
                      <i class="bi bi-clock"></i>
                    </button>
                    <button 
                      class="btn btn-info btn-sm tooltip-custom" 
                      @click="verDetalles(gasto)"
                      data-tooltip="Ver Detalles"
                    >
                      <i class="bi bi-eye"></i>
                    </button>
                    <button 
                      class="btn btn-danger btn-sm tooltip-custom" 
                      @click="eliminarGasto(gasto._id)"
                      data-tooltip="Eliminar Gasto"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="gastosFiltrados.length === 0">
                <td colspan="6" class="text-center py-4">
                  <div class="text-muted">
                    <i class="bi bi-search fs-1 d-block mb-3"></i>
                    <h5>No se encontraron gastos</h5>
                    <p>Intenta ajustar los filtros de búsqueda</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal de detalles del gasto -->
    <div class="modal fade" id="detallesGastoModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <i class="bi bi-cash-coin me-2"></i>
              Detalles del Gasto Común
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body" v-if="gastoSeleccionado">
            <div class="row">
              <div class="col-md-4 text-center">
                <div class="avatar-large mb-3">
                  <i class="bi bi-cash-coin" style="font-size: 4rem; color: var(--primary-color);"></i>
                </div>
                <h4>Depto. {{ gastoSeleccionado.nro_departamento }}</h4>
                <p class="text-muted">{{ obtenerResidente(gastoSeleccionado.nro_departamento) }}</p>
                <span :class="gastoSeleccionado.estado_pago ? 'estado-pagado' : 'estado-pendiente'">
                  {{ gastoSeleccionado.estado_pago ? 'Pagado' : 'Pendiente' }}
                </span>
              </div>
              <div class="col-md-8">
                <div class="row g-3">
                  <div class="col-md-6">
                    <label class="fw-bold">Mes:</label>
                    <p>{{ gastoSeleccionado.mes }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Año:</label>
                    <p>{{ gastoSeleccionado.anio }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Valor:</label>
                    <p class="fw-bold text-success">${{ gastoSeleccionado.valor.toLocaleString() }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Estado:</label>
                    <p>{{ gastoSeleccionado.estado_pago ? 'Pagado' : 'Pendiente' }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button 
              v-if="!gastoSeleccionado?.estado_pago"
              type="button" 
              class="btn btn-success" 
              @click="marcarComoPagado(gastoSeleccionado?._id)" 
              data-bs-dismiss="modal"
            >
              <i class="bi bi-check-circle me-2"></i>Marcar como Pagado
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Modal } from 'bootstrap';

export default {
  data() {
    return {
      gastos: [],
      gastosFiltrados: [],
      residentes: [],
      gastoForm: {
        mes: '',
        anio: new Date().getFullYear(),
        valor: '',
        nro_departamento: ''
      },
      filtros: {
        departamento: '',
        estado: '',
        anio: '',
        mes: ''
      },
      busqueda: '',
      meses: [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
      ],
      gastoSeleccionado: null
    };
  },
  computed: {
    gastosPagados() {
      return this.gastosFiltrados.filter(g => g.estado_pago).length;
    },
    gastosPendientes() {
      return this.gastosFiltrados.filter(g => !g.estado_pago).length;
    },
    totalRecaudado() {
      return this.gastosFiltrados
        .filter(g => g.estado_pago)
        .reduce((total, gasto) => total + gasto.valor, 0);
    },
    aniosDisponibles() {
      const anios = [...new Set(this.gastos.map(g => g.anio))];
      return anios.sort((a, b) => b - a);
    }
  },
  mounted() {
    this.cargarDatos();
  },
  methods: {
    async cargarDatos() {
      try {
        const [gastosRes, residentesRes] = await Promise.all([
          axios.get('http://localhost:5000/gastos-comunes'),
          axios.get('http://localhost:5000/residentes')
        ]);
        
        this.gastos = gastosRes.data;
        this.residentes = residentesRes.data;
        this.aplicarFiltros();
              } catch (error) {
          console.error('Error al cargar datos:', error);
          this.$alert.mostrarError('Error al cargar datos');
        }
    },

    async generarGastoComun() {
      try {
        const response = await axios.post('http://localhost:5000/gastos-comunes', this.gastoForm);
        console.log('Gasto común generado:', response.data);
        this.$alert.mostrarExito('Gasto común generado exitosamente');
        this.resetForm();
        this.cargarDatos();
      } catch (error) {
        console.error('Error al generar gasto común:', error);
        this.$alert.mostrarError('Error al generar gasto común');
      }
    },

    async marcarComoPagado(id) {
      try {
        await axios.put(`http://localhost:5000/gastos-comunes/${id}`, {
          estado_pago: true
        });
        this.$alert.mostrarExito('Gasto marcado como pagado');
        this.cargarDatos();
      } catch (error) {
        console.error('Error al marcar como pagado:', error);
        this.$alert.mostrarError('Error al marcar como pagado');
      }
    },

    async marcarComoPendiente(id) {
      try {
        await axios.put(`http://localhost:5000/gastos-comunes/${id}`, {
          estado_pago: false
        });
                this.$alert.mostrarExito('Gasto marcado como pendiente');
        this.cargarDatos();
      } catch (error) {
        console.error('Error al marcar como pendiente:', error);
        this.$alert.mostrarError('Error al marcar como pendiente');
        }
    },

    async eliminarGasto(id) {
      const confirmado = await this.$alert.confirm('¿Estás seguro de eliminar este gasto?');
      if (confirmado) {
        try {
          await axios.delete(`http://localhost:5000/gastos-comunes/${id}`);
                  this.$alert.mostrarExito('Gasto eliminado exitosamente');
        this.cargarDatos();
      } catch (error) {
        console.error('Error al eliminar gasto:', error);
        this.$alert.mostrarError('Error al eliminar gasto');
      }
      }
    },

    async pagarAnoCompleto() {
      const confirmado = await this.$alert.confirm('¿Estás seguro de marcar todos los gastos pendientes como pagados?');
      if (confirmado) {
        try {
          const gastosPendientes = this.gastosFiltrados.filter(g => !g.estado_pago);
          const promesas = gastosPendientes.map(gasto => 
            axios.put(`http://localhost:5000/gastos-comunes/${gasto._id}`, {
              estado_pago: true
            })
          );
          
          await Promise.all(promesas);
                  this.$alert.mostrarExito('Todos los gastos marcados como pagados');
        this.cargarDatos();
      } catch (error) {
        console.error('Error al pagar año completo:', error);
        this.$alert.mostrarError('Error al pagar año completo');
      }
      }
    },

    aplicarFiltros() {
      let filtrado = [...this.gastos];

      // Filtro por departamento
      if (this.filtros.departamento) {
        filtrado = filtrado.filter(g => g.nro_departamento === this.filtros.departamento);
      }

      // Filtro por estado
      if (this.filtros.estado) {
        if (this.filtros.estado === 'pagado') {
          filtrado = filtrado.filter(g => g.estado_pago);
        } else if (this.filtros.estado === 'pendiente') {
          filtrado = filtrado.filter(g => !g.estado_pago);
        }
      }

      // Filtro por año
      if (this.filtros.anio) {
        filtrado = filtrado.filter(g => g.anio === this.filtros.anio);
      }

      // Filtro por mes
      if (this.filtros.mes) {
        filtrado = filtrado.filter(g => g.mes === this.filtros.mes);
      }

      // Filtro por búsqueda
      if (this.busqueda) {
        const busquedaLower = this.busqueda.toLowerCase();
        filtrado = filtrado.filter(g => 
          g.nro_departamento.toLowerCase().includes(busquedaLower) ||
          g.mes.toLowerCase().includes(busquedaLower) ||
          g.anio.toString().includes(busquedaLower) ||
          g.valor.toString().includes(busquedaLower)
        );
      }

      this.gastosFiltrados = filtrado;
    },

    obtenerResidente(departamento) {
      const residente = this.residentes.find(r => r.nro_departamento === departamento);
      return residente ? `${residente.Nombre} ${residente.ApePat}` : 'Sin asignar';
    },

    verDetalles(gasto) {
      this.gastoSeleccionado = gasto;
      const modal = new Modal(document.getElementById('detallesGastoModal'));
      modal.show();
    },

    resetForm() {
      this.gastoForm = {
        mes: '',
        anio: new Date().getFullYear(),
        valor: '',
        nro_departamento: ''
      };
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
  width: 100px;
  height: 100px;
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

.badge {
  font-size: 0.875rem;
  padding: 0.5rem 0.75rem;
}

.stats-card {
  transition: transform 0.2s ease;
}

.stats-card:hover {
  transform: translateY(-5px);
}
</style>