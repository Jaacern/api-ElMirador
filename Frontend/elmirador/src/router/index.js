import { createRouter, createWebHistory } from 'vue-router';
import GestionResidentes from '../views/GestionResidentes.vue';
import GestionPersonal from '../views/GestionPersonal.vue';
import GastosComunes from '../views/GastosComunes.vue';
import Estadisticas from '../views/Estadisticas.vue';
import Reportes from '../views/Reportes.vue';
import Herramientas from '../views/Herramientas.vue';

const routes = [
  { path: '/', component: GestionResidentes }, // Ruta predeterminada
  { path: '/gestion-residentes', component: GestionResidentes },
  { path: '/gestion-personal', component: GestionPersonal },
  { path: '/gastos-comunes', component: GastosComunes },
  { path: '/estadisticas', component: Estadisticas },
  { path: '/reportes', component: Reportes },
  { path: '/herramientas', component: Herramientas }
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
