<template>
  <div class="container mt-5">
    <!-- Títulos de las páginas -->
    <h2 v-if="currentPage === 'panel'">Panel de Administración</h2>
    <h2 v-if="currentPage === 'gestionResidentes'">Gestión de Residentes</h2>
    <h2 v-if="currentPage === 'gestionPersonal'">Gestión de Personal</h2>
    <h2 v-if="currentPage === 'gastosComunes'">Gastos Comunes</h2>
    <h2 v-if="currentPage === 'estadisticas'">Estadísticas</h2>
    <h2 v-if="currentPage === 'reportes'">Reportes</h2>
    <h2 v-if="currentPage === 'herramientas'">Herramientas</h2>

    <!-- Campo de búsqueda sin funcionalidad -->
    <div class="mt-3">
      <input
        type="text"
        class="form-control"
        placeholder="Buscar..."
        disabled
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "PageContent",
  props: {
    currentPage: String,  // Recibimos el nombre de la página actual como prop
  },
};
</script>

<style scoped>
/* Asegúrate de que el contenido tiene un fondo oscuro */
.container {
  background-color: #181818;
  color: #e0e0e0;
}

input[type="text"] {
  background-color: #333;
  color: #fff;
  border: 1px solid #444;
}

input[type="text"]:focus {
  border-color: #bb86fc;
}
</style>
