
<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-people me-2"></i>Gestión de Residentes
    </h1>

    <!-- Botones de acción con Bootstrap Grid -->
    <div class="row justify-content-center mb-4">
      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Resident Actions">
          <button class="btn btn-primary" @click="mostrarResidentess">
            <i class="bi bi-list-ul me-1"></i>Mostrar Residentes
          </button>
          <button class="btn btn-success" @click="agregarResidenteFormulario">
            <i class="bi bi-plus-circle me-1"></i>Agregar Residente
          </button>
        </div>
      </div>
    </div>

    <!-- Lista de Residentes -->
    <div v-if="showResidentList" class="card shadow-sm">
      <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
        <h4 class="mb-0">
          <i class="bi bi-list-check me-2"></i>Lista de Residentes
        </h4>
        <span class="badge bg-light text-dark">Total: {{ residentes.length }}</span>
      </div>
      <div class="card-body p-0">
        <div class="table-responsive">
          <table class="table table-striped table-hover mb-0">
            <thead class="table-light">
              <tr>
                <th>#</th>
                <th>Nombre Completo</th>
                <th>Rut</th>
                <th>Email</th>
                <th>Departamento</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(residente, index) in residentes" :key="residente._id">
                <td>{{ index + 1 }}</td>
                <td>{{ residente.Nombre }} {{ residente.ApePat }} {{ residente.ApeMat }}</td>
                <td>{{ residente.RutArre }}</td>
                <td>{{ residente.Email }}</td>
                <td>{{ residente.nro_departamento }}</td>
                <td>
                  <div class="btn-group btn-group-sm" role="group">
                    <button 
                      class="btn btn-warning" 
                      @click="editarResidente(residente)"
                      title="Editar"
                    >
                      <i class="bi bi-pencil"></i>
                    </button>
                    <button 
                      class="btn btn-danger" 
                      @click="eliminarResidente(residente._id)"
                      title="Eliminar"
                    >
                      <i class="bi bi-trash"></i>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Formulario de Residentes -->
    <div v-if="showForm" class="card shadow-sm mt-4">
      <div class="card-header bg-primary text-white">
        <h4 class="mb-0">
          <i class="bi bi-plus-square me-2"></i>
          {{ editMode ? 'Editar Residente' : 'Nuevo Residente' }}
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="submitResidente">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="rut" class="form-label">Rut</label>
              <input 
                v-model="residenteForm.RutArre" 
                type="text" 
                id="rut" 
                class="form-control" 
                required 
                placeholder="Rut del residente"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="nombre" class="form-label">Nombre</label>
              <input 
                v-model="residenteForm.Nombre" 
                type="text" 
                id="nombre" 
                class="form-control" 
                required 
                placeholder="Nombre del residente"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="apePat" class="form-label">Apellido Paterno</label>
              <input 
                v-model="residenteForm.ApePat" 
                type="text" 
                id="apePat" 
                class="form-control" 
                required 
                placeholder="Apellido paterno"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="apeMat" class="form-label">Apellido Materno</label>
              <input 
                v-model="residenteForm.ApeMat" 
                type="text" 
                id="apeMat" 
                class="form-control" 
                required 
                placeholder="Apellido materno"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="email" class="form-label">Email</label>
              <input 
                v-model="residenteForm.Email" 
                type="email" 
                id="email" 
                class="form-control" 
                required 
                placeholder="correo@ejemplo.com"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="departamento" class="form-label">Departamento</label>
              <input 
                v-model="residenteForm.nro_departamento" 
                type="text" 
                id="departamento" 
                class="form-control" 
                required 
                placeholder="Número de departamento"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="fono1" class="form-label">Teléfono 1</label>
              <input 
                v-model="residenteForm.Fono1" 
                type="tel" 
                id="fono1" 
                class="form-control" 
                placeholder="+569 12345678"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="fono2" class="form-label">Teléfono 2 (Opcional)</label>
              <input 
                v-model="residenteForm.Fono2" 
                type="tel" 
                id="fono2" 
                class="form-control" 
                placeholder="+569 12345678"
              />
            </div>
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
import { mapActions } from 'vuex';

export default {
  // El código del script permanece exactamente igual al original
  // Se copia y pega el script completo del documento original
  data() {
    return {
      residentes: [], 
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
    };
  },
  mounted() {
    this.mostrarResidentess();
  },
  methods: {
    ...mapActions(['updateResidentesCount']),
    async mostrarResidentess() {
      try {
        const response = await axios.get('http://localhost:5000/residentes');
        this.residentes = response.data;
        this.showResidentList = true;
        this.showForm = false;
        this.updateResidentesCount(this.residentes.length); // Actualiza el estado global
      } catch (error) {
        console.error('Error al obtener los residentes:', error);
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
        alert('Residente agregado exitosamente');
        this.mostrarResidentess();
        this.resetForm();
      } catch (error) {
        console.error('Error al agregar residente:', error);
        alert('Hubo un error al agregar el residente');
      }
    },

    async actualizarResidente() {
      try {
        const response = await axios.put(`http://localhost:5000/residentes/${this.currentResidenteId}`, this.residenteForm);
        console.log('Residente actualizado:', response.data);
        alert('Residente actualizado exitosamente');
        this.mostrarResidentess();
        this.resetForm();
      } catch (error) {
        console.error('Error al actualizar residente:', error);
        alert('Hubo un error al actualizar el residente');
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
      if (confirm('¿Estás seguro de eliminar este residente?')) {
        try {
          const response = await axios.delete(`http://localhost:5000/residentes/${id}`);
          console.log('Residente eliminado:', response.data);
          alert('Residente eliminado exitosamente');
          this.mostrarResidentess();
        } catch (error) {
          console.error('Error al eliminar residente:', error);
          alert('Hubo un error al eliminar el residente');
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
      this.resetForm();
      this.showResidentList = true;
      this.showForm = false;
    }
  },
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
</style>