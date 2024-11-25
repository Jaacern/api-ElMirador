<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="d-flex align-items-center">
      <!-- Ícono de edificio y texto El Mirador -->
      <i class="bi bi-building ml-2"></i>
      <a class="navbar-brand ml-2" href="#">El Mirador</a>
    </div>
    <div class="ml-auto d-flex align-items-center">
      <!-- Campo de búsqueda -->
      <input type="text" class="form-control form-control-sm" placeholder="Buscar..." style="width: 200px;">
      <!-- Íconos de notificación y mensaje -->
      <i class="bi bi-bell ml-3"></i>
      <i class="bi bi-envelope ml-3"></i>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'PageNavbar'
}
</script>
