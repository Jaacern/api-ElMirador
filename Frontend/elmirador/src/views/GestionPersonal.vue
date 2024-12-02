<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-person-badge me-2"></i>Gestión de Personal
    </h1>

    <!-- Botones de acción -->
    <div class="row justify-content-center mb-4">
      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Personal Actions">
          <button class="btn btn-primary" @click="mostrarPersonal">
            <i class="bi bi-list-ul me-1"></i>Mostrar Personal
          </button>
          <button class="btn btn-success" @click="agregarPersonalFormulario">
            <i class="bi bi-plus-circle me-1"></i>Agregar Personal
          </button>
        </div>
      </div>
    </div>
<!-- Lista de Personal -->
<div v-if="showPersonalList" class="card shadow-sm">
  <div class="card-header custom-header text-white d-flex justify-content-between align-items-center">
    <h4 class="mb-0">
      <i class="bi bi-list-check me-2"></i>Lista de Personal
    </h4>
    <span class="badge bg-light text-dark">Total: {{ personal.length }}</span>
  </div>
  <div class="card-body p-0">
    <div class="table-responsive">
      <table class="table table-striped table-hover mb-0">
        <thead class="table-light">
          <tr>
            <th>#</th>
            <th>Nombre Completo</th>
            <th>Correo</th>
            <th>Cargo</th>
            <th>Estado</th> <!-- Nueva columna para estado -->
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(persona, index) in personal" :key="persona._id">
            <td>{{ index + 1 }}</td>
            <td>{{ persona.Nombre }} {{ persona.ApePat }} {{ persona.ApeMat }}</td>
            <td>{{ persona.Email }}</td>
            <td>{{ persona.Cargo }}</td>
            <!-- Mostrar estado como texto y color -->
            <td>
              <span :class="persona.Estado === 'Activo' ? 'btn btn-success btn-sm' : 'btn btn-secondary btn-sm'">
                {{ persona.Estado }}
              </span>
            </td>
            <td>
              <div class="btn-group btn-group-sm" role="group">
                <button 
                  class="btn btn-warning" 
                  @click="editarPersonal(persona)"
                  title="Editar"
                >
                  <i class="bi bi-pencil"></i>
                </button>
                <button 
                  class="btn btn-danger" 
                  @click="eliminarPersonal(persona._id)"
                  title="Eliminar"
                >
                  <i class="bi bi-trash"></i>
                </button>
                <!-- Botón para cambiar el estado -->
                <button 
                  class="btn" 
                  :class="persona.Estado === 'Activo' ? 'btn-danger' : 'btn-success'" 
                  @click="toggleEstado(persona._id, persona.Estado)" 
                  title="Cambiar Estado"
                >
                  <i class="bi" :class="persona.Estado === 'Activo' ? 'bi-x-circle' : 'bi-check-circle'"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>


    <!-- Formulario de Personal -->
    <div v-if="showForm" class="card shadow-sm mt-4">
      <div class="card-header custom-header text-white">
        <h4 class="mb-0">
          <i class="bi bi-plus-square me-2"></i>
          {{ editMode ? 'Editar Personal' : 'Nuevo Personal' }}
        </h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="submitPersonal">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="rut" class="form-label">Rut</label>
              <input 
                v-model="personalForm.RutPersonal" 
                type="text" 
                id="rut" 
                class="form-control" 
                required 
                placeholder="Rut del personal"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="nombre" class="form-label">Nombre</label>
              <input 
                v-model="personalForm.Nombre" 
                type="text" 
                id="nombre" 
                class="form-control" 
                required 
                placeholder="Nombre del personal"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="apePat" class="form-label">Apellido Paterno</label>
              <input 
                v-model="personalForm.ApePat" 
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
                v-model="personalForm.ApeMat" 
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
                v-model="personalForm.Email" 
                type="email" 
                id="email" 
                class="form-control" 
                required 
                placeholder="correo@ejemplo.com"
              />
            </div>
            <div class="col-md-6 mb-3">
              
  <label for="cargo" class="form-label">Cargo</label>
  <select 
    v-model="personalForm.Cargo" 
    id="cargo" 
    class="form-select" 
    required
  >
    <option value="" disabled selected>Seleccione un cargo</option>
    <option value="Administrador del Edificio">Administrador del Edificio</option>
    <option value="Conserje">Conserje</option>
    <option value="Guardia de Seguridad">Guardia de Seguridad</option>
    <option value="Encargado de Mantención">Encargado de Mantención</option>
    <option value="Jardinero">Jardinero</option>
    <option value="Auxiliar de Aseo">Auxiliar de Aseo</option>
    <option value="Encargado de Recepción">Encargado de Recepción</option>
    <option value="Técnico en Servicios Generales">Técnico en Servicios Generales</option>
  </select>
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
// Aquí se importa el código y métodos necesarios para gestionar el personal
import axios from 'axios';

