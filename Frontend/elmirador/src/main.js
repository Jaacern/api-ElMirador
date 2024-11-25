import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'; // Asegúrate de que Bootstrap está incluido
import './assets/styles.css'; // Archivo de estilos personalizados para el dark theme
import 'bootstrap-icons/font/bootstrap-icons.css';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale } from 'chart.js';
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,   // Para las líneas del gráfico
  PointElement,  // Para los puntos en las líneas
  CategoryScale, // Para la escala de categorías en el eje X
  LinearScale    // Para la escala lineal en el eje Y
);


createApp(App)
  .use(router)
  .mount('#app');
