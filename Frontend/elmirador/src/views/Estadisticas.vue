<template>
  <div class="container-fluid p-4">
    <h1 class="text-center mb-4">
      <i class="bi bi-bar-chart me-2"></i>Vista de Estadísticas
    </h1>

    <div class="row mb-4">
      <div class="col-md-3 mb-3">
        <div class="card shadow-sm h-100">
          <div class="card-body d-flex align-items-center">
            <i class="bi bi-people fs-2 me-3 text-primary"></i>
            <div>
              <h5 class="card-title mb-0">Residentes</h5>
              <div class="h3 mb-0">{{ getResidentesCount }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card shadow-sm h-100">
          <div class="card-body d-flex align-items-center">
            <i class="bi bi-person-badge fs-2 me-3 text-success"></i>
            <div>
              <h5 class="card-title mb-0">Personal</h5>
              <div class="h3 mb-0">{{ personalCount }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card shadow-sm h-100">
          <div class="card-body d-flex align-items-center">
            <i class="bi bi-cash-coin fs-2 me-3 text-warning"></i>
            <div>
              <h5 class="card-title mb-0">Gastos Comunes</h5>
              <div class="h3 mb-0">{{ gastosCount }}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3 mb-3">
        <div class="card shadow-sm h-100">
          <div class="card-body d-flex align-items-center">
            <i class="bi bi-file-text fs-2 me-3 text-info"></i>
            <div>
              <h5 class="card-title mb-0">Reportes</h5>
              <div class="h3 mb-0">{{ reportesCount }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm h-100">
          <div class="card-header custom-header text-white">
            <h4 class="mb-0"><i class="bi bi-pie-chart me-2"></i>Gráfico Gastos</h4>
          </div>
          <div class="card-body">
            <PageGraficoGastos />
          </div>
        </div>
      </div>
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm h-100">
          <div class="card-header custom-header text-white">
            <h4 class="mb-0"><i class="bi bi-flag me-2"></i>Gráfico Reclamos</h4>
          </div>
          <div class="card-body">
            <PageGraficoReclamos />
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm h-100">
          <div class="card-header custom-header text-white">
            <h4 class="mb-0"><i class="bi bi-cash-coin me-2"></i>Gráfico Pagos</h4>
          </div>
          <div class="card-body">
            <PageGraficoPagos />
          </div>
        </div>
      </div>
      <div class="col-md-6 mb-4">
        <div class="card shadow-sm h-100">
          <div class="card-header custom-header text-white">
            <h4 class="mb-0"><i class="bi bi-bar-chart-line me-2"></i>Gráfico General</h4>
          </div>
          <div class="card-body">
            <PageGraficoGeneral />
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-12 mb-4">
        <div class="card shadow-sm h-100">
          <div class="card-header custom-header text-white">
            <h4 class="mb-0"><i class="bi bi-people me-2"></i>Gráfico Residentes</h4>
          </div>
          <div class="card-body">
            <PageGraficoResidentes />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PageGraficoGastos from '@/components/GraficoGastos.vue'
import PageGraficoGeneral from '@/components/GraficoGeneral.vue'
import PageGraficoPagos from '@/components/GraficoPagos.vue'
import PageGraficoReclamos from '@/components/GraficoReclamos.vue'
import PageGraficoResidentes from '@/components/GraficoResidentes.vue'
import { mapGetters } from 'vuex';

export default {
  name: 'PageEstadistica',
  components: {
    PageGraficoGastos,
    PageGraficoGeneral,
    PageGraficoPagos,
    PageGraficoReclamos,
    PageGraficoResidentes,
  },
  computed: {
    ...mapGetters(['getResidentesCount']),
  },
  data() {
    return {
      personalCount: 2,
      gastosCount: 10,
      reportesCount: 3,
    };
  },
};

</script>

<style scoped>
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.custom-header {
  background-color: #008E63;
  color: white;
}
</style>