<template>
  <div id="app" style="display: flex; flex-direction: column; height: 100vh;">
    <Navbar />
    <div class="d-flex" style="flex-grow: 1; margin-top: 70px;"> <!-- El margen superior asegura que el contenido no se superponga al navbar -->
      <Sidebar />
      <div class="flex-grow-1" style="overflow-y: auto; padding: 10px; margin-left: 250px; height: 100%;"> <!-- Contenido desplazable debajo del navbar, desplazamiento solo para el contenido -->
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import Sidebar from './components/Sidebar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Sidebar
  }
}
</script>

<style>
/* Para asegurar que todo se acomode bien en la pantalla */
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.d-flex {
  display: flex;
}

.flex-grow-1 {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 10px;
}

/* Aseguramos que el navbar no tape el contenido */
.navbar {
  z-index: 1000;
}

/* Estilo para el sidebar fijo */
.sidebar {
  position: fixed;  /* Fijamos el sidebar en el lado izquierdo */
  width: 250px;
  background-color: #343a40;
  color: white;
  min-height: 100vh;
  top: 0px; /* Lo dejamos debajo del navbar */
  bottom: 0;
}

/* Estilos para el contenido */
.router-view {
  flex-grow: 1;
  background-color: #f8f9fa;
  padding: 20px;
  margin-left: 0px; /* Espacio para que no se solape con el sidebar */
  height: 100%;
}
</style>
