<template>
  <div>
    <h1>Gráfico Pagos - Neón</h1>
    <canvas ref="myDoughnutChart"></canvas> <!-- El canvas donde se renderizará el gráfico -->
  </div>
</template>

<script>
// Importamos las dependencias necesarias para Chart.js
import { Chart as ChartJS, ArcElement, Tooltip, Legend, DoughnutController } from 'chart.js';

// Registramos todos los componentes necesarios de Chart.js
ChartJS.register(ArcElement, Tooltip, Legend, DoughnutController);

export default {
  name: 'PageGraficoPagos',
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
    // Función para crear y configurar el gráfico Doughnut
    createDoughnutChart() {
      // Definimos la cantidad de datos y el rango
      const DATA_COUNT = 5;
      const MIN_VALUE = 0;
      const MAX_VALUE = 100;

      const data = {
        labels: ['Verde Neón', 'Morado Neón', 'Rosa Neón', 'Amarillo Neón', 'Azul Neón'],
        datasets: [
          {
            label: 'Dataset 1',
            data: this.generateRandomData(DATA_COUNT, MIN_VALUE, MAX_VALUE), // Usamos la función para generar datos aleatorios
            backgroundColor: [
              '#00e600', // Verde Neón más saturado
              '#9b00d1', // Morado Neón más saturado
              '#d100d1', // Rosa Neón más saturado
              '#b5ff00', // Amarillo Neón más saturado
              '#00e6e6'  // Azul Neón más saturado
            ],
            // Los colores de hover, haciendo los colores menos saturados
            hoverBackgroundColor: [
              'rgba(0, 230, 0, 0.6)',   // Verde Neón con menos saturación
              'rgba(155, 0, 209, 0.6)', // Morado Neón con menos saturación
              'rgba(209, 0, 209, 0.6)', // Rosa Neón con menos saturación
              'rgba(181, 255, 0, 0.6)', // Amarillo Neón con menos saturación
              'rgba(0, 230, 230, 0.6)'  // Azul Neón con menos saturación
            ],
          }
        ]
      };

      const config = {
        type: 'doughnut',
        data: data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Gráfico Doughnut con Colores Neón Saturados'
            }
          },
          hover: {
            mode: 'nearest',
            intersect: true,
          }
        },
      };

      // Creamos el gráfico usando el canvas de la referencia
      this.chart = new ChartJS(this.$refs.myDoughnutChart, config);
    }
  },
  mounted() {
    // Cuando el componente se monta, se crea el gráfico
    this.createDoughnutChart();
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
