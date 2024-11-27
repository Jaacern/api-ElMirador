<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-tools me-2"></i>Configuración de la Página
    </h1>

    <!-- Menú principal de herramientas -->
    <div class="row justify-content-center mb-4">
      <div class="col-auto">
        <div class="btn-group" role="group" aria-label="Configuraciones">
          <button class="btn btn-primary" @click="mostrarTab('colores')">
            <i class="bi bi-palette me-1"></i>Colores
          </button>
          <button class="btn btn-secondary" @click="mostrarTab('notificaciones')">
            <i class="bi bi-bell me-1"></i>Notificaciones
          </button>
          <button class="btn btn-success" @click="mostrarTab('perfil')">
            <i class="bi bi-person-circle me-1"></i>Perfil
          </button>
          <button class="btn btn-warning" @click="mostrarTab('datos')">
            <i class="bi bi-folder me-1"></i>Datos
          </button>
        </div>
      </div>
    </div>

    <!-- Contenido de configuración -->
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <!-- Tarjeta de Colores -->
        <div v-if="tabActual === 'colores'" class="card shadow-sm fade" :class="{ show: tabActual === 'colores' }">
          <div class="card-header bg-primary text-white">
            <h4><i class="bi bi-palette me-2"></i>Colores</h4>
          </div>
          <div class="card-body">
            <p>Cambia el esquema de colores de la página:</p>
            <div class="form-check">
              <input 
                class="form-check-input" 
                type="radio" 
                id="lightMode" 
                value="light" 
                v-model="config.colores">
              <label class="form-check-label" for="lightMode">Modo Claro</label>
            </div>
            <div class="form-check">
              <input 
                class="form-check-input" 
                type="radio" 
                id="darkMode" 
                value="dark" 
                v-model="config.colores">
              <label class="form-check-label" for="darkMode">Modo Oscuro</label>
            </div>
          </div>
        </div>

        <!-- Tarjeta de Notificaciones -->
        <div v-if="tabActual === 'notificaciones'" class="card shadow-sm fade" :class="{ show: tabActual === 'notificaciones' }">
          <div class="card-header bg-secondary text-white">
            <h4><i class="bi bi-bell me-2"></i>Notificaciones</h4>
          </div>
          <div class="card-body">
            <p>Configura tus notificaciones:</p>
            <div class="form-check">
              <input 
                class="form-check-input" 
                type="checkbox" 
                id="emailNotifications" 
                v-model="config.notificaciones.email">
              <label class="form-check-label" for="emailNotifications">Correo Electrónico</label>
            </div>
            <div class="form-check">
              <input 
                class="form-check-input" 
                type="checkbox" 
                id="pushNotifications" 
                v-model="config.notificaciones.push">
              <label class="form-check-label" for="pushNotifications">Notificaciones Push</label>
            </div>
          </div>
        </div>

        <!-- Tarjeta de Perfil -->
        <div v-if="tabActual === 'perfil'" class="card shadow-sm fade" :class="{ show: tabActual === 'perfil' }">
          <div class="card-header bg-success text-white">
            <h4><i class="bi bi-person-circle me-2"></i>Perfil</h4>
          </div>
          <div class="card-body">
            <div class="mb-3">
              <label class="form-label">Nombre</label>
              <input 
                type="text" 
                class="form-control" 
                v-model="config.perfil.nombre" 
                placeholder="Tu nombre">
            </div>
            <div class="mb-3">
              <label class="form-label">Foto de Perfil</label>
              <input 
                type="file" 
                class="form-control" 
                @change="cargarFotoPerfil">
            </div>
          </div>
        </div>

        <!-- Tarjeta de Datos -->
        <div v-if="tabActual === 'datos'" class="card shadow-sm fade" :class="{ show: tabActual === 'datos' }">
          <div class="card-header bg-warning text-white">
            <h4><i class="bi bi-folder me-2"></i>Datos</h4>
          </div>
          <div class="card-body">
            <button 
              class="btn btn-danger" 
              @click="borrarDatos">
              <i class="bi bi-trash me-1"></i>Eliminar Datos
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PageHerramientas',
  data() {
    return {
      tabActual: "colores",
      config: {
        colores: "light",
        notificaciones: {
          email: true,
          push: false,
        },
        perfil: {
          nombre: "",
          foto: null,
        },
      },
    };
  },
  methods: {
    mostrarTab(tab) {
      this.tabActual = tab;
    },
    cargarFotoPerfil(event) {
      const file = event.target.files[0];
      if (file) {
        this.config.perfil.foto = URL.createObjectURL(file);
        alert("Foto de perfil cargada.");
      }
    },
    borrarDatos() {
      if (confirm("¿Estás seguro de eliminar los datos?")) {
        this.config = {
          colores: "light",
          notificaciones: { email: true, push: false },
          perfil: { nombre: "", foto: null },
        };
        alert("Datos eliminados.");
      }
    },
  },
};
</script>

<style scoped>
/* Transiciones suaves */
.fade {
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}
.fade.show {
  opacity: 1;
}

.card-header h4 {
  margin: 0;
}

.btn-group > .btn {
  margin: 0 0.25rem;
}

h1 i {
  color: #007bff;
}
</style>
