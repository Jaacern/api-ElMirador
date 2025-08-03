<template>
  <button
    :class="buttonClasses"
    :disabled="disabled || loading"
    :type="type"
    @click="handleClick"
    @focus="handleFocus"
    @blur="handleBlur"
    :aria-label="ariaLabel"
    :aria-describedby="ariaDescribedby"
  >
    <!-- Loading spinner -->
    <span v-if="loading" class="loading-spinner" aria-hidden="true"></span>
    
    <!-- Icon left -->
    <i v-if="iconLeft && !loading" :class="iconLeft" class="btn-icon-left"></i>
    
    <!-- Content -->
    <span v-if="$slots.default" class="btn-content">
      <slot></slot>
    </span>
    
    <!-- Icon right -->
    <i v-if="iconRight && !loading" :class="iconRight" class="btn-icon-right"></i>
  </button>
</template>

<script>
import { computed } from 'vue';

export default {
  name: 'BaseButton',
  props: {
    variant: {
      type: String,
      default: 'primary',
      validator: (value) => ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'ghost'].includes(value)
    },
    size: {
      type: String,
      default: 'md',
      validator: (value) => ['sm', 'md', 'lg'].includes(value)
    },
    disabled: {
      type: Boolean,
      default: false
    },
    loading: {
      type: Boolean,
      default: false
    },
    type: {
      type: String,
      default: 'button'
    },
    iconLeft: {
      type: String,
      default: ''
    },
    iconRight: {
      type: String,
      default: ''
    },
    fullWidth: {
      type: Boolean,
      default: false
    },
    rounded: {
      type: Boolean,
      default: false
    },
    ariaLabel: {
      type: String,
      default: ''
    },
    ariaDescribedby: {
      type: String,
      default: ''
    }
  },
  emits: ['click', 'focus', 'blur'],
  setup(props, { emit }) {
    const buttonClasses = computed(() => [
      'btn-modern',
      `btn-${props.variant}`,
      `btn-${props.size}`,
      {
        'btn-full-width': props.fullWidth,
        'btn-rounded': props.rounded,
        'btn-loading': props.loading
      }
    ]);

    const handleClick = (event) => {
      if (!props.disabled && !props.loading) {
        emit('click', event);
      }
    };

    const handleFocus = (event) => {
      emit('focus', event);
    };

    const handleBlur = (event) => {
      emit('blur', event);
    };

    return {
      buttonClasses,
      handleClick,
      handleFocus,
      handleBlur
    };
  }
};
</script>

<style scoped>
.btn-modern {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-6);
  font-family: var(--font-family-primary);
  font-size: var(--text-sm);
  font-weight: 500;
  line-height: 1.5;
  border: 1px solid transparent;
  border-radius: var(--border-radius-lg);
  transition: all var(--transition-normal);
  cursor: pointer;
  text-decoration: none;
  overflow: hidden;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

.btn-modern::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left var(--transition-slow);
}

.btn-modern:hover::before {
  left: 100%;
}

.btn-modern:focus {
  outline: 2px solid var(--primary-500);
  outline-offset: 2px;
}

.btn-modern:active {
  transform: translateY(1px);
}

.btn-modern:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.btn-modern:disabled:hover {
  transform: none;
}

/* Variantes */
.btn-primary {
  background: linear-gradient(135deg, var(--primary-500), var(--primary-600));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-primary:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--primary-600), var(--primary-700));
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.btn-secondary {
  background: white;
  color: var(--secondary-700);
  border: 1px solid var(--secondary-300);
  box-shadow: var(--shadow-sm);
}

.btn-secondary:hover:not(:disabled) {
  background: var(--secondary-50);
  border-color: var(--secondary-400);
  box-shadow: var(--shadow-md);
}

.btn-success {
  background: linear-gradient(135deg, var(--success-500), var(--success-600));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-success:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--success-600), var(--success-700));
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.btn-danger {
  background: linear-gradient(135deg, var(--danger-500), var(--danger-600));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-danger:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--danger-600), var(--danger-700));
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.btn-warning {
  background: linear-gradient(135deg, var(--warning-500), var(--warning-600));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-warning:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--warning-600), var(--warning-700));
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.btn-info {
  background: linear-gradient(135deg, var(--info-500), var(--info-600));
  color: white;
  box-shadow: var(--shadow-md);
}

.btn-info:hover:not(:disabled) {
  background: linear-gradient(135deg, var(--info-600), var(--info-700));
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.btn-ghost {
  background: transparent;
  color: var(--secondary-600);
  border: 1px solid transparent;
}

.btn-ghost:hover:not(:disabled) {
  background: var(--secondary-100);
  color: var(--secondary-800);
}

/* Tamaños */
.btn-sm {
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-xs);
}

.btn-lg {
  padding: var(--space-4) var(--space-8);
  font-size: var(--text-base);
}

/* Utilidades */
.btn-full-width {
  width: 100%;
}

.btn-rounded {
  border-radius: var(--border-radius-full);
}

/* Loading state */
.btn-loading {
  pointer-events: none;
}

.loading-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Iconos */
.btn-icon-left,
.btn-icon-right {
  font-size: 1em;
  line-height: 1;
}

.btn-icon-left {
  margin-right: var(--space-1);
}

.btn-icon-right {
  margin-left: var(--space-1);
}

/* Responsive */
@media (max-width: 768px) {
  .btn-modern {
    padding: var(--space-3) var(--space-4);
    font-size: var(--text-sm);
  }
  
  .btn-lg {
    padding: var(--space-4) var(--space-6);
  }
}
</style> 