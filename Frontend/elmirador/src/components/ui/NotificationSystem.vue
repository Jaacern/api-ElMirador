<template>
  <div class="notification-container" role="region" aria-label="Notificaciones">
    <TransitionGroup
      name="notification"
      tag="div"
      class="notification-list"
    >
      <div
        v-for="notification in notifications"
        :key="notification.id"
        :class="notificationClasses(notification)"
        :role="notification.type === 'alert' ? 'alert' : 'status'"
        :aria-live="notification.type === 'alert' ? 'assertive' : 'polite'"
        :aria-describedby="`notification-${notification.id}`"
      >
        <div class="notification-content">
          <div class="notification-icon">
            <i :class="getIcon(notification.type)" aria-hidden="true"></i>
          </div>
          
          <div class="notification-body">
            <h4 v-if="notification.title" class="notification-title">
              {{ notification.title }}
            </h4>
            <p v-if="notification.message" class="notification-message">
              {{ notification.message }}
            </p>
            <div v-if="notification.details" class="notification-details">
              {{ notification.details }}
            </div>
          </div>
          
          <div class="notification-actions">
            <button
              v-if="notification.dismissible !== false"
              @click="removeNotification(notification.id)"
              class="notification-close"
              :aria-label="`Cerrar notificación: ${notification.title || notification.message}`"
              type="button"
            >
              <i class="bi bi-x-lg" aria-hidden="true"></i>
            </button>
          </div>
        </div>
        
        <!-- Progress bar for auto-dismiss -->
        <div
          v-if="notification.autoDismiss && notification.type !== 'alert'"
          class="notification-progress"
          :style="{ animationDuration: `${notification.duration || 5000}ms` }"
        ></div>
      </div>
    </TransitionGroup>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useAppStore } from '@/stores/app';

export default {
  name: 'NotificationSystem',
  setup() {
    const appStore = useAppStore();
    
    const notifications = computed(() => appStore.notifications);
    
    const notificationClasses = (notification) => [
      'notification',
      `notification-${notification.type}`,
      {
        'notification-read': notification.read,
        'notification-unread': !notification.read
      }
    ];
    
    const getIcon = (type) => {
      const icons = {
        success: 'bi bi-check-circle-fill',
        error: 'bi bi-x-circle-fill',
        warning: 'bi bi-exclamation-triangle-fill',
        info: 'bi bi-info-circle-fill',
        alert: 'bi bi-exclamation-circle-fill'
      };
      return icons[type] || icons.info;
    };
    
    const removeNotification = (id) => {
      appStore.removeNotification(id);
    };
    
    return {
      notifications,
      notificationClasses,
      getIcon,
      removeNotification
    };
  }
};
</script>

<style scoped>
.notification-container {
  position: fixed;
  top: var(--space-6);
  right: var(--space-6);
  z-index: var(--z-toast);
  max-width: 400px;
  width: 100%;
  pointer-events: none;
}

.notification-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.notification {
  background: white;
  border-radius: var(--border-radius-xl);
  box-shadow: var(--shadow-xl);
  border: 1px solid var(--secondary-200);
  overflow: hidden;
  position: relative;
  pointer-events: auto;
  animation: slideInRight 0.3s ease-out;
}

.notification-content {
  display: flex;
  align-items: flex-start;
  gap: var(--space-4);
  padding: var(--space-4);
}

.notification-icon {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-size: 1rem;
}

.notification-success .notification-icon {
  background: var(--success-50);
  color: var(--success-600);
}

.notification-error .notification-icon {
  background: var(--danger-50);
  color: var(--danger-600);
}

.notification-warning .notification-icon {
  background: var(--warning-50);
  color: var(--warning-600);
}

.notification-info .notification-icon {
  background: var(--info-50);
  color: var(--info-600);
}

.notification-alert .notification-icon {
  background: var(--danger-50);
  color: var(--danger-600);
}

.notification-body {
  flex: 1;
  min-width: 0;
}

.notification-title {
  margin: 0 0 var(--space-1) 0;
  font-family: var(--font-family-primary);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--secondary-800);
  line-height: 1.4;
}

.notification-message {
  margin: 0;
  font-family: var(--font-family-primary);
  font-size: var(--text-sm);
  color: var(--secondary-600);
  line-height: 1.4;
}

.notification-details {
  margin-top: var(--space-2);
  font-family: var(--font-family-primary);
  font-size: var(--text-xs);
  color: var(--secondary-500);
  line-height: 1.3;
}

.notification-actions {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.notification-close {
  background: none;
  border: none;
  padding: var(--space-1);
  border-radius: var(--border-radius-md);
  color: var(--secondary-400);
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
}

.notification-close:hover {
  background: var(--secondary-100);
  color: var(--secondary-600);
}

.notification-close:focus {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

.notification-progress {
  height: 3px;
  background: var(--primary-500);
  animation: progressShrink linear forwards;
}

@keyframes progressShrink {
  from {
    width: 100%;
  }
  to {
    width: 0%;
  }
}

/* Animaciones de entrada y salida */
.notification-enter-active {
  transition: all 0.3s ease-out;
}

.notification-leave-active {
  transition: all 0.3s ease-in;
}

.notification-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.notification-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

.notification-move {
  transition: transform 0.3s ease;
}

/* Estados */
.notification-unread {
  border-left: 4px solid var(--primary-500);
}

.notification-read {
  opacity: 0.8;
}

/* Responsive */
@media (max-width: 768px) {
  .notification-container {
    top: var(--space-4);
    right: var(--space-4);
    left: var(--space-4);
    max-width: none;
  }
  
  .notification-content {
    padding: var(--space-3);
  }
  
  .notification-title {
    font-size: var(--text-xs);
  }
  
  .notification-message {
    font-size: var(--text-xs);
  }
}

/* Accesibilidad */
@media (prefers-reduced-motion: reduce) {
  .notification-enter-active,
  .notification-leave-active,
  .notification-move {
    transition: none;
  }
  
  .notification-progress {
    animation: none;
  }
}

/* Alto contraste */
@media (prefers-contrast: high) {
  .notification {
    border: 2px solid var(--secondary-800);
  }
  
  .notification-unread {
    border-left: 4px solid var(--primary-900);
  }
}
</style> 