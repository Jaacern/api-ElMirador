<template>
    <div>
      <h1>Gráfico General</h1>
      <canvas ref="myPieChart"></canvas> <!-- El canvas donde se renderizará el gráfico -->
    </div>
  </template>
  
  <script>
  // Importamos las dependencias necesarias para Chart.js
  import { Chart as ChartJS, ArcElement, Tooltip, Legend, PieController } from 'chart.js';
  
  // Registramos todos los componentes necesarios para el gráfico de Pie
  ChartJS.register(ArcElement, Tooltip, Legend, PieController);
  
  export default {
    name: 'PageGraficoGeneral',
    data() {
      return {
        chart: null, // Referencia para el gráfico
      };
    },
    methods: {
      // Función para generar números aleatorios
      generateRandomData(count, min, max) {
        const data = [];
        for (let i = 0; i < count; i++) {
          data.push(Math.floor(Math.random() * (max - min + 1)) + min); // Genera números aleatorios entre min y max
        }
        return data;
      },
      // Función para crear y configurar el gráfico Pie
      createPieChart() {
        const DATA_COUNT = 5;
        const NUMBER_CFG = { count: DATA_COUNT, min: 0, max: 100 };
  
        const data = {
          labels: ['Red', 'Orange', 'Yellow', 'Green', 'Blue'],
          datasets: [
            {
              label: 'Dataset 1',
              data: this.generateRandomData(NUMBER_CFG.count, NUMBER_CFG.min, NUMBER_CFG.max), // Usamos la función para generar datos aleatorios
              backgroundColor: ['#FF5733', '#FF8D1A', '#FFEB3B', '#28A745', '#007BFF'], // Colores del gráfico
            }
          ]
        };
  
        const config = {
          type: 'pie', // Tipo de gráfico Pie
          data: data,
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top', // Posición de la leyenda
              },
              title: {
                display: true,
                text: 'Gráfico Pie de Colores', // Título del gráfico
              }
            }
          }
        };
  
        // Creamos el gráfico usando el canvas de la referencia
        this.chart = new ChartJS(this.$refs.myPieChart, config);
      }
    },
    mounted() {
      // Cuando el componente se monta, se crea el gráfico
      this.createPieChart();
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
  