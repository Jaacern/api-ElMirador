<template>
  <transition name="alert-fade">
    <div v-if="show" class="custom-alert-overlay" @click="closeOnOverlay">
      <div class="custom-alert" :class="alertType" @click.stop>
        <div class="alert-header">
          <div class="alert-icon">
            <i :class="iconClass"></i>
          </div>
          <button class="close-btn" @click="close">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="alert-content">
          <h4 class="alert-title">{{ title }}</h4>
          <p class="alert-message">{{ message }}</p>
        </div>
        <div class="alert-actions">
          <button v-if="showConfirm" class="btn btn-primary" @click="confirm">
            {{ confirmText }}
          </button>
          <button v-if="showCancel" class="btn btn-secondary" @click="cancel">
            {{ cancelText }}
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'CustomAlert',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    type: {
      type: String,
      default: 'info',
      validator: value => ['success', 'error', 'warning', 'info'].includes(value)
    },
    title: {
      type: String,
      default: ''
    },
    message: {
      type: String,
      default: ''
    },
    showConfirm: {
      type: Boolean,
      default: false
    },
    showCancel: {
      type: Boolean,
      default: false
    },
    confirmText: {
      type: String,
      default: 'Aceptar'
    },
    cancelText: {
      type: String,
      default: 'Cancelar'
    },
    autoClose: {
      type: Boolean,
      default: true
    },
    autoCloseDelay: {
      type: Number,
      default: 3000
    }
  },
  computed: {
    alertType() {
      return `alert-${this.type}`;
    },
    iconClass() {
      const icons = {
        success: 'fas fa-check-circle',
        error: 'fas fa-exclamation-circle',
        warning: 'fas fa-exclamation-triangle',
        info: 'fas fa-info-circle'
      };
      return icons[this.type] || icons.info;
    }
  },
  watch: {
    show(newVal) {
      if (newVal && this.autoClose) {
        this.startAutoClose();
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    confirm() {
      this.$emit('confirm');
      this.close();
    },
    cancel() {
      this.$emit('cancel');
      this.close();
    },
    closeOnOverlay() {
      this.close();
    },
    startAutoClose() {
      if (this.autoCloseTimer) {
        clearTimeout(this.autoCloseTimer);
      }
      this.autoCloseTimer = setTimeout(() => {
        this.close();
      }, this.autoCloseDelay);
    }
  },
  beforeUnmount() {
    if (this.autoCloseTimer) {
      clearTimeout(this.autoCloseTimer);
    }
  }
}
</script>

<style scoped>
.custom-alert-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.custom-alert {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  max-width: 450px;
  width: 90%;
  overflow: hidden;
  text-align: center;
  position: relative;
}

.alert-header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 20px 0;
  position: relative;
}

.alert-icon {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.alert-icon i {
  display: block;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  color: #666;
  cursor: pointer;
  padding: 5px;
  border-radius: 50%;
  transition: all 0.2s ease;
  position: absolute;
  top: 15px;
  right: 15px;
}

.close-btn:hover {
  background: #f0f0f0;
  color: #333;
}

.alert-content {
  padding: 20px;
  text-align: center;
}

.alert-title {
  margin: 0 0 15px 0;
  font-weight: 700;
  font-size: 1.4rem;
  color: #333;
}

.alert-message {
  margin: 0;
  color: #555;
  line-height: 1.6;
  font-size: 1rem;
}

.alert-actions {
  padding: 0 20px 20px;
  display: flex;
  gap: 12px;
  justify-content: center;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  min-width: 100px;
}

.btn-primary {
  background: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background: var(--primary-dark);
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

/* Tipos de alerta */
.alert-success .alert-icon i {
  color: #10b981;
}

.alert-error .alert-icon i {
  color: #ef4444;
}

.alert-warning .alert-icon i {
  color: #f59e0b;
}

.alert-info .alert-icon i {
  color: #3b82f6;
}

/* Transiciones */
.alert-fade-enter-active,
.alert-fade-leave-active {
  transition: all 0.3s ease-out;
}

.alert-fade-enter-from,
.alert-fade-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

.alert-fade-enter-to,
.alert-fade-leave-from {
  opacity: 1;
  transform: scale(1);
}

/* Responsive */
@media (max-width: 768px) {
  .custom-alert {
    width: 95%;
    margin: 20px;
    max-width: 350px;
  }
  
  .alert-actions {
    flex-direction: column;
    gap: 8px;
  }
  
  .btn {
    width: 100%;
    padding: 14px 20px;
  }
  
  .alert-title {
    font-size: 1.2rem;
  }
  
  .alert-message {
    font-size: 0.95rem;
  }
}
</style> 