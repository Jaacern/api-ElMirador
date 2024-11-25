<template>
    <div>
      <h1 class="text-center my-4">Gestión de Residentes</h1>
  
      <!-- Botones de acción para mostrar y agregar residentes, centrados -->
      <div class="d-flex justify-content-center mb-3">
        <button class="btn btn-primary mx-2" @click="mostrarResidentess">
          Mostrar Residentes
        </button>
        <button class="btn btn-success mx-2" @click="agregarResidenteFormulario">
          Agregar Residente
        </button>
      </div>
  
      <!-- Mostrar la lista de residentes -->
      <div v-if="showResidentList">
        <h3>Lista de Residentes</h3>
        <table class="table">
          <thead>
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
                <button class="btn btn-warning btn-sm" @click="editarResidente(residente)">
                  Editar
                </button>
                <button class="btn btn-danger btn-sm" @click="eliminarResidente(residente._id)">
                  Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <!-- Mostrar el formulario para agregar o editar residente -->
      <div v-if="showForm" class="mt-3">
        <h4>{{ editMode ? 'Editar Residente' : 'Agregar Nuevo Residente' }}</h4>
        <form @submit.prevent="submitResidente">
          <div class="mb-3">
            <label for="rut" class="form-label">Rut</label>
            <input v-model="residenteForm.RutArre" type="text" id="rut" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input v-model="residenteForm.Nombre" type="text" id="nombre" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="apePat" class="form-label">Apellido Paterno</label>
            <input v-model="residenteForm.ApePat" type="text" id="apePat" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="apeMat" class="form-label">Apellido Materno</label>
            <input v-model="residenteForm.ApeMat" type="text" id="apeMat" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input v-model="residenteForm.Email" type="email" id="email" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="fono1" class="form-label">Teléfono 1</label>
            <input v-model="residenteForm.Fono1" type="text" id="fono1" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="fono2" class="form-label">Teléfono 2</label>
            <input v-model="residenteForm.Fono2" type="text" id="fono2" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="departamento" class="form-label">Departamento</label>
            <input v-model="residenteForm.nro_departamento" type="text" id="departamento" class="form-control" />
          </div>
          <div class="mb-3">
            <button type="submit" class="btn btn-primary">
              {{ editMode ? 'Actualizar Residente' : 'Agregar Residente' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        residentes: [], // Para almacenar los residentes obtenidos del servidor
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
        showResidentList: false, // Flag para mostrar la lista de residentes
        showForm: false, // Flag para mostrar el formulario
        editMode: false, // Flag para saber si estamos editando o agregando
        currentResidenteId: null, // Para guardar el ID del residente a editar
      };
    },
    methods: {
      // Mostrar la lista de residentes
      async mostrarResidentess() {
        try {
          const response = await axios.get('http://localhost:5000/residentes');
          this.residentes = response.data;
          this.showResidentList = true;
          this.showForm = false; // Ocultamos el formulario cuando mostramos la lista
        } catch (error) {
          console.error('Error al obtener los residentes:', error);
        }
      },
  
      // Mostrar el formulario para agregar un nuevo residente
      agregarResidenteFormulario() {
        this.showResidentList = false; // Ocultamos la lista de residentes
        this.showForm = true; // Mostramos el formulario
        this.resetForm(); // Limpiamos el formulario
        this.editMode = false; // Aseguramos que estamos en modo de agregar
      },
  
      // Función para agregar o editar un residente
      async submitResidente() {
        if (this.editMode) {
          await this.actualizarResidente();
        } else {
          await this.agregarResidente();
        }
      },
  
      // Función para agregar un nuevo residente
      async agregarResidente() {
        try {
          const response = await axios.post('http://localhost:5000/residentes', this.residenteForm);
          console.log('Residente agregado:', response.data);
          alert('Residente agregado exitosamente');
          this.mostrarResidentess(); // Volver a mostrar la lista de residentes
          this.resetForm(); // Limpiar el formulario
        } catch (error) {
          console.error('Error al agregar residente:', error);
          alert('Hubo un error al agregar el residente');
        }
      },
  
      // Función para actualizar un residente existente
      async actualizarResidente() {
        try {
          const response = await axios.put(`http://localhost:5000/residentes/${this.currentResidenteId}`, this.residenteForm);
          console.log('Residente actualizado:', response.data);
          alert('Residente actualizado exitosamente');
          this.mostrarResidentess(); // Volver a mostrar la lista de residentes
          this.resetForm(); // Limpiar el formulario
        } catch (error) {
          console.error('Error al actualizar residente:', error);
          alert('Hubo un error al actualizar el residente');
        }
      },
  
      // Función para editar un residente
      editarResidente(residente) {
        this.residenteForm = { ...residente }; // Prellenamos el formulario con los datos del residente
        this.currentResidenteId = residente._id; // Guardamos el ID del residente que vamos a editar
        this.editMode = true; // Activamos el modo de edición
        this.showForm = true; // Mostramos el formulario
        this.showResidentList = false; // Ocultamos la lista de residentes
      },
  
      // Función para eliminar un residente
      async eliminarResidente(id) {
        if (confirm('¿Estás seguro de eliminar este residente?')) {
          try {
            const response = await axios.delete(`http://localhost:5000/residentes/${id}`);
            console.log('Residente eliminado:', response.data);
            alert('Residente eliminado exitosamente');
            this.mostrarResidentess(); // Volver a mostrar la lista de residentes
          } catch (error) {
            console.error('Error al eliminar residente:', error);
            alert('Hubo un error al eliminar el residente');
          }
        }
      },
  
      // Función para resetear el formulario
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
        this.editMode = false; // Desactivamos el modo de edición
        this.currentResidenteId = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .table {
    width: 100%;
    margin-top: 20px;
  }
  
  .btn-group {
    margin-bottom: 20px;
  }
  
  .d-flex {
    justify-content: center;
  }
  </style>
  