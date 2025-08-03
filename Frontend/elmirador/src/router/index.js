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
  // Rutas directas para compatibilidad - redirigir al dashboard con la ruta correcta
  { 
    path: '/gestion-residentes', 
    redirect: '/dashboard/gestion-residentes'
  },
  { 
    path: '/gestion-personal', 
    redirect: '/dashboard/gestion-personal'
  },
  { 
    path: '/gastos-comunes', 
    redirect: '/dashboard/gastos-comunes'
  },
  { 
    path: '/estadisticas', 
    redirect: '/dashboard/estadisticas'
  },
  { 
    path: '/reportes', 
    redirect: '/dashboard/reportes'
  },
  { 
    path: '/herramientas', 
    redirect: '/dashboard/herramientas'
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

// Guard de autenticación
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
  
  // Rutas públicas que no requieren autenticación
  const publicRoutes = ['/', '/login'];
  
  if (publicRoutes.includes(to.path)) {
    // Si está autenticado y va a login, redirigir al dashboard
    if (to.path === '/login' && isAuthenticated) {
      next('/dashboard');
      return;
    }
    next();
    return;
  }
  
  // Para rutas protegidas, verificar autenticación
  if (!isAuthenticated) {
    next('/login');
    return;
  }
  
  next();
});

export default router;
