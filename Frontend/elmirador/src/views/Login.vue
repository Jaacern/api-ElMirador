<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-card">
        <div class="login-header">
          <div class="logo">
            <i class="bi bi-building"></i>
            <h2>El Mirador</h2>
          </div>
          <p class="login-subtitle">Accede a tu panel de administración</p>
        </div>

        <form @submit.prevent="handleLogin" class="login-form">
          <div class="form-group">
            <label for="email" class="form-label">Email</label>
            <div class="input-group">
              <span class="input-group-text">
                <i class="bi bi-envelope"></i>
              </span>
              <input
                type="email"
                id="email"
                v-model="form.email"
                class="form-control"
                placeholder="tu@email.com"
                required
                :class="{ 'is-invalid': errors.email }"
              >
            </div>
            <div v-if="errors.email" class="invalid-feedback">
              {{ errors.email }}
            </div>
          </div>

          <div class="form-group">
            <label for="password" class="form-label">Contraseña</label>
            <div class="input-group">
              <span class="input-group-text">
                <i class="bi bi-lock"></i>
              </span>
              <input
                :type="showPassword ? 'text' : 'password'"
                id="password"
                v-model="form.password"
                class="form-control"
                placeholder="Tu contraseña"
                required
                :class="{ 'is-invalid': errors.password }"
              >
              <button
                type="button"
                class="btn btn-outline-secondary"
                @click="togglePassword"
              >
                <i :class="showPassword ? 'bi bi-eye-slash' : 'bi bi-eye'"></i>
              </button>
            </div>
            <div v-if="errors.password" class="invalid-feedback">
              {{ errors.password }}
            </div>
          </div>

          <div class="form-group">
            <div class="form-check">
              <input
                type="checkbox"
                id="remember"
                v-model="form.remember"
                class="form-check-input"
              >
              <label class="form-check-label" for="remember">
                Recordar mi sesión
              </label>
            </div>
          </div>

          <button
            type="submit"
            class="btn btn-primary w-100"
            :disabled="isLoading"
          >
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
            <i v-else class="bi bi-box-arrow-in-right me-2"></i>
            {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
          </button>
        </form>

        <div class="login-footer">
          <a href="#" class="forgot-password">¿Olvidaste tu contraseña?</a>
          <div class="divider">
            <span>o</span>
          </div>
          <router-link to="/" class="btn btn-outline-secondary w-100">
            <i class="bi bi-arrow-left me-2"></i>
            Volver al Inicio
          </router-link>
        </div>

        <!-- Demo Credentials -->
        <div class="demo-credentials">
          <h6>Credenciales de Demo:</h6>
          <div class="demo-item">
            <strong>Email:</strong> admin@elmirador.com
          </div>
          <div class="demo-item">
            <strong>Contraseña:</strong> admin123
          </div>
        </div>
      </div>
    </div>

    <!-- Background Elements -->
    <div class="background-elements">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      form: {
        email: '',
        password: '',
        remember: false
      },
      errors: {},
      isLoading: false,
      showPassword: false
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },

    validateForm() {
      this.errors = {};

      if (!this.form.email) {
        this.errors.email = 'El email es requerido';
      } else if (!this.isValidEmail(this.form.email)) {
        this.errors.email = 'Ingresa un email válido';
      }

      if (!this.form.password) {
        this.errors.password = 'La contraseña es requerida';
      } else if (this.form.password.length < 6) {
        this.errors.password = 'La contraseña debe tener al menos 6 caracteres';
      }

      return Object.keys(this.errors).length === 0;
    },

    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    },

    async handleLogin() {
      if (!this.validateForm()) {
        return;
      }

      this.isLoading = true;

      try {
        // Simular llamada a API
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Validar credenciales de demo
        if (this.form.email === 'admin@elmirador.com' && this.form.password === 'admin123') {
          // Guardar datos de sesión
          localStorage.setItem('isAuthenticated', 'true');
          localStorage.setItem('userEmail', this.form.email);
          
          if (this.form.remember) {
            localStorage.setItem('rememberMe', 'true');
          }

          // Redirigir al dashboard
          this.$router.push('/dashboard');
        } else {
          this.errors.password = 'Credenciales incorrectas. Usa las credenciales de demo.';
        }
      } catch (error) {
        this.errors.password = 'Error al iniciar sesión. Intenta nuevamente.';
      } finally {
        this.isLoading = false;
      }
    }
  },

  mounted() {
    // Verificar si ya está autenticado
    if (localStorage.getItem('isAuthenticated') === 'true') {
      this.$router.push('/dashboard');
    }
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.login-container {
  width: 100%;
  max-width: 400px;
  padding: 2rem;
  z-index: 10;
}

.login-card {
  background: white;
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  position: relative;
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.logo i {
  font-size: 2rem;
  color: var(--primary-color);
}

.logo h2 {
  margin: 0;
  font-weight: 700;
  color: var(--dark-color);
}

.login-subtitle {
  color: var(--secondary-color);
  margin: 0;
  font-size: 1rem;
}

.login-form {
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  font-weight: 600;
  color: var(--dark-color);
  margin-bottom: 0.5rem;
}

.input-group-text {
  background: #f8fafc;
  border-color: #e2e8f0;
  color: var(--secondary-color);
}

.form-control {
  border-color: #e2e8f0;
  border-radius: 10px;
  padding: 0.75rem 1rem;
  transition: all 0.2s ease;
}

.form-control:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.2rem rgba(37, 99, 235, 0.25);
}

.form-control.is-invalid {
  border-color: var(--danger-color);
}

.invalid-feedback {
  display: block;
  color: var(--danger-color);
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

.form-check-input:checked {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.form-check-label {
  color: var(--secondary-color);
  font-size: 0.9rem;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  border: none;
  border-radius: 10px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-primary:disabled {
  opacity: 0.7;
  transform: none;
}

.login-footer {
  text-align: center;
}

.forgot-password {
  color: var(--primary-color);
  text-decoration: none;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  display: block;
}

.forgot-password:hover {
  text-decoration: underline;
}

.divider {
  position: relative;
  text-align: center;
  margin: 1.5rem 0;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: #e2e8f0;
}

.divider span {
  background: white;
  padding: 0 1rem;
  color: var(--secondary-color);
  font-size: 0.9rem;
}

.btn-outline-secondary {
  border-color: #e2e8f0;
  color: var(--secondary-color);
  border-radius: 10px;
  padding: 0.75rem 1.5rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.btn-outline-secondary:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
  color: var(--dark-color);
}

.demo-credentials {
  margin-top: 2rem;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
}

.demo-credentials h6 {
  margin: 0 0 0.5rem 0;
  color: var(--dark-color);
  font-weight: 600;
}

.demo-item {
  font-size: 0.875rem;
  color: var(--secondary-color);
  margin-bottom: 0.25rem;
}

.demo-item strong {
  color: var(--dark-color);
}

/* Background Elements */
.background-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  animation: float 6s ease-in-out infinite;
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 150px;
  height: 150px;
  top: 60%;
  right: 15%;
  animation-delay: 2s;
}

.shape-3 {
  width: 80px;
  height: 80px;
  bottom: 20%;
  left: 20%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .login-container {
    padding: 1rem;
  }
  
  .login-card {
    padding: 2rem;
  }
  
  .logo h2 {
    font-size: 1.5rem;
  }
  
  .logo i {
    font-size: 1.5rem;
  }
}
</style> 