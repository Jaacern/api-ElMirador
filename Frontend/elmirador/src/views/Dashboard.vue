<template>
  <div id="app">
    <Sidebar />
    <main class="main-content" :class="{ 'sidebar-collapsed': sidebarCollapsed }">
      <router-view />
    </main>
    
    <!-- Alerta global personalizada -->
    <CustomAlert
      :show="alertState.show"
      :type="alertState.type"
      :title="alertState.title"
      :message="alertState.message"
      :show-confirm="alertState.showConfirm"
      :show-cancel="alertState.showCancel"
      :confirm-text="alertState.confirmText"
      :cancel-text="alertState.cancelText"
      :auto-close="alertState.autoClose"
      :auto-close-delay="alertState.autoCloseDelay"
      @close="cerrarAlerta"
      @confirm="onConfirmarAlerta"
      @cancel="onCancelarAlerta"
    />

    <!-- Chatbot flotante -->
    <ChatbotComponent />
  </div>
</template>

<script>
import { computed } from 'vue';
import Sidebar from '../components/Sidebar.vue';
import CustomAlert from '../components/CustomAlert.vue';
import ChatbotComponent from '../components/Chatbot.vue';
import { useAppStore } from '@/stores/app';

export default {
  name: 'DashboardView',
  components: {
    Sidebar,
    CustomAlert,
    ChatbotComponent
  },
  setup() {
    const appStore = useAppStore();
    const sidebarCollapsed = computed(() => appStore.sidebarCollapsed);
    
    return {
      sidebarCollapsed
    };
  },
  data() {
    return {
      alertState: {
        show: false,
        type: 'info',
        title: '',
        message: '',
        showConfirm: false,
        showCancel: false,
        confirmText: 'Aceptar',
        cancelText: 'Cancelar',
        autoClose: true,
        autoCloseDelay: 3000
      }
    };
  },
  mounted() {
    // Escuchar eventos de actualización de alertas
    window.addEventListener('alert-update', (event) => {
      this.alertState = { ...event.detail };
    });
  },
  methods: {
    cerrarAlerta() {
      this.alertState.show = false;
    },
    onConfirmarAlerta() {
      if (window.$alert) {
        window.$alert.onConfirmarAlerta();
      }
    },
    onCancelarAlerta() {
      if (window.$alert) {
        window.$alert.onCancelarAlerta();
      }
    }
  }
};
</script>

<style>
/* Layout principal */
#app {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  margin: 0;
  padding: 0;
}

/* Contenido principal */
.main-content {
  flex: 1;
  margin-left: 280px; /* Ancho del sidebar */
  overflow-y: auto;
  background: #e2e8f0;
  min-height: 100vh;
  width: calc(100vw - 280px);
}

/* Responsive */
@media (max-width: 768px) {
  .main-content {
    margin-left: 0;
    width: 100vw;
  }
}

/* Cuando el sidebar está colapsado */
@media (min-width: 769px) {
  .sidebar-collapsed + .main-content {
    margin-left: 80px;
    width: calc(100vw - 80px);
  }
}
</style> 