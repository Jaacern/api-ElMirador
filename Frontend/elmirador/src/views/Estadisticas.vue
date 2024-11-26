<!-- src/views/Estadistica.vue -->
<template>
  <div>
    <h2>Vista de Estadísticas</h2>
    <PageGraficoGastos />
    <PageGraficoGeneral />
    <PageGraficoPagos/>
    <PageGraficoReclamos />
    <PageGraficoResidentes/>
     <!-- Aquí usamos el componente PageGraficoGastos -->
  </div>
</template>

<script>

import PageGraficoGastos from '@/components/GraficoGastos.vue'
import PageGraficoGeneral from '@/components/GraficoGeneral.vue'
import PageGraficoPagos from '@/components/GraficoPagos.vue'
import PageGraficoReclamos from '@/components/GraficoReclamos.vue'
import PageGraficoResidentes from '@/components/GraficoResidentes.vue'

export default {
  name: 'PageEstadistica',
  components: {
    PageGraficoGastos ,
    PageGraficoGeneral,
    PageGraficoPagos,
    PageGraficoReclamos,
    PageGraficoResidentes,
     // Registra el componente correctamente
  }
}
</script>

<style scoped>
/* Estilos para la vista estadística */
</style>
