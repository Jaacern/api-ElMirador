import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'; // Asegúrate de que Bootstrap está incluido
import './assets/styles.css'; // Archivo de estilos personalizados para el dark theme
import 'bootstrap-icons/font/bootstrap-icons.css';

createApp(App)
  .use(router)
  .mount('#app');
