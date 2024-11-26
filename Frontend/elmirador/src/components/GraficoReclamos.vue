<template>
    <div>
      <h1>Gráfico Reclamos</h1>
      <canvas ref="myBarChart"></canvas> <!-- El canvas donde se renderizará el gráfico -->
    </div>
  </template>
  
  <script>
  // Importamos las dependencias necesarias para Chart.js
  import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend, BarController } from 'chart.js';
  
  // Registramos todos los componentes necesarios de Chart.js
  ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend, BarController);
  
  export default {
    name: 'PageGraficoReclamos',
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
      // Función para crear y configurar el gráfico de barras horizontal
      createBarChart() {
        const DATA_COUNT = 7;
        const MIN_VALUE = -100;
        const MAX_VALUE = 100;
  
        const data = {
          labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'], // Etiquetas para los meses
          datasets: [
            {
              label: 'Dataset 1',
              data: this.generateRandomData(DATA_COUNT, MIN_VALUE, MAX_VALUE), // Usamos la función para generar datos aleatorios
              borderColor: 'rgba(255, 99, 132, 1)', // Color del borde (rojo)
              backgroundColor: 'rgba(255, 99, 132, 0.2)', // Color de fondo con opacidad (rojo claro)
            },
            {
              label: 'Dataset 2',
              data: this.generateRandomData(DATA_COUNT, MIN_VALUE, MAX_VALUE), // Usamos la función para generar datos aleatorios
              borderColor: 'rgba(54, 162, 235, 1)', // Color del borde (azul)
              backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo con opacidad (azul claro)
            }
          ]
        };
  
        const config = {
          type: 'bar', // Tipo de gráfico de barras
          data: data,
          options: {
            indexAxis: 'y', // Configuración para gráfico de barras horizontal
            elements: {
              bar: {
                borderWidth: 2, // Grosor del borde de las barras
              }
            },
            responsive: true,
            plugins: {
              legend: {
                position: 'top', // Posición de la leyenda
              },
              title: {
                display: true,
                text: 'Gráfico de Barras Horizontal de Reclamos' // Título del gráfico
              }
            }
          },
        };
  
        // Creamos el gráfico usando el canvas de la referencia
        this.chart = new ChartJS(this.$refs.myBarChart, config);
      }
    },
    mounted() {
      // Cuando el componente se monta, se crea el gráfico
      this.createBarChart();
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
  