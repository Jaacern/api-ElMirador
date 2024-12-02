<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-cash-coin me-2"></i>Gestión de Gastos Comunes
    </h1>

    <!-- Generar Gasto Común Card -->
    <div class="card shadow-sm mb-4">
      <div class="card-header custom-header text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-plus-square me-2"></i>Generar Gasto Común
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="generarGastoComun">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Mes</label>
              <select v-model="gastoForm.mes" class="form-select" required>
                <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
              </select>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Año</label>
              <input type="number" v-model="gastoForm.anio" class="form-control" required />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Valor</label>
              <input type="number" v-model="gastoForm.valor" class="form-control" required />
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Departamento</label>
              <select v-model="gastoForm.nro_departamento" class="form-select" required>
                <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                  {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
                </option>
              </select>
            </div>
          </div>

          <div class="d-flex justify-content-between">
            <button type="submit" class="btn btn-primary">
              <i class="bi bi-save me-1"></i>Generar Gasto Común
            </button>
          </div>
        </form>
      </div>
    </div>

    <div class="card shadow-sm">
      <div class="card-header custom-header text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-list-check me-2"></i>Lista de Gastos Comunes
        </h4>
        <button 
      v-if="gastosFiltrados.length > 0" 
      class="btn btn-success btn-sm me-2" 
      @click="pagarAnoCompleto"
    >
      <i class="bi bi-calendar-check me-1"></i>Pagar Año Completo
    </button>
        <span class="badge bg-light text-dark">Total: {{ gastosFiltrados.length }}</span>
      </div>
      <div class="card-body">
        <!-- Filtros -->
        <div class="row mb-4">
          <div class="col-md-3 mb-2">
            <label class="form-label">Departamento</label>
            <select v-model="filtros.departamento" class="form-select" @change="aplicarFiltros">
              <option value="">Todos los departamentos</option>
              <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
              </option>
            </select>
          </div>
          <div class="col-md-3 mb-2">
            <label class="form-label">Estado</label>
            <select v-model="filtros.estado" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option value="pagado">Pagados</option>
              <option value="pendiente">Pendientes</option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">Año</label>
            <select v-model="filtros.anio" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option v-for="anio in aniosDisponibles" :key="anio" :value="anio">{{ anio }}</option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">Mes</label>
            <select v-model="filtros.mes" class="form-select" @change="aplicarFiltros">
              <option value="">Todos</option>
              <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
            </select>
          </div>
          <div class="col-md-2 mb-2">
            <label class="form-label">Ordenar valor</label>
            <select v-model="filtros.ordenValor" class="form-select" @change="aplicarFiltros">
              <option value="">Sin orden</option>
              <option value="asc">Menor a mayor</option>
              <option value="desc">Mayor a menor</option>
            </select>
          </div>
        </div>
      </div>

      <div v-if="gastosFiltrados.length" class="table-responsive">
        <table class="table table-striped table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th>Mes</th>
              <th>Año</th>
              <th>Valor</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="gasto in gastosFiltrados" :key="gasto._id">
              <td>{{ gasto.mes }}</td>
              <td>{{ gasto.anio }}</td>
              <td>${{ gasto.valor }}</td>
              <td> <span :class="gasto.estado_pago ? 'badge bg-success' : 'badge bg-warning'">
    {{ gasto.estado_pago ? 'Pagado' : 'Pendiente' }}
  </span></td>
              <td>
                <div class="btn-group btn-group-sm" role="group">
                  <button 
                    v-if="!gasto.estado_pago"
                    class="btn btn-success" 
                    @click="pagarGasto(gasto._id)"
                    title="Pagar"
                  >
                    <i class="bi bi-check-circle"></i>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="alert alert-info text-center">
        No se encontraron gastos con los filtros seleccionados
      </div>

      <!-- Gastos Pendientes -->
      <div class="card shadow-sm mt-4">
        <div class="card-header custom-header text-white d-flex justify-content-between align-items-center">
          <h4 class="mb-0">
            <i class="bi bi-clock-history me-2"></i>Gastos Comunes Pendientes
          </h4>
          <button class="btn btn-light btn-sm" @click="generarInformeJSON">
            <i class="bi bi-file-earmark-text me-1"></i>Generar Informe JSON
          </button>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-striped table-hover mb-0">
              <thead class="table-light">
                <tr>
                  <th>Mes</th>
                  <th>Año</th>
                  <th>Valor</th>
                  <th>Departamento</th>
                  <th>Estado</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="gasto in gastosPendientes" :key="gasto._id">
                  <td>{{ gasto.mes }}</td>
                  <td>{{ gasto.anio }}</td>
                  <td>${{ gasto.valor }}</td>
                  <td>{{ gasto.nro_departamento }}</td>
                  <td>  <span class="badge bg-warning">Pendiente</span> </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      meses: [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Año completo',
      ],
      gastoForm: {
        mes: '',
        anio: new Date().getFullYear(),
        valor: '',
        nro_departamento: ''
      },
      residentes: [],
      gastos: [],
      gastosPendientes: [],
      gastosFiltrados: [],
      filtros: {
        departamento: '',
        estado: '',
        anio: '',
        mes: '',
        ordenValor: ''
      },
      aniosDisponibles: []
    };
  },

  computed: {
    obtenerTituloFiltros() {
      const partes = [];
      
      if (this.filtros.departamento) {
        partes.push(`Depto ${this.filtros.departamento}`);
      }
      if (this.filtros.estado) {
        partes.push(this.filtros.estado === 'pagado' ? 'pagados' : 'pendientes');
      }
      if (this.filtros.anio) {
        partes.push(`del año ${this.filtros.anio}`);
      }
      if (this.filtros.mes) {
        partes.push(`del mes ${this.filtros.mes}`);
      }
      
      return partes.length ? 'Gastos para ' + partes.join(', ') : 'Todos los gastos';
    }
  },

  mounted() {
    this.cargarResidentes();
    this.cargarGastos();
    this.cargarGastosPendientes();
    this.generarAniosDisponibles();
  },

  methods: {
    async cargarResidentes() {
      try {
        const response = await axios.get('http://localhost:5000/residentes');
        this.residentes = response.data;
      } catch (error) {
        console.error('Error al cargar residentes:', error);
      }
    },

    async cargarGastos() {
      try {
        const response = await axios.get('http://localhost:5000/gastos-comunes');
        this.gastos = response.data;
        this.aplicarFiltros();
      } catch (error) {
        console.error('Error al cargar gastos:', error);
      }
    },

    async cargarGastosPendientes() {
      try {
        const response = await axios.get('http://localhost:5000/gastos-comunes/pendientes');
        this.gastosPendientes = response.data;
      } catch (error) {
        console.error('Error al cargar gastos pendientes:', error);
      }
    },

    generarAniosDisponibles() {
      const anioActual = new Date().getFullYear();
      this.aniosDisponibles = Array.from(
        { length: 5 },
        (_, i) => anioActual - i
      );
    },

    aplicarFiltros() {
      let gastosFiltrados = [...this.gastos];

      // Filtro por departamento
      if (this.filtros.departamento) {
        gastosFiltrados = gastosFiltrados.filter(
          gasto => gasto.nro_departamento === this.filtros.departamento
        );
      }

      // Filtro por estado
      if (this.filtros.estado) {
        const estaPagado = this.filtros.estado === 'pagado';
        gastosFiltrados = gastosFiltrados.filter(
          gasto => gasto.estado_pago === estaPagado
        );
      }

      // Filtro por año
      if (this.filtros.anio) {
        gastosFiltrados = gastosFiltrados.filter(
          gasto => gasto.anio === parseInt(this.filtros.anio)
        );
      }

      // Filtro por mes
      if (this.filtros.mes) {
        gastosFiltrados = gastosFiltrados.filter(
          gasto => gasto.mes === this.filtros.mes
        );
      }

      // Ordenar por valor
      if (this.filtros.ordenValor) {
        gastosFiltrados.sort((a, b) => {
          if (this.filtros.ordenValor === 'asc') {
            return a.valor - b.valor;
          } else {
            return b.valor - a.valor;
          }
        });
      }

      this.gastosFiltrados = gastosFiltrados;
    },

    async generarGastoComun() {
  try {
    // Si el mes seleccionado es "Año completo"
    if (this.gastoForm.mes === 'Año completo') {
      // Generar gastos para todos los meses del año
      const mesesAGenerar = this.meses.slice(0, 12); // Excluye "Año completo"
      
      for (const mes of mesesAGenerar) {
        const gastoExistente = this.gastos.find(gasto => 
          gasto.mes === mes && 
          gasto.anio === this.gastoForm.anio && 
          gasto.nro_departamento === this.gastoForm.nro_departamento
        );

        if (!gastoExistente) {
          await axios.post('http://localhost:5000/gastos-comunes', {
            ...this.gastoForm,
            mes: mes
          });
        }
      }

      alert('Gastos comunes generados para todo el año');
    } else {
      // Lógica existente para un mes específico
      const gastoExistente = this.gastos.find(gasto => 
        gasto.mes === this.gastoForm.mes && 
        gasto.anio === this.gastoForm.anio && 
        gasto.nro_departamento === this.gastoForm.nro_departamento
      );

      if (gastoExistente) {
        alert('Ya existe un gasto común para este departamento en el mes y año seleccionados');
        return;
      }

      await axios.post('http://localhost:5000/gastos-comunes', this.gastoForm);
      alert('Gasto común generado exitosamente');
    }

    // Recargar y resetear
    this.cargarGastos();
    this.cargarGastosPendientes();
    this.gastoForm = {
      mes: '',
      anio: new Date().getFullYear(),
      valor: '',
      nro_departamento: ''
    };
  } catch (error) {
    console.error('Error al generar gasto común:', error);
    alert('Error al generar gasto común');
  }
},
async pagarAnoCompleto() {
  // Verificar si hay un año seleccionado en los filtros
  const anioAPagar = this.filtros.anio || new Date().getFullYear();
  
  // Filtrar gastos pendientes del año seleccionado
  const gastosPendientesPorPagar = this.gastosFiltrados.filter(
    gasto => !gasto.estado_pago && gasto.anio === anioAPagar
  );

  if (gastosPendientesPorPagar.length === 0) {
    alert('No hay gastos pendientes para pagar en este año');
    return;
  }

  try {
    // Pagar cada gasto pendiente
    for (const gasto of gastosPendientesPorPagar) {
      await axios.put(`http://localhost:5000/gastos-comunes/${gasto._id}`, {
        estado_pago: true
      });
    }

    alert(`Todos los gastos de ${anioAPagar} han sido marcados como pagados`);
    
    // Recargar la lista de gastos
    this.cargarGastos();
    this.cargarGastosPendientes();
  } catch (error) {
    console.error('Error al pagar año completo:', error);
    alert('Hubo un error al intentar pagar todos los gastos');
  }
},

    async pagarGasto(id) {
      try {
        await axios.put(`http://localhost:5000/gastos-comunes/${id}`, {
          estado_pago: true
        });
        alert('Gasto marcado como pagado');
        this.cargarGastos();
        this.cargarGastosPendientes();
      } catch (error) {
        console.error('Error al pagar gasto:', error);
        alert('Error al actualizar el estado del pago');
      }
    },

    

    generarInformeJSON() {
      const jsonData = JSON.stringify(this.gastosPendientes, null, 2);
      const blob = new Blob([jsonData], { type: 'application/json' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'gastos-pendientes.json';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    }
  }
};
</script>

<style scoped>
.form-label {
  font-weight: 600;
}

.table-responsive {
  max-height: 500px;
  overflow-y: auto;
}

.btn-group-sm > .btn {
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
}

/* Opcional: Añadir algunas transiciones suaves */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.custom-header {
  background-color: #008E63;
  color: white;
}
</style>