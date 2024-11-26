<template>
  <div>
    <h1>Gráfico Gastos</h1>
    <canvas ref="myLineChart"></canvas> <!-- El canvas donde se renderizará el gráfico -->
  </div>
</template>

<script>
// Importamos las dependencias necesarias para Chart.js
import { Chart as ChartJS, LineController, LineElement, LinearScale, TimeScale, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns'; // Importamos el adaptador de fecha para las escalas de tiempo

// Registramos los componentes necesarios para los gráficos de líneas
ChartJS.register(LineController, LineElement, LinearScale, TimeScale, Tooltip, Legend);

export default {
  name: 'PageGraficoGastos',
  data() {
    return {
      chart: null, // Referencia para el gráfico
    };
  },
  methods: {
    // Función para generar datos aleatorios
    generateRandomData(count, min, max) {
      const data = [];
      for (let i = 0; i < count; i++) {
        data.push(Math.floor(Math.random() * (max - min + 1)) + min); // Genera números aleatorios entre min y max
      }
      return data;
    },
    // Función para crear y configurar el gráfico de línea
    createLineChart() {
      const DATA_COUNT = 7;
      const data = {
        labels: [ // Fechas (en formato de fecha)
          new Date(0),
          new Date(1),
          new Date(2),
          new Date(3),
          new Date(4),
          new Date(5),
          new Date(6),
        ],
        datasets: [
          {
            label: 'Dataset 1',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            borderColor: 'rgba(255, 99, 132, 1)',
            fill: false,
            data: this.generateRandomData(DATA_COUNT, 0, 100),
          },
          {
            label: 'Dataset 2',
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            fill: false,
            data: this.generateRandomData(DATA_COUNT, 0, 100),
          },
        ],
      };

      const config = {
        type: 'line',
        data: data,
        options: {
          responsive: true,
          plugins: {
            title: {
              text: 'Gráfico de Línea de Gastos',
              display: true,
            },
          },
          scales: {
            x: {
              type: 'time', // Usamos una escala de tiempo en el eje X
              time: {
                unit: 'day', // Unidad de tiempo en días
                tooltipFormat: 'll', // Formato del tooltip
              },
              title: {
                display: true,
                text: 'Fecha',
              },
            },
            y: {
              title: {
                display: true,
                text: 'Valor',
              },
            },
          },
        },
      };

      // Creamos el gráfico usando el canvas de la referencia
      this.chart = new ChartJS(this.$refs.myLineChart, config);
    }
  },
  mounted() {
    // Cuando el componente se monta, se crea el gráfico
    this.createLineChart();
  },
  beforeUnmount() {
    // Limpiar el gráfico antes de desmontar el componente
    if (this.chart) {
      this.chart.destroy();
    }
  }
};
</script>

<style scoped>
/* Estilos para el canvas del gráfico */
canvas {
  width: 100%;
  height: 400px; /* Puedes ajustar la altura según lo necesites */
  border: 1px solid #ddd;
}
</style>
