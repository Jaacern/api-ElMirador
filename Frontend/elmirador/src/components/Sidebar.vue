<template>
    <div class="sidebar">
      <ul class="nav flex-column">
        <!-- Título Panel -->
        <li class="nav-item">
          <span class="sidebar-title">Panel</span>
        </li>
        <!-- Opciones del sidebar -->
        <li class="nav-item">
          <router-link to="/gestion-residentes" class="nav-link" :class="{ active: isActive('/gestion-residentes') }">
            <i class="bi bi-person"></i> Gestion Residentes
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/gestion-personal" class="nav-link" :class="{ active: isActive('/gestion-personal') }">
            <i class="bi bi-person-lines-fill"></i> Gestion Personal
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/gastos-comunes" class="nav-link" :class="{ active: isActive('/gastos-comunes') }">
            <i class="bi bi-cash-stack"></i> Gastos Comunes
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/estadisticas" class="nav-link" :class="{ active: isActive('/estadisticas') }">
            <i class="bi bi-bar-chart"></i> Estadísticas
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/reportes" class="nav-link" :class="{ active: isActive('/reportes') }">
            <i class="bi bi-file-earmark-text"></i> Reportes
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/herramientas" class="nav-link" :class="{ active: isActive('/herramientas') }">
            <i class="bi bi-gear"></i> Herramientas
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PageSidebar',
    methods: {
      // Método para verificar si la ruta es activa
      isActive(route) {
        return this.$route.path === route;
      }
    }
  }
  </script>
  