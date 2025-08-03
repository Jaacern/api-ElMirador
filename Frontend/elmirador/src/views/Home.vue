<template>
  <div class="landing-page">
    <!-- Header/Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container">
        <a class="navbar-brand" href="#">
          <i class="bi bi-building"></i>
          El Mirador
        </a>
        <div class="navbar-nav ms-auto">
          <a class="nav-link" href="#inicio">Inicio</a>
          <a class="nav-link" href="#funcionalidades">Funcionalidades</a>
          <a class="nav-link" href="#precios">Precios</a>
          <a class="nav-link" href="#contacto">Contacto</a>
          <router-link to="/login" class="btn btn-primary ms-3">
            Iniciar Sesión
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section id="inicio" class="hero-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <div class="hero-content">
              <span class="hero-badge">Solución Definitiva para Edificios</span>
              <h1 class="hero-title">
                Guía Definitiva para la Gestión Inteligente
              </h1>
              <p class="hero-subtitle">
                Transforma la forma en que administras edificios residenciales con nuestra plataforma integral de gestión.
              </p>
              <div class="hero-buttons">
                <router-link to="/login" class="btn btn-primary btn-lg">
                  Comenzar Prueba Gratuita
                </router-link>
              </div>
              <div class="hero-features">
                <span class="feature-item">Sin tarjeta de crédito requerida</span>
                <span class="feature-item">Soporte 24/7</span>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="hero-visuals">
              <div class="floating-card card-1">
                <h6>Ingresos Mensuales</h6>
                <div class="chart-value">$89,200</div>
              </div>
              <div class="floating-card card-2">
                <h6>Promedio de Pagos</h6>
                <div class="chart-value">$1,200</div>
              </div>
              <div class="floating-card card-3">
                <h6>Crecimiento de Residentes</h6>
                <div class="chart-value">45,623</div>
              </div>
            </div>
          </div>
        </div>
        <div class="trust-indicators">
          <p>Confiado por empresas alrededor del mundo</p>
          <div class="trust-logos">
            <span>El Mirador</span>
            <span>Goldex</span>
            <span>Elitex</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Advanced Features Section -->
    <section class="features-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <div class="feature-card">
              <h3>IA para gestión inteligente de edificios</h3>
              <div class="ai-diagram">
                <div class="ai-node">Chat Bot</div>
                <div class="ai-node">Chat en Vivo</div>
                <div class="ai-node">Soporte por Email</div>
                <div class="ai-node">Gestión Automática</div>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <h2>Características de Seguridad Avanzadas</h2>
            <p>Nuestra plataforma cuenta con las más altas medidas de seguridad para proteger la información de tu edificio. Utilizamos encriptación de nivel bancario y respaldos automáticos para garantizar que tus datos estén siempre seguros.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- AI Optimization Section -->
    <section class="ai-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <h2>Optimiza la Interacción con IA Avanzada</h2>
            <p>Nuestro sistema de inteligencia artificial te ayuda a gestionar tu edificio de manera más eficiente, automatizando tareas repetitivas y proporcionando insights valiosos para la toma de decisiones.</p>
            <div class="ai-features">
              <div class="ai-feature">
                <i class="bi bi-clock"></i>
                <div>
                  <h5>Insights en Tiempo Real</h5>
                  <p>Monitorea el estado de tu edificio en tiempo real</p>
                </div>
              </div>
              <div class="ai-feature">
                <i class="bi bi-shield-check"></i>
                <div>
                  <h5>Garantía de Privacidad</h5>
                  <p>Protección completa de datos de residentes</p>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="ai-image">
              <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500" alt="Profesional trabajando" class="img-fluid rounded">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Scalable Solutions Section -->
    <section class="scalable-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <h2>Soluciones Escalables</h2>
            <p>Nuestra plataforma crece contigo. Desde pequeños edificios hasta complejos residenciales, El Mirador se adapta a tus necesidades específicas.</p>
          </div>
          <div class="col-lg-6">
            <div class="row">
              <div class="col-md-6">
                <div class="stats-card">
                  <h6>Estadísticas de Facturación</h6>
                  <div class="stats-value">4,198</div>
                  <div class="stats-breakdown">
                    <span>Total Facturas</span>
                    <span>Facturas Pagadas</span>
                    <span>Facturas Pendientes</span>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="stats-card">
                  <h6>Actividad de Usuarios</h6>
                  <div class="chart-placeholder">
                    <div class="chart-line"></div>
                    <div class="chart-line"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

         <!-- Pricing Section -->
     <section class="pricing-section">
       <div class="container">
         <div class="row">
           <div class="col-lg-8 mx-auto text-center">
             <span class="pricing-badge">Características Principales</span>
             <h2>Fácil de Comenzar, Fácil de Escalar</h2>
             <p class="pricing-subtitle">Nos enorgullece nuestra atención al detalle y compromiso con la satisfacción del cliente.</p>
             
             <!-- Billing Toggle -->
             <div class="billing-toggle">
               <span class="toggle-label" :class="{ active: billingPeriod === 'monthly' }">Mensual</span>
               <div class="toggle-switch" @click="toggleBilling">
                 <div class="toggle-slider" :class="{ 'slide-right': billingPeriod === 'yearly' }"></div>
               </div>
               <span class="toggle-label" :class="{ active: billingPeriod === 'yearly' }">Anual</span>
               <span class="discount-badge" v-if="billingPeriod === 'yearly'">Ahorra 20%</span>
             </div>
           </div>
         </div>
         
         <!-- Pricing Cards -->
         <div class="row g-4 justify-content-center mt-5">
           <div class="col-lg-4 col-md-6">
             <div class="pricing-card">
               <div class="card-header">
                 <h3>Plan Básico</h3>
                 <div class="price">
                   <span class="currency">$</span>
                   <span class="amount">{{ billingPeriod === 'monthly' ? '29' : '23' }}</span>
                   <span class="period">/mes</span>
                 </div>
                 <p class="card-description">Gratis para uso personal</p>
               </div>
               <div class="card-features">
                 <ul>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Hasta 50 residentes</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>2 GB almacenamiento por sitio</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Hasta 7 páginas por sitio</span>
                   </li>
                   <li class="feature-excluded">
                     <i class="bi bi-x"></i>
                     <span>SSL gratuito para dominio personalizado</span>
                   </li>
                   <li class="feature-excluded">
                     <i class="bi bi-x"></i>
                     <span>Conectar dominio personalizado</span>
                   </li>
                 </ul>
               </div>
               <div class="card-action">
                 <button class="btn btn-outline-dark w-100">
                   Elegir Plan
                   <i class="bi bi-arrow-right ms-2"></i>
                 </button>
               </div>
             </div>
           </div>
           
           <div class="col-lg-4 col-md-6">
             <div class="pricing-card featured">
               <div class="featured-badge">Más Popular</div>
               <div class="card-header">
                 <h3>Plan Estándar</h3>
                 <div class="price">
                   <span class="currency">$</span>
                   <span class="amount">{{ billingPeriod === 'monthly' ? '59' : '47' }}</span>
                   <span class="period">/mes</span>
                 </div>
                 <p class="card-description">Para startups, facturado mensualmente</p>
               </div>
               <div class="card-features">
                 <ul>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Hasta 200 residentes</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>7 GB almacenamiento por sitio</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Hasta 20 páginas por sitio</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>SSL gratuito para dominio personalizado</span>
                   </li>
                   <li class="feature-excluded">
                     <i class="bi bi-x"></i>
                     <span>Conectar dominio personalizado</span>
                   </li>
                 </ul>
               </div>
               <div class="card-action">
                 <button class="btn btn-primary w-100">
                   Elegir Plan
                   <i class="bi bi-arrow-right ms-2"></i>
                 </button>
               </div>
             </div>
           </div>
           
           <div class="col-lg-4 col-md-6">
             <div class="pricing-card">
               <div class="card-header">
                 <h3>Plan Premium</h3>
                 <div class="price">
                   <span class="currency">$</span>
                   <span class="amount">{{ billingPeriod === 'monthly' ? '99' : '79' }}</span>
                   <span class="period">/mes</span>
                 </div>
                 <p class="card-description">Para escalar, facturado mensualmente</p>
               </div>
               <div class="card-features">
                 <ul>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Residentes ilimitados</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>15 GB almacenamiento por sitio</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Hasta 30 páginas por sitio</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>SSL gratuito para dominio personalizado</span>
                   </li>
                   <li class="feature-included">
                     <i class="bi bi-check"></i>
                     <span>Conectar dominio personalizado</span>
                   </li>
                 </ul>
               </div>
               <div class="card-action">
                 <button class="btn btn-outline-dark w-100">
                   Elegir Plan
                   <i class="bi bi-arrow-right ms-2"></i>
                 </button>
               </div>
             </div>
           </div>
         </div>
       </div>
     </section>

    <!-- Collaboration Tools Section -->
    <section class="collaboration-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <div class="collaboration-image">
              <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=500" alt="Profesional en oficina" class="img-fluid rounded">
              <div class="overlay-card">
                <h6>Puntuación de Riesgo</h6>
                <div class="risk-score">70</div>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <h2>Herramientas de Colaboración para la Productividad</h2>
            <p>Facilita la comunicación entre administradores, personal y residentes con nuestras herramientas integradas de colaboración.</p>
            <ul class="collaboration-features">
              <li><i class="bi bi-check"></i> Interfaz fácil de usar</li>
              <li><i class="bi bi-check"></i> Dashboard centralizado</li>
              <li><i class="bi bi-check"></i> Características intuitivas</li>
              <li><i class="bi bi-check"></i> Herramientas de comunicación integradas</li>
            </ul>
            <router-link to="/login" class="btn btn-primary">
              Leer Más Sobre Nosotros
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <h2>Preguntas Frecuentes</h2>
            <div class="faq-list">
              <div class="faq-item">
                <h5>¿Cómo puede escalar tu sistema de precios?</h5>
                <p>Nuestros precios se adaptan al tamaño de tu edificio y número de residentes.</p>
              </div>
              <div class="faq-item">
                <h5>¿Qué información se requiere para registrarse?</h5>
                <p>Solo necesitas información básica de tu edificio y datos de contacto.</p>
              </div>
              <div class="faq-item">
                <h5>¿Necesito pagar por la prueba gratuita?</h5>
                <p>No, la prueba gratuita es completamente gratuita sin compromisos.</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="testimonial-card">
              <div class="testimonial-header">
                <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100" alt="Dennis J. Lester" class="testimonial-avatar">
                <div>
                  <h5>Dennis J. Lester</h5>
                  <p>CEO & Fundador</p>
                </div>
              </div>
              <p class="testimonial-text">"El Mirador ha transformado completamente la forma en que gestionamos nuestro edificio. La eficiencia ha aumentado significativamente."</p>
              <div class="testimonial-rating">
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <span>4.5/5 en Trustpilot</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Revolution Section -->
    <section class="revolution-section">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <h2>El Mirador está Revolucionando la Gestión de Edificios</h2>
            <div class="revolution-features">
              <div class="revolution-feature">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=100" alt="Productividad" class="feature-icon">
                <h5>Impulsa tu Productividad</h5>
                <p>Automatiza tareas repetitivas y enfócate en lo importante</p>
              </div>
              <div class="revolution-feature">
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=100" alt="Flujo de trabajo" class="feature-icon">
                <h5>Optimiza tu Flujo de Trabajo</h5>
                <p>Organiza y simplifica todos los procesos administrativos</p>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="cta-section">
              <h3>¡Listo para Obtener 14 Días de Prueba Gratuita!</h3>
              <p>Comienza tu prueba gratuita hoy y experimenta todo el poder de nuestra plataforma.</p>
              <router-link to="/login" class="btn btn-primary btn-lg">
                Comenzar 14 Días Gratis
              </router-link>
              <div class="cta-visual">
                <div class="chart-card">
                  <div class="main-chart">45,623</div>
                  <div class="sub-chart"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="row">
          <div class="col-lg-3">
            <h5>Suscríbete a Nuestro Boletín</h5>
            <div class="newsletter-form">
              <input type="email" class="form-control" placeholder="Tu email">
              <button class="btn btn-primary">Suscribirse</button>
            </div>
          </div>
          <div class="col-lg-3">
            <h5>Enlaces Rápidos</h5>
            <ul class="footer-links">
              <li><a href="#inicio">Inicio</a></li>
              <li><a href="#funcionalidades">Funcionalidades</a></li>
              <li><a href="#precios">Precios</a></li>
              <li><a href="#contacto">Contacto</a></li>
            </ul>
          </div>
          <div class="col-lg-3">
            <h5>Recursos</h5>
            <ul class="footer-links">
              <li><a href="#">Blog</a></li>
              <li><a href="#">Casos de Estudio</a></li>
              <li><a href="#">Términos y Condiciones</a></li>
            </ul>
          </div>
          <div class="col-lg-3">
            <h5>Contáctanos</h5>
            <div class="contact-info">
              <p>info@elmirador.com</p>
              <p>Santiago, Chile</p>
              <p>+56 9 1234 5678</p>
            </div>
          </div>
        </div>
        <hr>
        <div class="footer-bottom">
          <p>&copy; El Mirador 2024. Todos los derechos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      billingPeriod: 'monthly'
    };
  },
  methods: {
    toggleBilling() {
      this.billingPeriod = this.billingPeriod === 'monthly' ? 'yearly' : 'monthly';
    }
  },
  mounted() {
    // Smooth scrolling para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }
};
</script>

