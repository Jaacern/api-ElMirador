<template>
  <div class="main-container fade-in">
    <!-- Header con estadísticas -->
    <div class="row mb-4">
      <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="page-title">
            <i class="fas fa-user-tie"></i>
            Gestión de Personal
          </h1>
          <div class="d-flex gap-2">
            <button class="btn btn-primary" @click="mostrarPersonal">
              <i class="bi bi-list-ul me-2"></i>
              Mostrar Personal
            </button>
            <button class="btn btn-success" @click="agregarPersonalFormulario">
              <i class="bi bi-plus-circle me-2"></i>
              Agregar Personal
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Tarjetas de estadísticas -->
    <div class="row mb-4" v-if="showPersonalList">
      <div class="col-md-3">
        <div class="stats-card">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ personal.length }}</h3>
              <p>Total Personal</p>
            </div>
            <i class="bi bi-people-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #10b981, #059669);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ personalActivo }}</h3>
              <p>Personal Activo</p>
            </div>
            <i class="bi bi-check-circle-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ personalInactivo }}</h3>
              <p>Personal Inactivo</p>
            </div>
            <i class="bi bi-x-circle-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="stats-card" style="background: linear-gradient(135deg, #06b6d4, #0891b2);">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h3>{{ cargosUnicos }}</h3>
              <p>Diferentes Cargos</p>
            </div>
            <i class="bi bi-briefcase-fill" style="font-size: 2rem; opacity: 0.8;"></i>
          </div>
        </div>
      </div>
    </div>

    <!-- Lista de Personal -->
    <div v-if="showPersonalList" class="card shadow-lg">
      <div class="card-header custom-header personal d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-list-check me-2"></i>
          Lista de Personal
        </h4>
        <div class="d-flex align-items-center gap-3">
          <div class="input-group" style="width: 300px;">
            <span class="input-group-text">
              <i class="bi bi-search"></i>
            </span>
            <input 
              type="text" 
              class="form-control" 
              placeholder="Buscar personal..."
              v-model="busqueda"
              @input="filtrarPersonal"
            >
          </div>
          <div class="btn-group" role="group">
            <button 
              class="btn btn-outline-light" 
              :class="{ 'active': filtroEstado === '' }"
              @click="filtrarPorEstado('')"
            >
              Todos
            </button>
            <button 
              class="btn btn-outline-light" 
              :class="{ 'active': filtroEstado === 'Activo' }"
              @click="filtrarPorEstado('Activo')"
            >
              Activos
            </button>
            <button 
              class="btn btn-outline-light" 
              :class="{ 'active': filtroEstado === 'Inactivo' }"
              @click="filtrarPorEstado('Inactivo')"
            >
              Inactivos
            </button>
          </div>
          <span class="badge bg-light text-dark fs-6">
            {{ personalFiltrado.length }} de {{ personal.length }}
          </span>
        </div>
      </div>
      <div class="card-body p-0">
        <div class="table-responsive">
          <table class="table table-hover mb-0">
            <thead>
              <tr>
                <th class="text-center">#</th>
                <th>Personal</th>
                <th>Rut</th>
                <th>Email</th>
                <th>Cargo</th>
                <th>Estado</th>
                <th class="text-center">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(persona, index) in personalFiltrado" :key="persona._id" class="fade-in">
                <td class="text-center fw-bold">{{ index + 1 }}</td>
                <td>
                  <div class="d-flex align-items-center">
                    <div class="avatar me-3">
                      <i class="bi bi-person-badge fs-4 text-primary"></i>
                    </div>
                    <div>
                      <div class="fw-semibold">
                        {{ persona.Nombre }} {{ persona.ApePat }} {{ persona.ApeMat }}
                      </div>
                      <small class="text-muted">{{ persona.Email }}</small>
                    </div>
                  </div>
                </td>
                <td>
                  <span class="badge bg-secondary">{{ persona.RutPersonal }}</span>
                </td>
                <td>
                  <a :href="'mailto:' + persona.Email" class="text-decoration-none">
                    {{ persona.Email }}
                  </a>
                </td>
                <td>
                  <span class="badge bg-info">
                    <i class="bi bi-briefcase me-1"></i>
                    {{ persona.Cargo }}
                  </span>
                </td>
                <td>
                  <span :class="persona.Estado === 'Activo' ? 'estado-pagado' : 'estado-pendiente'">
                    <i :class="persona.Estado === 'Activo' ? 'bi bi-check-circle me-1' : 'bi bi-x-circle me-1'"></i>
                    {{ persona.Estado }}
                  </span>
                </td>
                <td>
                  <div class="d-flex justify-content-center gap-1">
                    <button 
                      class="btn btn-warning btn-sm tooltip-custom" 
                      @click="editarPersonal(persona)"
                      data-tooltip="Editar Personal"
                    >
                      <i class="bi bi-pencil"></i>
                    </button>
                    <button 
                      class="btn btn-info btn-sm tooltip-custom" 
                      @click="verDetalles(persona)"
                      data-tooltip="Ver Detalles"
                    >
                      <i class="bi bi-eye"></i>
                    </button>
                    <button 
                      :class="['btn', persona.Estado === 'Activo' ? 'btn-danger' : 'btn-success', 'tooltip-custom']" 
                      @click="toggleEstado(persona._id, persona.Estado)"
                      :data-tooltip="persona.Estado === 'Activo' ? 'Desactivar' : 'Activar'"
                    >
                      <i :class="persona.Estado === 'Activo' ? 'bi bi-x-circle' : 'bi bi-check-circle'"></i>
                    </button>
                    <button 
                      class="btn btn-danger btn-sm tooltip-custom" 
                      @click="eliminarPersonal(persona._id)"
                      data-tooltip="Eliminar Personal"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                  </div>
                </td>
              </tr>
              <tr v-if="personalFiltrado.length === 0">
                <td colspan="7" class="text-center py-4">
                  <div class="text-muted">
                    <i class="bi bi-search fs-1 d-block mb-3"></i>
                    <h5>No se encontró personal</h5>
                    <p>Intenta ajustar los filtros de búsqueda</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Formulario de Personal -->
    <div v-if="showForm" class="card shadow-lg mt-4">
      <div class="card-header custom-header">
        <h4 class="mb-0">
          <i class="bi bi-person-plus me-2"></i>
          {{ editMode ? 'Editar Personal' : 'Agregar Nuevo Personal' }}
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="submitPersonal" class="row g-3">
          <div class="col-md-6">
            <label for="rut" class="form-label">
              <i class="bi bi-card-text me-1"></i>Rut
            </label>
            <input 
              v-model="personalForm.RutPersonal" 
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
              v-model="personalForm.Nombre" 
              type="text" 
              id="nombre" 
              class="form-control" 
              placeholder="Nombre del personal"
              required
            />
          </div>
          <div class="col-md-6">
            <label for="apePat" class="form-label">
              <i class="bi bi-person me-1"></i>Apellido Paterno
            </label>
            <input 
              v-model="personalForm.ApePat" 
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
              v-model="personalForm.ApeMat" 
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
              v-model="personalForm.Email" 
              type="email" 
              id="email" 
              class="form-control" 
              placeholder="correo@ejemplo.com"
            />
          </div>
          <div class="col-md-6">
            <label for="cargo" class="form-label">
              <i class="bi bi-briefcase me-1"></i>Cargo
            </label>
            <select v-model="personalForm.Cargo" class="form-select" required>
              <option value="">Seleccionar cargo</option>
              <option value="Administrador">Administrador</option>
              <option value="Conserje">Conserje</option>
              <option value="Mantenimiento">Mantenimiento</option>
              <option value="Seguridad">Seguridad</option>
              <option value="Limpieza">Limpieza</option>
              <option value="Jardinería">Jardinería</option>
            </select>
          </div>
          <div class="col-md-6">
            <label for="fono1" class="form-label">
              <i class="bi bi-telephone me-1"></i>Teléfono Principal
            </label>
            <input 
              v-model="personalForm.Fono1" 
              type="tel" 
              id="fono1" 
              class="form-control" 
              placeholder="+56 9 1234 5678"
            />
          </div>
          <div class="col-md-6">
            <label for="estado" class="form-label">
              <i class="bi bi-toggle-on me-1"></i>Estado
            </label>
            <select v-model="personalForm.Estado" class="form-select" required>
              <option value="Activo">Activo</option>
              <option value="Inactivo">Inactivo</option>
            </select>
          </div>
          <div class="col-12">
            <div class="d-flex justify-content-end gap-2">
              <button type="button" class="btn btn-secondary" @click="cancelarFormulario">
                <i class="bi bi-x-circle me-2"></i>Cancelar
              </button>
              <button type="submit" class="btn btn-primary">
                <i class="bi bi-check-circle me-2"></i>
                {{ editMode ? 'Actualizar Personal' : 'Agregar Personal' }}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de detalles del personal -->
    <div class="modal fade" id="detallesPersonalModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">
              <i class="bi bi-person-badge me-2"></i>
              Detalles del Personal
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body" v-if="personalSeleccionado">
            <div class="row">
              <div class="col-md-4 text-center">
                <div class="avatar-large mb-3">
                  <i class="bi bi-person-badge" style="font-size: 4rem; color: var(--primary-color);"></i>
                </div>
                <h4>{{ personalSeleccionado.Nombre }} {{ personalSeleccionado.ApePat }} {{ personalSeleccionado.ApeMat }}</h4>
                <p class="text-muted">{{ personalSeleccionado.Cargo }}</p>
                <span :class="personalSeleccionado.Estado === 'Activo' ? 'estado-pagado' : 'estado-pendiente'">
                  {{ personalSeleccionado.Estado }}
                </span>
              </div>
              <div class="col-md-8">
                <div class="row g-3">
                  <div class="col-12">
                    <label class="fw-bold">Rut:</label>
                    <p>{{ personalSeleccionado.RutPersonal }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Email:</label>
                    <p>{{ personalSeleccionado.Email }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Cargo:</label>
                    <p>{{ personalSeleccionado.Cargo }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Teléfono:</label>
                    <p>{{ personalSeleccionado.Fono1 }}</p>
                  </div>
                  <div class="col-md-6">
                    <label class="fw-bold">Estado:</label>
                    <p>{{ personalSeleccionado.Estado }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-warning" @click="editarPersonal(personalSeleccionado)" data-bs-dismiss="modal">
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
      personal: [],
      personalFiltrado: [],
      personalForm: {
        RutPersonal: '',
        Nombre: '',
        ApePat: '',
        ApeMat: '',
        Email: '',
        Cargo: '',
        Fono1: '',
        Estado: 'Activo'
      },
      showPersonalList: false,
      showForm: false,
      editMode: false,
      currentPersonalId: null,
      busqueda: '',
      filtroEstado: '',
      personalSeleccionado: null,
    };
  },
  computed: {
    personalActivo() {
      return this.personal.filter(p => p.Estado === 'Activo').length;
    },
    personalInactivo() {
      return this.personal.filter(p => p.Estado === 'Inactivo').length;
    },
    cargosUnicos() {
      const cargos = new Set(this.personal.map(p => p.Cargo));
      return cargos.size;
    }
  },
  mounted() {
    // Cargar personal automáticamente al montar el componente
    this.mostrarPersonal();
  },
  methods: {
    async mostrarPersonal() {
      try {
        const response = await axios.get('http://localhost:5000/personal');
        this.personal = response.data;
        this.personalFiltrado = [...this.personal];
        this.showPersonalList = true;
        this.showForm = false;
      } catch (error) {
        console.error('Error al obtener el personal:', error);
        this.$alert.mostrarError('Error al cargar personal');
      }
    },

    agregarPersonalFormulario() {
      this.showPersonalList = false;
      this.showForm = true;
      this.resetForm();
      this.editMode = false;
    },

    async submitPersonal() {
      if (this.editMode) {
        await this.actualizarPersonal();
      } else {
        await this.agregarPersonal();
      }
    },

    async agregarPersonal() {
      try {
        const response = await axios.post('http://localhost:5000/personal', this.personalForm);
        console.log('Personal agregado:', response.data);
        this.$alert.mostrarExito('Personal agregado exitosamente');
        this.mostrarPersonal();
        this.resetForm();
      } catch (error) {
        console.error('Error al agregar personal:', error);
        this.$alert.mostrarError('Error al agregar personal');
      }
    },

    async actualizarPersonal() {
      try {
        const response = await axios.put(`http://localhost:5000/personal/${this.currentPersonalId}`, this.personalForm);
        console.log('Personal actualizado:', response.data);
        this.$alert.mostrarExito('Personal actualizado exitosamente');
        this.mostrarPersonal();
        this.resetForm();
      } catch (error) {
        console.error('Error al actualizar personal:', error);
        this.$alert.mostrarError('Error al actualizar personal');
      }
    },

    editarPersonal(persona) {
      this.personalForm = { ...persona };
      this.currentPersonalId = persona._id;
      this.editMode = true;
      this.showForm = true;
      this.showPersonalList = false;
    },

    async eliminarPersonal(id) {
      const confirmado = await this.$alert.confirm('¿Estás seguro de eliminar este personal?');
      if (confirmado) {
        try {
          const response = await axios.delete(`http://localhost:5000/personal/${id}`);
          console.log('Personal eliminado:', response.data);
          this.$alert.mostrarExito('Personal eliminado exitosamente');
          this.mostrarPersonal();
        } catch (error) {
          console.error('Error al eliminar personal:', error);
          this.$alert.mostrarError('Error al eliminar personal');
        }
      }
    },

    async toggleEstado(id, estadoActual) {
      const nuevoEstado = estadoActual === 'Activo' ? 'Inactivo' : 'Activo';
      try {
        const response = await axios.put(`http://localhost:5000/personal/${id}`, {
          ...this.personal.find(p => p._id === id),
          Estado: nuevoEstado
        });
        console.log('Estado actualizado:', response.data);
        this.$alert.mostrarExito(`Personal ${nuevoEstado.toLowerCase()} exitosamente`);
        this.mostrarPersonal();
      } catch (error) {
        console.error('Error al cambiar estado:', error);
        this.$alert.mostrarError('Error al cambiar estado');
      }
    },

    resetForm() {
      this.personalForm = {
        RutPersonal: '',
        Nombre: '',
        ApePat: '',
        ApeMat: '',
        Email: '',
        Cargo: '',
        Fono1: '',
        Estado: 'Activo'
      };
      this.editMode = false;
      this.currentPersonalId = null;
    },

    cancelarFormulario() {
      this.showForm = false;
      this.resetForm();
      if (this.personal.length > 0) {
        this.showPersonalList = true;
      }
    },

    filtrarPersonal() {
      this.aplicarFiltros();
    },

    filtrarPorEstado(estado) {
      this.filtroEstado = estado;
      this.aplicarFiltros();
    },

    aplicarFiltros() {
      let filtrado = [...this.personal];

      // Filtro por búsqueda
      if (this.busqueda) {
        const busquedaLower = this.busqueda.toLowerCase();
        filtrado = filtrado.filter(persona => 
          persona.Nombre.toLowerCase().includes(busquedaLower) ||
          persona.ApePat.toLowerCase().includes(busquedaLower) ||
          persona.ApeMat.toLowerCase().includes(busquedaLower) ||
          persona.RutPersonal.toLowerCase().includes(busquedaLower) ||
          persona.Email.toLowerCase().includes(busquedaLower) ||
          persona.Cargo.toLowerCase().includes(busquedaLower)
        );
      }

      // Filtro por estado
      if (this.filtroEstado) {
        filtrado = filtrado.filter(persona => persona.Estado === this.filtroEstado);
      }

      this.personalFiltrado = filtrado;
    },

    verDetalles(persona) {
      this.personalSeleccionado = persona;
      const modal = new Modal(document.getElementById('detallesPersonalModal'));
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

.btn-group .btn.active {
  background: white;
  color: var(--primary-color);
  border-color: white;
}
</style>
