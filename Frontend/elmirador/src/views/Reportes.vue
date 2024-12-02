<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-file-earmark-text me-2"></i>Gestión de Reclamos
    </h1>

    <!-- Botones de acción con Bootstrap Grid -->
    <div class="row justify-content-center mb-4">
      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Complaint Actions">
          <button class="btn btn-primary" @click="mostrarReclamos">
            <i class="bi bi-list-ul me-1"></i>Mostrar Reclamos
          </button>
          <button class="btn btn-success" @click="agregarReclamoFormulario">
            <i class="bi bi-plus-circle me-1"></i>Agregar Reclamo
          </button>
          
          <div class="btn-group" role="group">
            <button 
              type="button" 
              class="btn btn-info dropdown-toggle" 
              data-bs-toggle="dropdown" 
              aria-expanded="false"
            >
              <i class="bi bi-filter me-1"></i>Filtrar Estado
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#" @click="filtrarReclamos('Activo')">Activos</a></li>
              <li><a class="dropdown-item" href="#" @click="filtrarReclamos('Inactivo')">Inactivos</a></li>
              <li><a class="dropdown-item" href="#" @click="mostrarReclamos">Todos</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Lista de Reclamos -->
    <div v-if="showReclamosList" class="card shadow-sm">
      <div class="card-header custom-header text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-list-check me-2"></i>Lista de Reclamos
        </h4>
        <span class="badge bg-light text-dark">Total: {{ reclamos.length }}</span>
      </div>
      <div class="card-body p-0">
        <div class="table-responsive">
          <table class="table table-striped table-hover mb-0">
            <thead class="table-light">
              <tr>
                <th>#</th>
                <th>Título</th>
                <th>Categoría</th>
                <th>Descripción</th>
                <th>Nombre</th>
                <th>Urgencia</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(reclamo, index) in reclamos" :key="reclamo._id">
                <td>{{ index + 1 }}</td>
                <td>{{ reclamo.titulo }}</td>
                <td>
                  <span class="badge" :class="{
                    'bg-primary': reclamo.categoria === 'Mantención',
                    'bg-success': reclamo.categoria === 'Limpieza',
                    'bg-warning': reclamo.categoria === 'Seguridad',
                    'bg-secondary': reclamo.categoria === 'Otros'
                  }">
                    {{ reclamo.categoria }}
                  </span>
                </td>
                <td>{{ reclamo.descripcion.substring(0, 50) }}...</td>
                <td>{{ reclamo.nombre }}</td>
                <td>
                  <span class="badge" :class="{
                    'bg-success': reclamo.urgencia === 'Baja',
                    'bg-warning': reclamo.urgencia === 'Media',
                    'bg-danger': reclamo.urgencia === 'Alta'
                  }">
                    {{ reclamo.urgencia }}
                  </span>
                </td>
                <td>
                  <span class="badge" :class="{
                    'bg-success': reclamo.estado === 'Activo',
                    'bg-secondary': reclamo.estado === 'Inactivo'
                  }">
                    {{ reclamo.estado }}
                  </span>
                </td>
                <td>
                  <div class="btn-group btn-group-sm" role="group">
                    <button 
                      class="btn btn-warning" 
                      @click="editarReclamo(reclamo)"
                      title="Editar"
                    >
                      <i class="bi bi-pencil"></i>
                    </button>
                    <button 
                      class="btn btn-danger" 
                      @click="eliminarReclamo(reclamo._id)"
                      title="Eliminar"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                    <button 
                      v-if="reclamo.estado === 'Inactivo'" 
                      class="btn btn-success" 
                      @click="cambiarEstadoReclamo(reclamo._id, 'Activo')"
                      title="Activar"
                    >
                      <i class="bi bi-check-circle"></i>
                    </button>
                    <button 
                      v-if="reclamo.estado === 'Activo'" 
                      class="btn btn-secondary" 
                      @click="cambiarEstadoReclamo(reclamo._id, 'Inactivo')"
                      title="Desactivar"
                    >
                      <i class="bi bi-slash-circle"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Formulario de Reclamos -->
    <div v-if="showForm" class="card shadow-sm mt-4">
      <div class="card-header custom-header text-white">
        <h4 class="mb-0">
          <i class="bi bi-plus-square me-2"></i>
          {{ editMode ? 'Editar Reclamo' : 'Nuevo Reclamo' }}
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="submitReclamo">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="titulo" class="form-label">Título</label>
              <input 
                v-model="reclamoForm.titulo" 
                type="text" 
                id="titulo" 
                class="form-control" 
                required 
                placeholder="Título del reclamo"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="categoria" class="form-label">Categoría</label>
              <select 
                v-model="reclamoForm.categoria" 
                id="categoria" 
                class="form-select" 
                required
              >
                <option value="">Seleccionar Categoría</option>
                <option value="Mantención">Mantención</option>
                <option value="Limpieza">Limpieza</option>
                <option value="Seguridad">Seguridad</option>
                <option value="Otros">Otros</option>
              </select>
            </div>
          </div>

          <div class="mb-3">
            <label for="descripcion" class="form-label">Descripción</label>
            <textarea 
              v-model="reclamoForm.descripcion" 
              id="descripcion" 
              class="form-control" 
              rows="3" 
              required
              placeholder="Describa detalladamente su reclamo"
            ></textarea>
          </div>

          <div class="row">
            <div class="col-md-4 mb-3">
              <label for="ubicacion" class="form-label">Ubicación</label>
              <input 
                v-model="reclamoForm.ubicacion" 
                type="text" 
                id="ubicacion" 
                class="form-control" 
                placeholder="Ej: Edificio A, Piso 2"
              />
            </div>
            <div class="col-md-4 mb-3">
              <label for="urgencia" class="form-label">Urgencia</label>
              <select 
                v-model="reclamoForm.urgencia" 
                id="urgencia" 
                class="form-select" 
                required
              >
                <option value="">Seleccionar Urgencia</option>
                <option value="Baja">Baja</option>
                <option value="Media">Media</option>
                <option value="Alta">Alta</option>
              </select>
            </div>
            <div class="col-md-4 mb-3">
              <label for="fecha" class="form-label">Fecha</label>
              <input 
                v-model="reclamoForm.fecha" 
                type="date" 
                id="fecha" 
                class="form-control" 
                required 
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="nombre" class="form-label">Nombre</label>
              <input 
                v-model="reclamoForm.nombre" 
                type="text" 
                id="nombre" 
                class="form-control" 
                required 
                placeholder="Nombre completo"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="correo" class="form-label">Correo</label>
              <input 
                v-model="reclamoForm.correo" 
                type="email" 
                id="correo" 
                class="form-control" 
                required 
                placeholder="correo@ejemplo.com"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="telefono" class="form-label">Teléfono (Opcional)</label>
              <input 
                v-model="reclamoForm.telefono" 
                type="tel" 
                id="telefono" 
                class="form-control" 
                placeholder="+569 12345678"
              />
            </div>
            <div v-if="editMode" class="col-md-6 mb-3">
              <label for="estado" class="form-label">Estado</label>
              <select 
                v-model="reclamoForm.estado" 
                id="estado" 
                class="form-select"
              >
                <option value="Activo">Activo</option>
                <option value="Inactivo">Inactivo</option>
              </select>
            </div>
          </div>

          <div class="mb-3">
            <label for="archivos" class="form-label">Archivos (Opcional)</label>
            <input 
              type="file" 
              id="archivos" 
              class="form-control" 
              multiple 
              @change="handleFileUpload" 
            />
          </div>

          <div class="d-flex justify-content-between">
            <button type="submit" class="btn btn-primary">
              <i class="bi bi-save me-1"></i>
              {{ editMode ? 'Actualizar' : 'Guardar' }}
            </button>
            <button type="button" class="btn btn-secondary" @click="cancelarFormulario">
              <i class="bi bi-x-circle me-1"></i>Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PageReportes',
  data() {
    return {
      reclamos: [],
      reclamoForm: {
        titulo: '',
        categoria: '',
        descripcion: '',
        ubicacion: '',
        archivos: [],
        nombre: '',
        correo: '',
        telefono: '',
        fecha: '',
        urgencia: '',
        estado: 'Activo'
      },
      showReclamosList: true,
      showForm: false,
      editMode: false,
      currentReclamoId: null,
    };
  },
  mounted() {
    this.mostrarReclamos();
  },
  methods: {
    handleFileUpload(event) {
      const files = event.target.files;
      this.reclamoForm.archivos = [];
      for (let file of files) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.reclamoForm.archivos.push({
            nombre: file.name,
            base64: e.target.result
          });
        };
        reader.readAsDataURL(file);
      }
    },

    async mostrarReclamos() {
      try {
        const response = await axios.get('http://localhost:5000/reclamos');
        this.reclamos = response.data;
        this.showReclamosList = true;
        this.showForm = false;
      } catch (error) {
        console.error('Error al obtener los reclamos:', error);
        alert('Hubo un error al obtener los reclamos');
      }
    },

    async filtrarReclamos(estado) {
      try {
        const response = await axios.get('http://localhost:5000/reclamos', {
          params: { estado: estado }
        });
        this.reclamos = response.data;
        this.showReclamosList = true;
        this.showForm = false;
      } catch (error) {
        console.error('Error al filtrar reclamos:', error);
        alert('Hubo un error al filtrar los reclamos');
      }
    },

    agregarReclamoFormulario() {
      this.showReclamosList = false;
      this.showForm = true;
      this.resetForm();
      this.editMode = false;
    },

    async submitReclamo() {
      if (!this.reclamoForm.titulo || !this.reclamoForm.categoria) {
        alert('Por favor complete los campos obligatorios');
        return;
      }

      try {
        if (this.editMode) {
          await this.actualizarReclamo();
        } else {
          await this.agregarReclamo();
        }
      } catch (error) {
        console.error('Error al procesar reclamo:', error);
        alert('Hubo un error al procesar el reclamo');
      }
    },

    async agregarReclamo() {
      try {
        const response = await axios.post('http://localhost:5000/reclamos', this.reclamoForm);
        console.log('Reclamo agregado:', response.data);
        alert('Reclamo agregado exitosamente');
        this.mostrarReclamos();
        this.resetForm();
      } catch (error) {
        console.error('Error al agregar reclamo:', error);
        alert('Hubo un error al agregar el reclamo');
      }
    },

    async actualizarReclamo() {
      try {
        const response = await axios.put(`http://localhost:5000/reclamos/${this.currentReclamoId}`, this.reclamoForm);
        console.log('Reclamo actualizado:', response.data);
        alert('Reclamo actualizado exitosamente');
        this.mostrarReclamos();
        this.resetForm();
      } catch (error) {
        console.error('Error al actualizar reclamo:', error);
        alert('Hubo un error al actualizar el reclamo');
      }
    },

    editarReclamo(reclamo) {
      this.reclamoForm = { ...reclamo };
      this.currentReclamoId = reclamo._id;
      this.editMode = true;
      this.showForm = true;
      this.showReclamosList = false;
    },

    async eliminarReclamo(id) {
      if (confirm('¿Estás seguro de eliminar este reclamo?')) {
        try {
          const response = await axios.delete(`http://localhost:5000/reclamos/${id}`);
          console.log('Reclamo eliminado:', response.data);
          alert('Reclamo eliminado exitosamente');
          this.mostrarReclamos();
        } catch (error) {
          console.error('Error al eliminar reclamo:', error);
          alert('Hubo un error al eliminar el reclamo');
        }
      }
    },

    async cambiarEstadoReclamo(id, nuevoEstado) {
      try {
        const response = await axios.patch(`http://localhost:5000/reclamos/${id}/estado`, { estado: nuevoEstado });
        console.log('Estado del reclamo actualizado:', response.data);
        alert(`Reclamo ${nuevoEstado === 'Activo' ? 'activado' : 'desactivado'} exitosamente`);
        this.mostrarReclamos();
      } catch (error) {
        console.error('Error al cambiar el estado del reclamo:', error);
        alert('Hubo un error al cambiar el estado del reclamo');
      }
    },

    resetForm() {
      this.reclamoForm = {
        titulo: '',
        categoria: '',
        descripcion: '',
        ubicacion: '',
        archivos: [],
        nombre: '',
        correo: '',
        telefono: '',
        fecha: '',
        urgencia: '',
        estado: 'Activo'
      };
      this.editMode = false;
      this.currentReclamoId = null;
    },

    cancelarFormulario() {
      this.resetForm();
      this.showReclamosList = true;
      this.showForm = false;
    }
  }
};
</script>

<style scoped>
/* Estilos adicionales */
.table-responsive {
  max-height: 500px;
  overflow-y: auto;
}

.btn-group-sm > .btn {
  padding: 0.25rem 0.5rem;
  font-size: 0.75rem;
}

/* Mejoras de accesibilidad y diseño */
.form-label {
  font-weight: 600;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Transiciones suaves */
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