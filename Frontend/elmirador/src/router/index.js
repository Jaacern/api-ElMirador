import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue';
import GestionResidentes from '../views/GestionResidentes.vue';
import GestionPersonal from '../views/GestionPersonal.vue';
import GastosComunes from '../views/GastosComunes.vue';
import Estadisticas from '../views/Estadisticas.vue';
import Reportes from '../views/Reportes.vue';
import Herramientas from '../views/Herramientas.vue';

const routes = [
  { path: '/', component: Home }, // Landing page
  { path: '/login', component: Login },
  { 
    path: '/dashboard', 
    component: Dashboard,
    children: [
      { path: '', component: GestionResidentes }, // Dashboard principal
      { path: 'gestion-residentes', component: GestionResidentes },
      { path: 'gestion-personal', component: GestionPersonal },
      { path: 'gastos-comunes', component: GastosComunes },
      { path: 'estadisticas', component: Estadisticas },
      { path: 'reportes', component: Reportes },
      { path: 'herramientas', component: Herramientas }
    ]
  },
  // Rutas directas para compatibilidad
  { path: '/gestion-residentes', component: Dashboard },
  { path: '/gestion-personal', component: Dashboard },
  { path: '/gastos-comunes', component: Dashboard },
  { path: '/estadisticas', component: Dashboard },
  { path: '/reportes', component: Dashboard },
  { path: '/herramientas', component: Dashboard }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
