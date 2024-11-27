import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store/store'; // Importa el store desde src/store/store.js
import 'bootstrap/dist/css/bootstrap.min.css'; // Asegúrate de que Bootstrap está incluido
import './assets/styles.css'; // Archivo de estilos personalizados para el dark theme
import 'bootstrap-icons/font/bootstrap-icons.css';

// Crea la aplicación y utiliza tanto el router como el store
createApp(App)
  .use(router)
  .use(store) // Registra el store
  .mount('#app');
