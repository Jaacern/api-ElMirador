<template>
  <div>
    <h3>Estadisticas</h3>
    <!-- Usando el componente Line aquí -->
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale } from 'chart.js';

// Registra los componentes de Chart.js
ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale);

export default {
  name: "PageEstadisticas",
  components: {
    Line // Ahora el componente Line es utilizado
  },
  data() {
    return {
      chartData: {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        datasets: [
          {
            label: 'Datos de Gestión',
            data: [10, 20, 30, 40, 50],
            borderColor: ['#32CD32'], // Verde
            backgroundColor: ['rgba(50, 205, 50, 0.2)'],
            fill: true,
            tension: 0.4
          },
          {
            label: 'Datos Adicionales',
            data: [15, 25, 35, 45, 55],
            borderColor: ['#800080'], // Morado
            backgroundColor: ['rgba(128, 0, 128, 0.2)'],
            fill: true,
            tension: 0.4
          }
        ]
      },
      chartOptions: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Gráfico de Gestión Personal'
          },
          tooltip: {
            mode: 'index',
            intersect: false
          }
        }
      }
    };
  }
};
</script>

<style scoped>
canvas {
  display: block;
  margin: 0 auto;
}
</style>