<style scoped>
.landing-page {
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
  width: 100%;
  max-width: 100%;
}

/* Navbar */
.navbar {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 1rem 0;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.navbar-brand {
  font-weight: 700;
  font-size: 1.5rem;
  color: #1e293b;
}

.navbar-nav .nav-link {
  color: #64748b;
  font-weight: 500;
  margin: 0 1rem;
  transition: color 0.3s ease;
}

.navbar-nav .nav-link:hover {
  color: #3b82f6;
}

/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  color: white;
  padding: 120px 0 80px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
}

.hero-badge {
  background: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 1rem;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.9;
  line-height: 1.6;
  color: #cbd5e1;
}

.hero-buttons .btn {
  padding: 1rem 2rem;
  font-weight: 600;
  border-radius: 10px;
  font-size: 1.1rem;
}

.hero-features {
  margin-top: 2rem;
  display: flex;
  gap: 2rem;
}

.feature-item {
  color: #94a3b8;
  font-size: 0.9rem;
}

.hero-visuals {
  position: relative;
  height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.floating-card {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  color: #1e293b;
  min-width: 200px;
  margin: 0.5rem;
  transform: translateY(0);
  transition: transform 0.3s ease;
}

.floating-card:hover {
  transform: translateY(-5px);
}

.card-1 {
  align-self: flex-start;
}

.card-2 {
  align-self: flex-end;
}

.card-3 {
  align-self: flex-start;
}

.chart-value {
  font-size: 2rem;
  font-weight: 700;
  color: #3b82f6;
}

.trust-indicators {
  text-align: center;
  margin-top: 4rem;
}

.trust-indicators p {
  color: #94a3b8;
  margin-bottom: 1rem;
}

.trust-logos {
  display: flex;
  justify-content: center;
  gap: 2rem;
  color: #64748b;
  font-weight: 600;
}

/* Features Section */
.features-section {
  padding: 100px 0;
  background: white;
}

.feature-card {
  background: #f8fafc;
  padding: 2rem;
  border-radius: 20px;
  height: 100%;
}

.ai-diagram {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 2rem;
}

.ai-node {
  background: #3b82f6;
  color: white;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
  font-weight: 600;
}

/* AI Section */
.ai-section {
  padding: 100px 0;
  background: #f8fafc;
}

.ai-features {
  margin-top: 2rem;
}

.ai-feature {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 2rem;
}

.ai-feature i {
  font-size: 1.5rem;
  color: #3b82f6;
  margin-top: 0.25rem;
}

.ai-image img {
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
}

/* Scalable Section */
.scalable-section {
  padding: 100px 0;
  background: #3b82f6;
  color: white;
}

.stats-card {
  background: white;
  color: #1e293b;
  padding: 2rem;
  border-radius: 15px;
  margin-bottom: 1rem;
}

.stats-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: #3b82f6;
  margin: 1rem 0;
}

