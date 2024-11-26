<template>
    <div>
      <h1>Gráfico Residentes</h1>
      <canvas ref="myLineChart"></canvas> <!-- El canvas donde se renderizará el gráfico -->
    </div>
  </template>
  
  <script>
  // Importamos las dependencias necesarias para Chart.js
  import { Chart as ChartJS, LineController, LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend } from 'chart.js';
  
  // Registramos todos los componentes necesarios de Chart.js
  ChartJS.register(LineController, LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);
  
  export default {
    name: 'PageGraficoResidentes',
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
      // Función para crear y configurar el gráfico Line
      createLineChart() {
        // Definimos la cantidad de datos y el rango
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
              fill: true, // Llena el área debajo de la línea
            },
            {
              label: 'Dataset 2',
              data: this.generateRandomData(DATA_COUNT, MIN_VALUE, MAX_VALUE), // Usamos la función para generar datos aleatorios
              borderColor: 'rgba(54, 162, 235, 1)', // Color del borde (azul)
              backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo con opacidad (azul claro)
              fill: true, // Llena el área debajo de la línea
            }
          ]
        };
  
        const config = {
          type: 'line',
          data: data,
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Gráfico de Línea de Residentes'
              }
            }
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
  