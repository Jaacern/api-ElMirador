<template>
  <div id="app">
    <Sidebar />
    <main class="main-content">
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
import Sidebar from '../components/Sidebar.vue';
import CustomAlert from '../components/CustomAlert.vue';
import ChatbotComponent from '../components/Chatbot.vue';

export default {
  name: 'DashboardView',
  components: {
    Sidebar,
    CustomAlert,
    ChatbotComponent
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
  width: 100%;
  overflow: hidden;
}

/* Contenido principal */
.main-content {
  flex: 1;
  margin-left: 280px; /* Ancho del sidebar */
  overflow-y: auto;
  background: #f8f9fa;
  min-height: 100vh;
}

/* Responsive */
@media (max-width: 768px) {
  .main-content {
    margin-left: 0;
  }
}
</style> 