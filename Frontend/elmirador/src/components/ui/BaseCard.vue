<template>
  <div
    :class="cardClasses"
    :style="cardStyles"
    @click="handleClick"
    @mouseenter="handleMouseEnter"
    @mouseleave="handleMouseLeave"
  >
    <!-- Header -->
    <header v-if="$slots.header || title" class="card-header">
      <slot name="header">
        <h3 v-if="title" class="card-title">
          <i v-if="icon" :class="icon" class="card-title-icon"></i>
          {{ title }}
        </h3>
      </slot>
    </header>

    <!-- Body -->
    <main class="card-body">
      <slot></slot>
    </main>

    <!-- Footer -->
    <footer v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </footer>

    <!-- Loading overlay -->
    <div v-if="loading" class="card-loading-overlay">
      <div class="loading-spinner"></div>
      <span class="loading-text">{{ loadingText }}</span>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  name: 'BaseCard',
  props: {
    title: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: ''
    },
    variant: {
      type: String,
      default: 'default',
      validator: (value) => ['default', 'primary', 'success', 'warning', 'danger', 'info'].includes(value)
    },
    loading: {
      type: Boolean,
      default: false
    },
    loadingText: {
      type: String,
      default: 'Cargando...'
    },
    clickable: {
      type: Boolean,
      default: false
    },
    hoverable: {
      type: Boolean,
      default: true
    },
    elevation: {
      type: String,
      default: 'md',
      validator: (value) => ['none', 'sm', 'md', 'lg', 'xl'].includes(value)
    },
    border: {
      type: Boolean,
      default: true
    },
    padding: {
      type: String,
      default: 'normal',
      validator: (value) => ['none', 'sm', 'normal', 'lg'].includes(value)
    }
  },
  emits: ['click', 'mouseenter', 'mouseleave'],
  setup(props, { emit }) {
    const cardClasses = computed(() => [
      'card-modern',
      `card-${props.variant}`,
      `card-elevation-${props.elevation}`,
      `card-padding-${props.padding}`,
      {
        'card-clickable': props.clickable,
        'card-hoverable': props.hoverable,
        'card-no-border': !props.border,
        'card-loading': props.loading
      }
    ]);

    const cardStyles = computed(() => {
      const styles = {};
      if (props.elevation === 'none') {
        styles.boxShadow = 'none';
      }
      return styles;
    });

    const handleClick = (event) => {
      if (props.clickable) {
        emit('click', event);
      }
    };

    const handleMouseEnter = (event) => {
      emit('mouseenter', event);
    };

    const handleMouseLeave = (event) => {
      emit('mouseleave', event);
    };

    return {
      cardClasses,
      cardStyles,
      handleClick,
      handleMouseEnter,
      handleMouseLeave
    };
  }
};
</script>

<style scoped>
.card-modern {
  position: relative;
  background: white;
  border-radius: var(--border-radius-xl);
  box-shadow: var(--shadow-md);
  border: 1px solid var(--secondary-200);
  transition: all var(--transition-normal);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.card-modern:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.card-header {
  padding: var(--space-6);
  border-bottom: 1px solid var(--secondary-200);
  background: linear-gradient(135deg, #475569, #334155);
  flex-shrink: 0;
}

.card-title {
  margin: 0;
  font-family: var(--font-family-display);
  font-size: var(--text-xl);
  font-weight: 600;
  color: var(--secondary-800);
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.card-title-icon {
  font-size: 1.2em;
  color: var(--primary-500);
}

.card-body {
  padding: var(--space-6);
  flex: 1;
}

.card-footer {
  padding: var(--space-6);
  border-top: 1px solid var(--secondary-200);
  background: var(--secondary-50);
  flex-shrink: 0;
}

/* Variantes */
.card-primary .card-header {
  background: linear-gradient(135deg, #475569, #334155);
}

.card-primary .card-title {
  color: white;
}

.card-primary .card-title-icon {
  color: white;
}

.card-success .card-header {
  background: linear-gradient(135deg, var(--success-500), var(--success-600));
}

.card-success .card-title {
  color: white;
}

.card-success .card-title-icon {
  color: white;
}

.card-warning .card-header {
  background: linear-gradient(135deg, var(--warning-500), var(--warning-600));
}

.card-warning .card-title {
  color: white;
}

.card-warning .card-title-icon {
  color: white;
}

.card-danger .card-header {
  background: linear-gradient(135deg, var(--danger-500), var(--danger-600));
}

.card-danger .card-title {
  color: white;
}

.card-danger .card-title-icon {
  color: white;
}

.card-info .card-header {
  background: linear-gradient(135deg, var(--info-500), var(--info-600));
}

.card-info .card-title {
  color: white;
}

.card-info .card-title-icon {
  color: white;
}

/* Elevaciones */
.card-elevation-none {
  box-shadow: none;
}

.card-elevation-sm {
  box-shadow: var(--shadow-sm);
}

.card-elevation-md {
  box-shadow: var(--shadow-md);
}

.card-elevation-lg {
  box-shadow: var(--shadow-lg);
}

.card-elevation-xl {
  box-shadow: var(--shadow-xl);
}

/* Padding */
.card-padding-none .card-body {
  padding: 0;
}

.card-padding-sm .card-body {
  padding: var(--space-4);
}

.card-padding-normal .card-body {
  padding: var(--space-6);
}

.card-padding-lg .card-body {
  padding: var(--space-8);
}

/* Estados */
.card-clickable {
  cursor: pointer;
}

.card-clickable:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
}

.card-hoverable:hover {
  transform: translateY(-2px);
}

.card-no-border {
  border: none;
}

/* Loading state */
.card-loading {
  pointer-events: none;
}

.card-loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 10;
  backdrop-filter: blur(2px);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--primary-200);
  border-radius: 50%;
  border-top-color: var(--primary-500);
  animation: spin 1s ease-in-out infinite;
  margin-bottom: var(--space-3);
}

.loading-text {
  font-family: var(--font-family-primary);
  font-size: var(--text-sm);
  color: var(--secondary-600);
  font-weight: 500;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .card-header,
  .card-body,
  .card-footer {
    padding: var(--space-4);
  }
  
  .card-title {
    font-size: var(--text-lg);
  }
  
  .card-padding-lg .card-body {
    padding: var(--space-6);
  }
}

/* Animaciones de entrada */
.card-modern {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style> 