export default {
  data() {
    return {
      personal: [],
      personalForm: {
        RutPersonal: '',
        Nombre: '',
        ApePat: '',
        ApeMat: '',
        Email: '',
        Cargo: '',
        Fono1: '',
        Estado: 'Inactivo', 
      },
      showPersonalList: false,
      showForm: false,
      editMode: false,
      currentPersonalId: null,
    };
  },
  mounted() {
    this.mostrarPersonal();
  },
  methods: {
  // Mostrar la lista de personal
  async mostrarPersonal() {
    try {
      const response = await axios.get('http://localhost:5000/personal');
      this.personal = response.data;
      this.showPersonalList = true;
      this.showForm = false;
    } catch (error) {
      console.error('Error al obtener el personal:', error);
    }
  },
  
  // Agregar personal desde el formulario
  agregarPersonalFormulario() {
    this.resetForm();
    this.showForm = true;
    this.showPersonalList = false;
  },
  
  // Enviar el formulario (agregar o actualizar personal)
  async submitPersonal() {
    if (this.editMode) {
      await this.actualizarPersonal();
    } else {
      await this.agregarPersonal();
    }
  },
  
  // Agregar nuevo personal
  async agregarPersonal() {
    try {
      // Asegurarse que el estado por defecto es "Inactivo"
      this.personalForm.Estado = 'Inactivo';
      await axios.post('http://localhost:5000/personal', this.personalForm);
      alert('Personal agregado exitosamente');
      this.mostrarPersonal();
    } catch (error) {
      alert('Error al agregar personal');
    }
  },
  
  // Actualizar información de un personal existente
  async actualizarPersonal() {
    try {
      await axios.put(`http://localhost:5000/personal/${this.currentPersonalId}`, this.personalForm);
      alert('Personal actualizado exitosamente');
      this.mostrarPersonal();
    } catch (error) {
      alert('Error al actualizar personal');
    }
  },
  
  // Editar un personal
  editarPersonal(persona) {
    this.personalForm = { ...persona };
    this.editMode = true;
    this.showForm = true;
    this.currentPersonalId = persona._id;
    this.showPersonalList = false;
  },
  
  // Eliminar un personal
  async eliminarPersonal(id) {
    if (confirm('¿Eliminar este registro?')) {
      try {
        await axios.delete(`http://localhost:5000/personal/${id}`);
        alert('Personal eliminado exitosamente');
        this.mostrarPersonal();
      } catch (error) {
        alert('Error al eliminar personal');
      }
    }
  },
  
  // Restablecer el formulario
  resetForm() {
    this.personalForm = {
      RutPersonal: '',
      Nombre: '',
      ApePat: '',
      ApeMat: '',
      Email: '',
      Cargo: '',
      Estado: 'Inactivo',  // Estado por defecto cuando se agrega un nuevo personal
    };
    this.editMode = false;
    this.currentPersonalId = null;
  },
  
  // Cancelar el formulario
  cancelarFormulario() {
    this.resetForm();
    this.showPersonalList = true;
    this.showForm = false;
  },
  
  // Cambiar el estado de un personal (Activo o Inactivo)
  async toggleEstado(id, estadoActual) {
    const nuevoEstado = estadoActual === 'Activo' ? 'Inactivo' : 'Activo';
    try {
      const response = await axios.put(`http://localhost:5000/personal/${id}`, { Estado: nuevoEstado });
      console.log('Estado actualizado:', response.data);
      this.mostrarPersonal(); // Recargar la lista de personal
    } catch (error) {
      console.error('Error al cambiar el estado:', error);
      alert('Hubo un error al cambiar el estado del personal');
    }
  }
}

};
</script>

<style scoped>
.btn-group button {
  margin-right: 5px;
}
.table td, .table th {
  vertical-align: middle;
}
.table-responsive {
  overflow-x: auto;
}
.custom-header {
  background-color: #008E63;
  color: white;
}

</style>
