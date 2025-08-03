<template>
  <aside 
    class="sidebar" 
    :class="{ 'sidebar-collapsed': sidebarCollapsed }"
    role="navigation"
    aria-label="Navegación principal"
  >
    <!-- Header del sidebar -->
    <header class="sidebar-header">
      <div class="logo-container">
        <i class="bi bi-building-fill logo-icon" aria-hidden="true"></i>
        <span class="logo-text" v-if="!sidebarCollapsed">El Mirador</span>
      </div>
      
      <!-- Botón para colapsar/expandir -->
      <button
        @click="toggleSidebar"
        class="sidebar-toggle"
        :aria-label="sidebarCollapsed ? 'Expandir menú' : 'Colapsar menú'"
        :aria-expanded="!sidebarCollapsed"
        type="button"
      >
        <i :class="sidebarCollapsed ? 'bi bi-chevron-right' : 'bi bi-chevron-left'" aria-hidden="true"></i>
      </button>
    </header>
    
    <!-- Navegación principal -->
    <nav class="sidebar-nav" role="navigation">
      <div class="nav-section">
        <h2 class="nav-section-title" v-if="!sidebarCollapsed">
          <i class="bi bi-grid-1x2-fill" aria-hidden="true"></i>
          Panel de Control
        </h2>
        
        <ul class="nav-list" role="list">
          <li class="nav-item" role="listitem">
            <router-link 
              to="/gestion-residentes" 
              class="nav-link" 
              :class="{ active: isActive('/gestion-residentes') }"
              :aria-current="isActive('/gestion-residentes') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-people-fill"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Gestión Residentes</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
          
          <li class="nav-item" role="listitem">
            <router-link 
              to="/gestion-personal" 
              class="nav-link" 
              :class="{ active: isActive('/gestion-personal') }"
              :aria-current="isActive('/gestion-personal') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-person-badge-fill"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Gestión Personal</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
          
          <li class="nav-item" role="listitem">
            <router-link 
              to="/gastos-comunes" 
              class="nav-link" 
              :class="{ active: isActive('/gastos-comunes') }"
              :aria-current="isActive('/gastos-comunes') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-cash-stack"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Gastos Comunes</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
        </ul>
      </div>
      
      <div class="nav-section">
        <h2 class="nav-section-title" v-if="!sidebarCollapsed">
          <i class="bi bi-graph-up" aria-hidden="true"></i>
          Análisis
        </h2>
        
        <ul class="nav-list" role="list">
          <li class="nav-item" role="listitem">
            <router-link 
              to="/estadisticas" 
              class="nav-link" 
              :class="{ active: isActive('/estadisticas') }"
              :aria-current="isActive('/estadisticas') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-bar-chart-fill"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Estadísticas</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
          
          <li class="nav-item" role="listitem">
            <router-link 
              to="/reportes" 
              class="nav-link" 
              :class="{ active: isActive('/reportes') }"
              :aria-current="isActive('/reportes') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-file-earmark-text"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Reportes</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
        </ul>
      </div>
      
      <div class="nav-section">
        <h2 class="nav-section-title" v-if="!sidebarCollapsed">
          <i class="bi bi-tools" aria-hidden="true"></i>
          Utilidades
        </h2>
        
        <ul class="nav-list" role="list">
          <li class="nav-item" role="listitem">
            <router-link 
              to="/herramientas" 
              class="nav-link" 
              :class="{ active: isActive('/herramientas') }"
              :aria-current="isActive('/herramientas') ? 'page' : undefined"
            >
              <div class="nav-icon" aria-hidden="true">
                <i class="bi bi-gear-fill"></i>
              </div>
              <span class="nav-text" v-if="!sidebarCollapsed">Herramientas</span>
              <div class="nav-indicator" aria-hidden="true"></div>
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
    
    <!-- Footer del sidebar -->
    <footer class="sidebar-footer" v-if="!sidebarCollapsed">
      <div class="user-info">
        <div class="user-avatar" aria-hidden="true">
          <i class="bi bi-person-circle"></i>
        </div>
        <div class="user-details">
          <span class="user-name">{{ currentUser?.name || 'Administrador' }}</span>
          <span class="user-role">{{ currentUser?.role || 'Sistema' }}</span>
        </div>
      </div>
      
      <!-- Acciones del usuario -->
      <div class="user-actions">
        <button
          @click="logout"
          class="user-action-btn"
          aria-label="Cerrar sesión"
          type="button"
        >
          <i class="bi bi-box-arrow-right" aria-hidden="true"></i>
          <span>Cerrar Sesión</span>
        </button>
      </div>
    </footer>
  </aside>
</template>

<script>
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAppStore } from '@/stores/app';

export default {
  name: 'PageSidebar',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const appStore = useAppStore();
    
    const sidebarCollapsed = computed(() => appStore.sidebarCollapsed);
    const currentUser = computed(() => appStore.currentUser);
    
    const toggleSidebar = () => {
      appStore.toggleSidebar();
    };
    
    const logout = () => {
      // Limpiar datos de sesión del localStorage
      localStorage.removeItem('isAuthenticated');
      localStorage.removeItem('userEmail');
      localStorage.removeItem('rememberMe');
      
      // Limpiar el store
      appStore.logout();
      
      // Redirigir al login usando Vue Router
      router.push('/login');
    };
    
    const isActive = (path) => {
      return route.path === path;
    };
    
    return {
      sidebarCollapsed,
      currentUser,
      toggleSidebar,
      logout,
      isActive,
      router
    };
  }
};
</script>