.chart-placeholder {
  height: 100px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: 1rem;
}

.chart-line {
  height: 4px;
  background: #e2e8f0;
  border-radius: 2px;
}

/* Pricing Section */
.pricing-section {
  padding: 100px 0;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  color: white;
}

.pricing-badge {
  background: rgba(59, 130, 246, 0.2);
  color: #60a5fa;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.875rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 1rem;
}

.pricing-subtitle {
  font-size: 1.1rem;
  color: #cbd5e1;
  margin-bottom: 3rem;
}

/* Billing Toggle */
.billing-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 3rem;
}

.toggle-label {
  color: #94a3b8;
  font-weight: 500;
  transition: color 0.3s ease;
}

.toggle-label.active {
  color: white;
}

.toggle-switch {
  width: 60px;
  height: 30px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  position: relative;
  cursor: pointer;
  transition: background 0.3s ease;
}

.toggle-switch:hover {
  background: rgba(255, 255, 255, 0.3);
}

.toggle-slider {
  width: 26px;
  height: 26px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  transition: transform 0.3s ease;
}

.toggle-slider.slide-right {
  transform: translateX(30px);
}

.discount-badge {
  background: #10b981;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-left: 1rem;
}

/* Pricing Cards */
.pricing-card {
  background: white;
  color: #1e293b;
  border-radius: 20px;
  padding: 2rem;
  height: 100%;
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.pricing-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.pricing-card.featured {
  background: #3b82f6;
  color: white;
  transform: scale(1.05);
}

.pricing-card.featured:hover {
  transform: scale(1.05) translateY(-5px);
}

.featured-badge {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  background: #10b981;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.card-header {
  text-align: center;
  margin-bottom: 2rem;
}

.card-header h3 {
  font-weight: 700;
  margin-bottom: 1rem;
}

.price {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
}

.currency {
  font-size: 1.5rem;
  vertical-align: top;
}

.period {
  font-size: 1rem;
  font-weight: 400;
  opacity: 0.7;
}

.card-description {
  color: #64748b;
  font-size: 0.9rem;
}

.pricing-card.featured .card-description {
  color: #cbd5e1;
}

.card-features {
  margin-bottom: 2rem;
}

.card-features ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.card-features li {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.feature-included i {
  color: #10b981;
  font-size: 1.1rem;
}

.feature-excluded i {
  color: #ef4444;
  font-size: 1.1rem;
}

.feature-excluded span {
  opacity: 0.6;
}

.card-action {
  margin-top: auto;
}

.card-action .btn {
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.card-action .btn:hover {
  transform: translateY(-2px);
}

/* Collaboration Section */
.collaboration-section {
  padding: 100px 0;
  background: white;
}

.collaboration-image {
  position: relative;
}

.overlay-card {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background: white;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.risk-score {
  font-size: 2rem;
  font-weight: 700;
  color: #3b82f6;
}

.collaboration-features {
  list-style: none;
  padding: 0;
  margin: 2rem 0;
}

.collaboration-features li {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  color: #64748b;
}

.collaboration-features i {
  color: #10b981;
  font-size: 1.2rem;
}

/* FAQ Section */
.faq-section {
  padding: 100px 0;
  background: #f8fafc;
}

.faq-item {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  margin-bottom: 1rem;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
}

.faq-item h5 {
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.testimonial-card {
  background: #1e293b;
  color: white;
  padding: 2rem;
  border-radius: 20px;
  height: 100%;
}

.testimonial-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.testimonial-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}

.testimonial-rating {
  margin-top: 1rem;
  color: #fbbf24;
}

.testimonial-rating span {
  color: white;
  margin-left: 0.5rem;
}

/* Revolution Section */
.revolution-section {
  padding: 100px 0;
  background: white;
}

.revolution-features {
  margin-top: 2rem;
}

.revolution-feature {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 2rem;
}

.feature-icon {
  width: 60px;
  height: 60px;
  border-radius: 10px;
  object-fit: cover;
}

.cta-section {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  color: white;
  padding: 3rem;
  border-radius: 20px;
  text-align: center;
}

.chart-card {
  background: white;
  color: #1e293b;
  padding: 2rem;
  border-radius: 15px;
  margin-top: 2rem;
}

.main-chart {
  font-size: 2rem;
  font-weight: 700;
  color: #3b82f6;
}

/* Footer */
.footer {
  background: #0f172a;
  color: white;
  padding: 4rem 0 2rem;
}

.newsletter-form {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: #94a3b8;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: white;
}

.contact-info p {
  color: #94a3b8;
  margin-bottom: 0.5rem;
}

.footer-bottom {
  text-align: center;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid #334155;
  color: #64748b;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-visuals {
    height: auto;
    margin-top: 2rem;
    flex-direction: column;
  }
  
  .floating-card {
    margin: 0.5rem 0;
    width: 100%;
    max-width: 300px;
  }
  
  .trust-logos {
    flex-direction: column;
    gap: 1rem;
  }
  
  .newsletter-form {
    flex-direction: column;
  }
  
  .hero-features {
    flex-direction: column;
    gap: 1rem;
  }
  
  .pricing-card.featured {
    transform: none;
  }
  
  .pricing-card.featured:hover {
    transform: translateY(-5px);
  }
  
  .billing-toggle {
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  
  .discount-badge {
    margin-left: 0;
    margin-top: 0.5rem;
  }
  
  .price {
    font-size: 2.5rem;
  }
}
</style> 