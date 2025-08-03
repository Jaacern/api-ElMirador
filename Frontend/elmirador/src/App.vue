<template>
  <div id="app" class="app-container">
    <!-- Sistema de notificaciones -->
    <NotificationSystem />
    
    <!-- Contenido principal -->
    <main class="app-main">
      <router-view v-slot="{ Component }">
        <Transition name="page" mode="out-in">
          <component :is="Component" />
        </Transition>
      </router-view>
    </main>
  </div>
</template>

<script>
import NotificationSystem from '@/components/ui/NotificationSystem.vue';

export default {
  name: 'App',
  components: {
    NotificationSystem
  },
  mounted() {
    // Configurar tema inicial
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    // Configurar idioma
    const savedLanguage = localStorage.getItem('language') || 'es';
    document.documentElement.setAttribute('lang', savedLanguage);
    
    // Configurar preferencias de accesibilidad
    this.setupAccessibility();
  },
  methods: {
    setupAccessibility() {
      // Detectar preferencias de movimiento reducido
      const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
      
      if (prefersReducedMotion.matches) {
        document.documentElement.classList.add('reduced-motion');
      }
      
      // Detectar preferencias de alto contraste
      const prefersHighContrast = window.matchMedia('(prefers-contrast: high)');
      
      if (prefersHighContrast.matches) {
        document.documentElement.classList.add('high-contrast');
      }
      
      // Escuchar cambios en las preferencias
      prefersReducedMotion.addEventListener('change', (e) => {
        if (e.matches) {
          document.documentElement.classList.add('reduced-motion');
        } else {
          document.documentElement.classList.remove('reduced-motion');
        }
      });
      
      prefersHighContrast.addEventListener('change', (e) => {
        if (e.matches) {
          document.documentElement.classList.add('high-contrast');
        } else {
          document.documentElement.classList.remove('high-contrast');
        }
      });
    }
  }
};
</script>

<style>
/* Estilos base de la aplicación */
.app-container {
  min-height: 100vh;
  background: var(--secondary-50);
  font-family: var(--font-family-primary);
  color: var(--secondary-900);
  line-height: 1.6;
}

.app-main {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Transiciones de página */
.page-enter-active,
.page-leave-active {
  transition: all 0.3s ease-in-out;
}

.page-enter-from {
  opacity: 0;
  transform: translateX(20px);
}

.page-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

/* Configuraciones de accesibilidad */
.reduced-motion *,
.reduced-motion *::before,
.reduced-motion *::after {
  animation-duration: 0.01ms !important;
  animation-iteration-count: 1 !important;
  transition-duration: 0.01ms !important;
}

.high-contrast {
  --primary-500: #0000ff;
  --secondary-500: #000000;
  --success-500: #008000;
  --danger-500: #ff0000;
  --warning-500: #ff8000;
}

/* Mejoras de accesibilidad */
@media (prefers-reduced-motion: reduce) {
  .page-enter-active,
  .page-leave-active {
    transition: none;
  }
}

/* Estilos para lectores de pantalla */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Focus visible mejorado */
*:focus-visible {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

/* Estilos para modo oscuro (futuro) */
@media (prefers-color-scheme: dark) {
  :root {
    --secondary-50: #0f172a;
    --secondary-100: #1e293b;
    --secondary-200: #334155;
    --secondary-300: #475569;
    --secondary-400: #64748b;
    --secondary-500: #94a3b8;
    --secondary-600: #cbd5e1;
    --secondary-700: #e2e8f0;
    --secondary-800: #f1f5f9;
    --secondary-900: #f8fafc;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .app-container {
    padding: 0;
  }
}

/* Mejoras de rendimiento */
* {
  box-sizing: border-box;
}

/* Optimizaciones de fuente */
body {
  font-feature-settings: 'liga' 1, 'kern' 1;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