<style scoped>
.sidebar {
  width: 280px;
  height: 100vh;
  background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
  color: white;
  display: flex;
  flex-direction: column;
  position: fixed;
  left: 0;
  top: 0;
  z-index: var(--z-fixed);
  box-shadow: 4px 0 20px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  transition: all var(--transition-normal);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-collapsed {
  width: 80px;
}

.sidebar-header {
  padding: var(--space-6) var(--space-4);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.logo-icon {
  font-size: 2rem;
  color: #3b82f6;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  flex-shrink: 0;
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sidebar-toggle {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  padding: var(--space-2);
  border-radius: var(--border-radius-md);
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
}

.sidebar-toggle:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.sidebar-toggle:focus {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

.sidebar-nav {
  flex: 1;
  padding: var(--space-6) 0;
  overflow-y: auto;
}

.nav-section {
  margin-bottom: var(--space-8);
}

.nav-section-title {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #94a3b8;
  padding: 0 var(--space-6) var(--space-3);
  margin: 0;
  display: flex;
  align-items: center;
  gap: var(--space-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin: var(--space-1) 0;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: var(--space-3) var(--space-6);
  color: #cbd5e1;
  text-decoration: none;
  border-radius: 0 var(--border-radius-xl) var(--border-radius-xl) 0;
  margin-right: var(--space-4);
  transition: all var(--transition-normal);
  position: relative;
  overflow: hidden;
  white-space: nowrap;
}

.nav-link::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 0;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  transition: width var(--transition-normal);
  z-index: -1;
}

.nav-link:hover {
  color: white;
  background: rgba(59, 130, 246, 0.1);
  transform: translateX(5px);
}

.nav-link:hover::before {
  width: 100%;
}

.nav-link.active {
  color: white;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
  transform: translateX(5px);
}

.nav-link.active::before {
  width: 100%;
}

.nav-icon {
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--border-radius-lg);
  background: rgba(255, 255, 255, 0.1);
  margin-right: var(--space-3);
  transition: all var(--transition-normal);
  flex-shrink: 0;
}

.nav-link:hover .nav-icon {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

.nav-link.active .nav-icon {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

.nav-text {
  font-weight: 500;
  font-size: 0.95rem;
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nav-indicator {
  width: 0.25rem;
  height: 0.25rem;
  background: #3b82f6;
  border-radius: 50%;
  opacity: 0;
  transition: all var(--transition-normal);
  flex-shrink: 0;
}

.nav-link.active .nav-indicator {
  opacity: 1;
  transform: scale(1.5);
}

.sidebar-footer {
  padding: var(--space-6);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
}

.user-info {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3);
  background: rgba(255, 255, 255, 0.05);
  border-radius: var(--border-radius-xl);
  transition: all var(--transition-normal);
  margin-bottom: var(--space-4);
}

.user-info:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

.user-avatar {
  width: 2.5rem;
  height: 2.5rem;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  color: white;
  flex-shrink: 0;
}

.user-details {
  display: flex;
  flex-direction: column;
  min-width: 0;
  flex: 1;
}

.user-name {
  font-weight: 600;
  font-size: 0.9rem;
  color: white;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-role {
  font-size: 0.75rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.user-action-btn {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: var(--border-radius-lg);
  color: #fca5a5;
  cursor: pointer;
  transition: all var(--transition-normal);
  font-size: 0.875rem;
  font-weight: 500;
  width: 100%;
  justify-content: center;
}

.user-action-btn:hover {
  background: rgba(239, 68, 68, 0.2);
  border-color: rgba(239, 68, 68, 0.3);
  color: #fecaca;
  transform: translateY(-1px);
}

.user-action-btn:focus {
  outline: 2px solid var(--danger-500);
  outline-offset: 2px;
}

/* Estados colapsados */
.sidebar-collapsed .logo-text,
.sidebar-collapsed .nav-text,
.sidebar-collapsed .nav-section-title,
.sidebar-collapsed .user-details,
.sidebar-collapsed .user-action-btn span {
  display: none;
}

.sidebar-collapsed .nav-link {
  padding: var(--space-3);
  margin-right: var(--space-2);
  justify-content: center;
}

.sidebar-collapsed .nav-icon {
  margin-right: 0;
}

.sidebar-collapsed .sidebar-toggle {
  transform: rotate(180deg);
}

/* Animaciones */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.nav-item {
  animation: slideIn 0.3s ease forwards;
}

.nav-item:nth-child(1) { animation-delay: 0.1s; }
.nav-item:nth-child(2) { animation-delay: 0.2s; }
.nav-item:nth-child(3) { animation-delay: 0.3s; }
.nav-item:nth-child(4) { animation-delay: 0.4s; }
.nav-item:nth-child(5) { animation-delay: 0.5s; }
.nav-item:nth-child(6) { animation-delay: 0.6s; }

/* Responsive */
@media (max-width: 1024px) {
  .sidebar {
    width: 250px;
  }
  
  .nav-text {
    font-size: 0.85rem;
  }
  
  .logo-text {
    font-size: 1.25rem;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
    z-index: var(--z-fixed);
  }
  
  .nav-text {
    display: none;
  }
  
  .nav-icon {
    margin-right: 0;
  }
  
  .sidebar-header,
  .sidebar-footer {
    display: none;
  }
  
  .nav-link {
    padding: var(--space-3) var(--space-4);
    margin-right: var(--space-2);
  }
}

/* Scrollbar personalizado */
.sidebar::-webkit-scrollbar {
  width: 6px;
}

.sidebar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

.sidebar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.sidebar::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}

/* Accesibilidad */
@media (prefers-reduced-motion: reduce) {
  .nav-item {
    animation: none;
  }
  
  .nav-link,
  .user-info,
  .user-action-btn {
    transition: none;
  }
}
</style>
  