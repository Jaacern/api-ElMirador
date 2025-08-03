import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store/store';
import { createPinia } from 'pinia';

// UI Libraries
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import '@fortawesome/fontawesome-free/css/all.css';

// PrimeVue
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-light-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

// Chart.js
import Chart from 'chart.js/auto';
window.Chart = Chart;

// Custom styles
import './assets/styles.css';
import './assets/design-system.css';

// Plugins
import alertPlugin from './plugins/alertPlugin.js';

// Create app
const app = createApp(App);
const pinia = createPinia();

app.use(router)
   .use(store)
   .use(pinia)
   .use(PrimeVue, {
     ripple: true,
     inputStyle: 'filled'
   })
   .use(alertPlugin)
   .mount('#app');
