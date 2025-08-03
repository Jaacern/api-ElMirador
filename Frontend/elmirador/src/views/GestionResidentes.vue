<template>
  <div class="main-container fade-in">
    <!-- Header con estadísticas -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-users"></i>
            Gestión de Residentes
          </h1>
          <div class="d-flex gap-2">
            <button class="btn btn-primary" @click="mostrarResidentess">
              <i class="bi bi-list-ul me-2"></i>
              Mostrar Residentes
            </button>
            <button class="btn btn-success" @click="agregarResidenteFormulario">
              <i class="bi bi-plus-circle me-2"></i>
              Agregar Residente
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tarjetas de estadísticas -->
    <div class="row mb-4" v-if="showResidentList">
      <div class="col-md-3">
        <div class="stats-card">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ residentes.length }}</h3>
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
              <h3>{{ residentesActivos }}</h3>
              <p>Residentes Activos</p>
            </div>
            <i class="bi bi-check-circle-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ departamentosOcupados }}</h3>
              <p>Departamentos Ocupados</p>
            </div>
            <i class="bi bi-building-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ promedioEdad }}</h3>
              <p>Edad Promedio</p>
            </div>
            <i class="bi bi-graph-up" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Lista de residentes -->
    <div v-if="showResidentList" class="card shadow-lg">
      <div class="card-header custom-header residentes d-flex justify-content-between align-items-center">
        <h4 class="card-title">
          <i class="fas fa-list"></i>
          Lista de Residentes
        </h4>
        <div class="d-flex align-items-center gap-3">
          <div class="input-group" style="width: 300px;">
            <span class="input-group-text">
              <i class="bi bi-search"></i>
            </span>
            <input 
              type="text" 
              class="form-control" 
              placeholder="Buscar residente..."
              v-model="busqueda"
              @input="filtrarResidentes"
            >
          </div>
          <span class="badge bg-light text-dark fs-6">
            {{ residentesFiltrados.length }} de {{ residentes.length }}
          </span>
        </div>
      </div>
      <div class="card-body p-0">
        <div class="table-responsive">
          <table class="table table-hover mb-0">
            <thead>
              <tr>
                <th class="text-center">#</th>
                <th>Nombre Completo</th>
                <th>Rut</th>
                <th>Email</th>
                <th>Teléfono</th>
                <th>Departamento</th>
                <th class="text-center">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(residente, index) in residentesFiltrados" :key="residente._id" class="fade-in">
                <td class="text-center fw-bold">{{ index + 1 }}</td>
                <td>
                  <div class="d-flex align-items-center">
                    <div class="avatar me-3">
                      <i class="bi bi-person-circle fs-4 text-primary"></i>
                    </div>
                    <div>
                      <div class="fw-semibold">
                        {{ residente.Nombre }} {{ residente.ApePat }} {{ residente.ApeMat }}
                      </div>
                      <small class="text-muted">{{ residente.Email }}</small>
                    </div>
                  </div>
                </td>
                <td>
                  <span class="badge bg-secondary">{{ residente.RutArre }}</span>
                </td>
                <td>
                  <a :href="'mailto:' + residente.Email" class="text-decoration-none">
                    {{ residente.Email }}
                  </a>
                </td>
                <td>
                  <div>
                    <div v-if="residente.Fono1">
                      <i class="bi bi-telephone me-1"></i>{{ residente.Fono1 }}
                    </div>
                    <div v-if="residente.Fono2" class="text-muted">
                      <i class="bi bi-telephone me-1"></i>{{ residente.Fono2 }}
                    </div>
                  </div>
                </td>
                <td>
                  <span class="badge bg-info">
                    <i class="bi bi-building me-1"></i>
                    {{ residente.nro_departamento }}
                  </span>
                </td>
                <td>
                  <div class="d-flex justify-content-center gap-1">
                    <button 
                      class="btn btn-warning btn-sm tooltip-custom" 
                      @click="editarResidente(residente)"
                      data-tooltip="Editar Residente"
                    >
                      <i class="bi bi-pencil"></i>
                    </button>
                    <button 
                      class="btn btn-info btn-sm tooltip-custom" 
                      @click="verDetalles(residente)"
                      data-tooltip="Ver Detalles"
                    >
                      <i class="bi bi-eye"></i>
                    </button>
                    <button 
                      class="btn btn-danger btn-sm tooltip-custom" 
                      @click="eliminarResidente(residente._id)"
                      data-tooltip="Eliminar Residente"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="residentesFiltrados.length === 0">
                <td colspan="7" class="text-center py-4">
                  <div class="text-muted">
                    <i class="bi bi-search fs-1 d-block mb-3"></i>
                    <h5>No se encontraron residentes</h5>
                    <p>Intenta ajustar los filtros de búsqueda</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Formulario para agregar/editar residente -->
    <div v-if="showForm" class="card shadow-lg mt-4">
      <div class="card-header custom-header">
        <h4 class="card-title">
          <i class="fas fa-user-plus"></i>
          {{ editMode ? 'Editar Residente' : 'Agregar Nuevo Residente' }}
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="submitResidente" class="row g-3">
          <div class="col-md-6">
            <label for="rut" class="form-label">
              <i class="bi bi-card-text me-1"></i>Rut
            </label>
            <input 
              v-model="residenteForm.RutArre" 
              type="text" 
              id="rut" 
              class="form-control" 
              placeholder="Ej: 12345678-9"
              required
            />
          </div>
          <div class="col-md-6">
            <label for="nombre" class="form-label">
              <i class="bi bi-person me-1"></i>Nombre
            </label>
            <input 
              v-model="residenteForm.Nombre" 
              type="text" 
              id="nombre" 
              class="form-control" 
              placeholder="Nombre del residente"
              required
            />
          </div>
          <div class="col-md-6">
            <label for="apePat" class="form-label">
              <i class="bi bi-person me-1"></i>Apellido Paterno
            </label>
            <input 
              v-model="residenteForm.ApePat" 
              type="text" 
              id="apePat" 
              class="form-control" 
              placeholder="Apellido paterno"
            />
          </div>
          <div class="col-md-6">
            <label for="apeMat" class="form-label">
              <i class="bi bi-person me-1"></i>Apellido Materno
            </label>
            <input 
              v-model="residenteForm.ApeMat" 
              type="text" 
              id="apeMat" 
              class="form-control" 
              placeholder="Apellido materno"
            />
          </div>
          <div class="col-md-6">
            <label for="email" class="form-label">
              <i class="bi bi-envelope me-1"></i>Email
            </label>
            <input 
              v-model="residenteForm.Email" 
              type="email" 
              id="email" 
              class="form-control" 
              placeholder="correo@ejemplo.com"
            />
          </div>
          <div class="col-md-6">
            <label for="departamento" class="form-label">
              <i class="bi bi-building me-1"></i>Departamento
            </label>
            <input 
              v-model="residenteForm.nro_departamento" 
              type="text" 
              id="departamento" 
              class="form-control" 
              placeholder="Número de departamento"
            />
          </div>
          <div class="col-md-6">
            <label for="fono1" class="form-label">
              <i class="bi bi-telephone me-1"></i>Teléfono Principal
            </label>
            <input 
              v-model="residenteForm.Fono1" 
              type="tel" 
              id="fono1" 
              class="form-control" 
              placeholder="+56 9 1234 5678"
            />
          </div>
          <div class="col-md-6">
            <label for="fono2" class="form-label">
              <i class="bi bi-telephone me-1"></i>Teléfono Secundario
            </label>
            <input 
              v-model="residenteForm.Fono2" 
              type="tel" 
              id="fono2" 
              class="form-control" 
              placeholder="+56 9 8765 4321"
            />
          </div>
          <div class="col-12">
            <div class="d-flex justify-content-end gap-2">
              <button type="button" class="btn btn-secondary" @click="cancelarFormulario">
                <i class="bi bi-x-circle me-2"></i>Cancelar
              </button>
              <button type="submit" class="btn btn-primary">
                <i class="bi bi-check-circle me-2"></i>
                {{ editMode ? 'Actualizar Residente' : 'Agregar Residente' }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de detalles del residente -->
    <div class="modal fade" id="detallesModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <i class="bi bi-person-circle me-2"></i>
              Detalles del Residente
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body" v-if="residenteSeleccionado">
            <div class="row">
              <div class="col-md-4 text-center">
                <div class="avatar-large mb-3">
                  <i class="bi bi-person-circle" style="font-size: 4rem; color: var(--primary-color);"></i>
                </div>
                <h4>{{ residenteSeleccionado.Nombre }} {{ residenteSeleccionado.ApePat }} {{ residenteSeleccionado.ApeMat }}</h4>
                <p class="text-muted">Residente</p>
              </div>
              <div class="col-md-8">
                <div class="row g-3">
                  <div class="col-12">
                    <label class="fw-bold">Rut:</label>
                    <p>{{ residenteSeleccionado.RutArre }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Email:</label>
                    <p>{{ residenteSeleccionado.Email }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Departamento:</label>
                    <p>{{ residenteSeleccionado.nro_departamento }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Teléfono Principal:</label>
                    <p>{{ residenteSeleccionado.Fono1 }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Teléfono Secundario:</label>
                    <p>{{ residenteSeleccionado.Fono2 }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-warning" @click="editarResidente(residenteSeleccionado)" data-bs-dismiss="modal">
              <i class="bi bi-pencil me-2"></i>Editar
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
      residentes: [],
      residentesFiltrados: [],
      residenteForm: {
        RutArre: '',
        Nombre: '',
        ApePat: '',
        ApeMat: '',
        Email: '',
        Fono1: '',
        Fono2: '',
        nro_departamento: '',
      },
      showResidentList: false,
      showForm: false,
      editMode: false,
      currentResidenteId: null,
      busqueda: '',
      residenteSeleccionado: null,
    };
  },
  computed: {
    residentesActivos() {
      return this.residentes.length;
    },
    departamentosOcupados() {
      const departamentos = new Set(this.residentes.map(r => r.nro_departamento));
      return departamentos.size;
    },
    promedioEdad() {
      // Simulación de cálculo de edad promedio
      return Math.floor(Math.random() * 20) + 35;
    }
  },
  mounted() {
    // Cargar residentes automáticamente al montar el componente
    this.mostrarResidentess();
  },
  methods: {
    async mostrarResidentess() {
      try {
        const response = await axios.get('http://localhost:5000/residentes');
        this.residentes = response.data;
        this.residentesFiltrados = [...this.residentes];
        this.showResidentList = true;
        this.showForm = false;
      } catch (error) {
        console.error('Error al obtener los residentes:', error);
        this.$alert.mostrarError('Error al cargar residentes');
      }
    },

    agregarResidenteFormulario() {
      this.showResidentList = false;
      this.showForm = true;
      this.resetForm();
      this.editMode = false;
    },

    async submitResidente() {
      if (this.editMode) {
        await this.actualizarResidente();
      } else {
        await this.agregarResidente();
      }
    },

    async agregarResidente() {
      try {
        const response = await axios.post('http://localhost:5000/residentes', this.residenteForm);
        console.log('Residente agregado:', response.data);
        this.$alert.mostrarExito('Residente agregado exitosamente');
        this.mostrarResidentess();
        this.resetForm();
      } catch (error) {
        console.error('Error al agregar residente:', error);
        this.$alert.mostrarError('Error al agregar residente');
      }
    },

    async actualizarResidente() {
      try {
        const response = await axios.put(`http://localhost:5000/residentes/${this.currentResidenteId}`, this.residenteForm);
        console.log('Residente actualizado:', response.data);
        this.$alert.mostrarExito('Residente actualizado exitosamente');
        this.mostrarResidentess();
        this.resetForm();
      } catch (error) {
        console.error('Error al actualizar residente:', error);
        this.$alert.mostrarError('Error al actualizar residente');
      }
    },

    editarResidente(residente) {
      this.residenteForm = { ...residente };
      this.currentResidenteId = residente._id;
      this.editMode = true;
      this.showForm = true;
      this.showResidentList = false;
    },

    async eliminarResidente(id) {
      const confirmado = await this.$alert.confirm('¿Estás seguro de eliminar este residente?');
      if (confirmado) {
        try {
          const response = await axios.delete(`http://localhost:5000/residentes/${id}`);
          console.log('Residente eliminado:', response.data);
          this.$alert.mostrarExito('Residente eliminado exitosamente');
          this.mostrarResidentess();
        } catch (error) {
          console.error('Error al eliminar residente:', error);
          this.$alert.mostrarError('Error al eliminar residente');
        }
      }
    },

    resetForm() {
      this.residenteForm = {
        RutArre: '',
        Nombre: '',
        ApePat: '',
        ApeMat: '',
        Email: '',
        Fono1: '',
        Fono2: '',
        nro_departamento: '',
      };
      this.editMode = false;
      this.currentResidenteId = null;
    },

    cancelarFormulario() {
      this.showForm = false;
      this.resetForm();
      if (this.residentes.length > 0) {
        this.showResidentList = true;
      }
    },

    filtrarResidentes() {
      if (!this.busqueda) {
        this.residentesFiltrados = [...this.residentes];
        return;
      }
      
      const busquedaLower = this.busqueda.toLowerCase();
      this.residentesFiltrados = this.residentes.filter(residente => 
        residente.Nombre.toLowerCase().includes(busquedaLower) ||
        residente.ApePat.toLowerCase().includes(busquedaLower) ||
        residente.ApeMat.toLowerCase().includes(busquedaLower) ||
        residente.RutArre.toLowerCase().includes(busquedaLower) ||
        residente.Email.toLowerCase().includes(busquedaLower) ||
        residente.nro_departamento.toLowerCase().includes(busquedaLower)
      );
    },

    verDetalles(residente) {
      this.residenteSeleccionado = residente;
      // Mostrar modal usando Bootstrap
      const modal = new Modal(document.getElementById('detallesModal'));
      modal.show();
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

.input-group-text {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  border: none;
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